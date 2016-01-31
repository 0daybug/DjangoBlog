#-*- coding:utf-8 -*-
from django.db import models
from datetime import time,tzinfo
from django.core.urlresolvers import reverse
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30,verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name='分类名称')
    index = models.IntegerField(default=999,verbose_name='分类排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


#自定义管理器 用于Archive
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('publish_date')
        for date in date_list:
            date = date['publish_date'].strftime('%Y/%m文章归档')
            if date not in distinct_date_list:
               distinct_date_list.append(date)
        return distinct_date_list


class Article(models.Model):
    title = models.CharField(max_length=30,verbose_name='标题')
    desc = models.CharField(max_length=50,verbose_name='文章描述')
    content = models.TextField(verbose_name='文章正文')
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    tags = models.ManyToManyField(Tag,verbose_name='标签')

    category = models.ForeignKey(Category,blank=True,null=True,verbose_name='分类')

    objects = ArticleManager()

    def get_absolute_url(self):
        path = reverse('detail',kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s"%path

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-publish_date']

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    article = models.ForeignKey(Article,blank=True,null=True,verbose_name='文章')
    pid = models.ForeignKey('self',blank=True,null=True,verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-publish_date']

    def __unicode__(self):
        return str(self.id)


