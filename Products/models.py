# coding:utf-8

from django.db import models
from django.utils import timezone


class Product(models.Model):
    PRODUCTS_CHOIES = (
        ('家用机器人', '家用机器人'),
        ('智能监控', '智能监控'),
        ('人脸识别解决方案', '人脸识别解决方案'),)
    title = models.CharField(max_length=50, verbose_name="产品标题")
    description = models.TextField(verbose_name="产品详情描述")
    producttype = models.CharField(choices=PRODUCTS_CHOIES, max_length=50, verbose_name="产品类型")  # 图片
    price = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True, verbose_name="产品价格")
    publishdate = models.DateTimeField(max_length=20, default=timezone.now, verbose_name="发布时间")
    views = models.PositiveIntegerField(default=0, verbose_name="浏览次数")

    def __str__(self):
        return self.title


class Meta:
    verbose_name = "产品"
    verbose_name_plural = '产品'
    ordering = ('-publishdate',)


class ProductImg(models.Model):
    product = models.ForeignKey(Product, related_name='productImgs', verbose_name="产品", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="图片标题")
    photo = models.ImageField(upload_to='Product/', blank=True, verbose_name="产品图片")


class Meta:
    verbose_name = "产品图片"
    verbose_name_plural = '产品图片'
