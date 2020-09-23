# coding:utf-8
from django.contrib import admin
from django.contrib.auth.models import User

admin.site.site_header = '企业信息管理平台'
admin.site.site_title = '企业信息管理平台'

# user = User.objects.get(username='stefen')
# user.set_password('QAZqaz1`')
# user.save()
