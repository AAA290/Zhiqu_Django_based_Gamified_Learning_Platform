from django.contrib import admin
from TestModel.models import UserInfo,TaskInfo,DateTodoInfo,DateCheckInfo,EquipmentInfo,TodoInfo

# Register your models here.
admin.site.site_header = '游戏后台管理页面'

class UserInfoAdmin(admin.ModelAdmin):
    filter_horizontal = ('equipements','tasks','todos')
    # 指定后台网页要显示的字段
    list_display = ("id","name", "rank")
    actions_on_bottom=True #底部显示删除动作选项
    actions_on_top=False #删除头部动作选项
    list_display_links = ('name',)
    list_per_page = 10   # 指定每页显示10条数据
    list_filter = ['rank']
    search_fields = ['id']
admin.site.register(UserInfo, UserInfoAdmin)

class TaskInfoAdmin(admin.ModelAdmin):
    # 指定后台网页要显示的字段
    list_display = ("id","name", "begin","end")
    actions_on_bottom=True #底部显示删除动作选项
    actions_on_top=False #删除头部动作选项
    list_display_links = ('name',)
    list_per_page = 10   # 指定每页显示10条数据
    search_fields = ['name']
admin.site.register(TaskInfo, TaskInfoAdmin)

class TodoInfoAdmin(admin.ModelAdmin):
    list_display = ("id","name", "date","state")
    actions_on_bottom=True #底部显示删除动作选项
    actions_on_top=False #删除头部动作选项
    list_display_links = ('name',)
    list_per_page = 10   # 指定每页显示10条数据
    search_fields = ['name','state','date']
admin.site.register(TodoInfo, TodoInfoAdmin)

class DateTodoInfoAdmin(admin.ModelAdmin):
    filter_horizontal = ('tasks_todo','todos')
    # 指定后台网页要显示的字段
    list_display = ("id","date")
    actions_on_bottom=True #底部显示删除动作选项
    actions_on_top=False #删除头部动作选项
    list_display_links = ('id','date',)
    list_per_page = 10   # 指定每页显示10条数据
    search_fields = ['date']
admin.site.register(DateTodoInfo, DateTodoInfoAdmin)

class DateCheckInfoAdmin(admin.ModelAdmin):
    filter_horizontal = ('tasks_done',)
    # 指定后台网页要显示的字段
    list_display = ("id","date")
    actions_on_bottom=True #底部显示删除动作选项
    actions_on_top=False #删除头部动作选项
    list_display_links = ('id','date',)
    list_per_page = 10   # 指定每页显示10条数据
    search_fields = ['date']
admin.site.register(DateCheckInfo, DateCheckInfoAdmin)

class EquipmentInfoAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    actions_on_bottom=True #底部显示删除动作选项
    actions_on_top=False #删除头部动作选项
    list_display_links = ('id','name',)
    list_per_page = 10   # 指定每页显示10条数据
    search_fields = ['name']
admin.site.register(EquipmentInfo, EquipmentInfoAdmin)