#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-06 12:50:49
# @Author  : Ivy Mong (davy0328meng@gmail.com)
# @Link    : https://blog.csdn.net/Eleveil
# @Version : $Id$

from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    
