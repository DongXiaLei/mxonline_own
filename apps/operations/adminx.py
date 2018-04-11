# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/4/7 19:07'

from  .models import UserAsk,UserFavorite,UserMessage,UserCourse,CourseComments

import xadmin

class UserAskAdmin(object):
    list_display = ['name','mobile','course_name','add_time']
    search_fields =  ['name','mobile','course_name']
    list_filter = ['name','mobile','course_name','add_time']

class UserFavoriteAdmin(object):
    list_display = ['user','fav_type','fav_id','add_time']
    search_fields =['user','fav_type','fav_id']
    list_filter =['user','fav_type','fav_id','add_time']

class UserMessageAdmin(object):
    list_display = ['user','message','has_read','add_time']
    search_fields = ['user','message','has_read']
    list_filter =['user','message','has_read','add_time']

class UserCourseAdmin(object):
    list_display =['user','course','add_time']
    search_fields = ['user','course']
    list_filter =['user','course','add_time']

class CourseCommentsAdmin(object):
    list_display = ['user','course']
    search_fields = ['user','course']
    list_filter =['user','course']


xadmin.site.register(UserAsk)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)




