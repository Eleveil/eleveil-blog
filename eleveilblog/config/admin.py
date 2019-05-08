from django.contrib import admin
from .models import Link, SideBar
from base_admin import BaseOwnerAdmin
from custom_site import custom_site

@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ['title', 'href', 'status', 'weight', 'created']
    fields = ('title', 'href', 'status', 'weight')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ['title', 'display_type', 'content', 'status', 'created']
    fields = ('title', 'display_type', 'content', 'status')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(SideBarAdmin, self).save_model(request, obj, form, change)