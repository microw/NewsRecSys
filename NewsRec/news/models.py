# -*-coding:utf-8-*-
from django.db import models

# 新闻类别表
class cate(models.Model):
    cate_id = models.CharField(blank=False, max_length=64, verbose_name='ID',unique=True)
    cate_name = models.CharField(blank=False, max_length=64, verbose_name='名字')

    def __str__(self):
        return self.cate_name
    class Meta:
        db_table = 'cate'

# 新闻与新闻相似表
class newsim(models.Model):
    new_id_base = models.CharField(blank=False, max_length=64, verbose_name="ID_base", unique=False)
    new_id_sim = models.CharField(blank=False, max_length=64, verbose_name="ID_sim", unique=False)
    new_correlation = models.FloatField(verbose_name="新闻相关度", blank=False)

    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.new_id_base

    class Meta:
        db_table = 'newsim'


# 新闻表
class new(models.Model):
    new_id = models.CharField(blank=False, max_length=64, verbose_name="ID", unique=True)
    new_cate = models.ForeignKey(cate, related_name="类别", on_delete=False)
    new_time = models.DateTimeField(blank=False, verbose_name="发表时间")
    new_seenum = models.IntegerField(verbose_name="浏览次数", blank=False)  # True表示可不填
    new_disnum = models.IntegerField(verbose_name="跟帖次数", blank=False)  # True表示可不填
    # related_name定义主表对象查询子表时使用的方法名称
    new_title = models.CharField(blank=False, max_length=100, verbose_name="标题")
    new_content = models.TextField(blank=False, verbose_name="新闻内容")

    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.new_title

    class Meta:
        db_table = 'new'
