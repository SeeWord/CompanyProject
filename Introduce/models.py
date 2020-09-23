# coding:utf-8
from django.db import models


class Award(models.Model):
    description = models.TextField(max_length=1000,blank=True,null=True)
    photo = models.ImageField(upload_to='Award/',blank=True)#图片
