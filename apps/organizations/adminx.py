
# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/4/7 18:50'

from .models import CityDict,Teacher,CourseOrg

import xadmin
class CityDictAdmin(object):
    list_display = ['name','desc','add_time']
    search_fields = ['name','desc']
    list_filter =['name','desc','add_time']
class CourseOrgAdmin(object):
    list_display = ['name','desc','clicK_nums','fav_nums','images','address','city','add_time']
    search_fields = ['name','desc','clicK_nums','fav_nums','images','address','city']
    list_filter = ['name','desc','clicK_nums','fav_nums','images','address','city','add_time']
class TeacherAdmin(object):
    list_display = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time']
    search_fields = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums']
    list_filter =  ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)

