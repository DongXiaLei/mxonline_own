# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name="课程名")
    desc = models.CharField(max_length=300,verbose_name="课程表表述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(verbose_name="难度等级",max_length=10,choices=(("cj","初级"),("zj","中级"),("gj","高级")))
    learn_times = models.IntegerField(default=0,verbose_name="学习人数")
    students = models.IntegerField(default=0,verbose_name="学习人数")
    favor = models.IntegerField(default=0,verbose_name="s收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m",verbose_name="封面")
    click_nums = models.IntegerField(default=0,verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加数")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="课程")
    name = models.CharField(max_length=100,verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name="章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Video(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,verbose_name="章节")
    name = models.CharField(max_length=100,verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name="视频"
        verbose_name_plural = verbose_name

class CourseResouce(models.Model):
    name = models.CharField(max_length=100,verbose_name="名称")
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="课程")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name="课程文件")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name



