from django.db import models
from django.utils import timezone

# Create your models here.
class TaskInfo(models.Model):
    name = models.CharField('任务名称',max_length = 30)
    # type = models.IntegerField('任务类型')   #0习惯 1待办
    begin = models.DateField('开始日期',default=timezone.now().date())
    end = models.DateField('结束日期')
    frequency = models.IntegerField('频率',default=1)
    def __str__(self):
        # 自定义字符串表示形式
        return self.name

class TodoInfo(models.Model):
    name = models.CharField('待办事项名称',max_length = 30)
    date = models.DateField('开始日期',default=timezone.now().date())
    state = models.IntegerField('完成情况')  #0未完成 1已完成 2已过期
    def __str__(self):
        # 自定义字符串表示形式
        return self.name

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# @receiver(post_save, sender=TodoInfo)
# def update_state(sender, instance, **kwargs):
#     if instance.date > timezone.now().date():
#         instance.state = 2  # 设置为已过期
#         instance.save()
#是一个很好的方法，可以自动把过期的待办设置成过期状态，但是会导致
# RecursionError at /admin/TestModel/todoinfo/add/
# maximum recursion depth exceeded while calling a Python object
# 所以就没有用了

class EquipmentInfo(models.Model):
    name = models.CharField('装备名称',max_length=255)
    description = models.TextField('描述')
    type = models.IntegerField('类型')   #类型：武器1，防具2，饰品3，道具4
    level = models.IntegerField('等级')  #等级：根据属性值规定等级3
    attack_power = models.IntegerField('攻击值')
    defense_power = models.IntegerField('防御值')
    value = models.IntegerField('价值',default=20)
    def __str__(self):
        # 自定义字符串表示形式
        return self.name

class UserInfo(models.Model):
    name = models.CharField('名称',max_length = 30)
    password = models.CharField('密码', max_length = 20)
    rank = models.IntegerField('等级',default=1)
    experience = models.IntegerField('经验值',default=0)
    attack_power = models.IntegerField('攻击值',default=0)
    defense_power = models.IntegerField('防御值',default=0)
    blood = models.IntegerField('血量',default=100)
    money = models.IntegerField('金币',default=0)
    equipements = models.ManyToManyField(EquipmentInfo,'设备',blank=True)
    tasks = models.ManyToManyField(TaskInfo,'任务',blank=True)
    todos = models.ManyToManyField(TodoInfo,'待办',blank=True)
    def __str__(self):
        # 自定义字符串表示形式
        return self.name

class DateTodoInfo(models.Model):
    date = models.DateField('日期',unique=True)
    tasks_todo = models.ManyToManyField(TaskInfo,'每日任务',blank=True)
    todos = models.ManyToManyField(TodoInfo,'待办事项',blank=True)
    def __str__(self):
        # 自定义字符串表示形式
        return str(self.date)

class DateCheckInfo(models.Model):
    date = models.DateField('日期',unique=True)
    tasks_done = models.ManyToManyField(TaskInfo,'已经打卡的任务')
    def __str__(self):
        # 自定义字符串表示形式
        return str(self.date)


