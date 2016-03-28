#coding:utf-8
from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "标签"
    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    tag = models.ForeignKey(Tags)

    class Meta:
        verbose_name = "文章"
        ordering = ['-create_time']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('Post_detail',None)





