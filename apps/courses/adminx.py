# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/4/7 18:22'

import xadmin

from .models import Course,Lesson,Video,CourseResouce

class CourseAdmin(object):

    list_display = ['name','desc','detail','degree','learn_times','students','favor','image','click_nums','add_time']
    search_fields = ['name','desc','detail','degree','learn_times','students','favor','image','click_nums']
    list_filter = ['name','desc','detail','degree','learn_times','students','favor','image','click_nums','add_time']
class LessonAdmin(object):
    list_display =['course','name','add_time']
    search_fields =['course','name']
    list_filter =['course__name','name','add_time']
class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter =['lesson', 'name', 'add_time']
class CourseResouceAdmin(object):
    list_display = ['name', 'course','download', 'add_time']
    search_fields = ['name', 'course','download']
    list_filter =['name', 'course','download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResouce, CourseResouceAdmin)