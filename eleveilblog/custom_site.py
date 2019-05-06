#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-06 13:26:09
# @Author  : Ivy Mong (davy0328meng@gmail.com)
# @Link    : https://blog.csdn.net/Eleveil
# @Version : $Id$

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Eleveil Blog'
    site_title = 'Eleveil Blog管理后台'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')
