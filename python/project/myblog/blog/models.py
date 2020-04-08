from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    """文章"""
    title = models.CharField(max_length=100)

    body = models.TextField()   # TextField 来存储大段文本
    created_time =  models.DateTimeField()
    modified_time = models.DateTimeField()  # 存储时间的字段用 DateTimeField 类型

    excerpt = models.CharField(max_length=200, blank=True)  # 摘要

    # 外键关联不同的表
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title