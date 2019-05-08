#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-08 10:10:35
# @Author  : Ivy Mong (davy0328meng@gmail.com)


from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ('owner',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)