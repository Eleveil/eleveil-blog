from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Category, Tag, Post
from .adminforms import PostAdminForm

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'is_nav', 'post_count', 'created']
    fields = ('name','status','is_nav')

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created']
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'desc','status', 'category', 'tag', 'created', 'operator']
    exclude = ('owner', )    #不展示的字段

    #展示的字段
    # fields = (
    #     ('title','category'),
    #     'desc',
    #     'content',
    #     'status',
    #     'tag')
    fieldsets = (
        ('基础配置', {
            'description': '基础配置',
            'fields': (
                ('title','category'),
                'status'
                )
            }),
        ('内容',{
            'fields':(
                'desc',
                'content',
                ),
            }),
        ('额外信息', {
            'classes': ('collapse', ),
            'fields': (
                'tag',
                ),
            })
    )

    list_display_links = []  #用来配置哪些字段可以作为链接，点击字段，可以进入编辑页面

    list_filter = [CategoryOwnerFilter] #配置页面过滤器，通过这些字段可以锅里列表页
    search_fields = ['titel', 'category__name'] #配置搜索字段

    actions_on_top = True  #动作相关的配置是否显示在顶部
    # actions_on_bottom = True #动作相关的配置是否显示在底部

    # save_on_top = True #保存/编辑/编辑并新建按钮是否现实在顶部

    # filter_horizontal = ('tag',)

    # class Media:
    #     css = {
    #         'all':("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",)
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


