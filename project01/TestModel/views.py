import json

from django.shortcuts import render,HttpResponse,redirect
from TestModel import models
from django.utils import timezone
from datetime import timedelta
import requests
from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
# RunOnce=True
# Create your views here.

# Create your views here.

def login_form(request):
    if request.method == 'POST':
        name = request.POST.get('account')
        password = request.POST.get('password')
        obj = models.UserInfo.objects.get(name=name,password=password)
        request.session['userid'] = obj.id  # 将用户对象保存到会话中
        datecheck = models.DateCheckInfo.objects.all()
        undo = obj.todos.filter(state=0)
    return render(request,"home.html",{"user":obj,"checkall":datecheck,"undo":undo})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        obj = models.UserInfo.objects.create(name=name,password=password)
        request.session['userid'] = obj.id  # 将用户对象保存到会话中
        # print(obj.name,obj.password)
        # print(request.session.get('userid'),type(request.session.get('userid')))
    return render(request,"home.html",{"user":obj})

def visual_home(request):   ##根据app的注册顺序,在每个app下的templates目录中寻找
    # obj = models.UserInfo.objects.filter(name="Unkown1").first()
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    datecheck = models.DateCheckInfo.objects.all()
    undo = obj.todos.filter(state=0)
    return render(request,"home.html",{"user":obj,"checkall":datecheck,"undo":undo})

def visual_login(request):   ##根据app的注册顺序,在每个app下的templates目录中寻找
    # obj = models.UserInfo.objects.filter(name="Unkown1").first()
    return render(request,"index.html")

def create_date_todo_info(task_info):
    begin = task_info.begin
    end = task_info.end
    fre = task_info.frequency
    for i in range(0,(end - begin).days + 1,fre):# 日期为begin到end的隔开fre
        date = begin + timedelta(days=i)
        datetodo = models.DateTodoInfo.objects.create(date=date)
        datetodo.tasks_todo.add(task_info)

def visual_everyday_tasks(request):   ##根据app的注册顺序,在每个app下的templates目录中寻找
    # if(RunOnce):
    #     obj=models.UserInfo.objects.create(name="Unkown1",password="123456",rank=3,blood=70,experience=80)
    #     task1=models.TaskInfo.objects.create(name="每日签到",type=0,begin=timezone.now().date(),end= timezone.now().date() + timedelta(days=5*365),frequency=1)
    #     obj.tasks.add(task1)
    #     create_date_todo_info(task1)
    #     Run_Once=False

    # task=models.TaskInfo.objects.get(name="每日签到")
    # # 获取所有的DateTodoInfo实例
    # date_todo_instances = models.DateTodoInfo.objects.all()
    #
    # # 遍历所有的DateTodoInfo实例，并将TaskInfo实例添加到tasks_todo字段中
    # for date_todo_instance in date_todo_instances:
    #     date_todo_instance.tasks_todo.add(task)
    #     date_todo_instance.save()

    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    datecheck = models.DateCheckInfo.objects.all()
    return render(request,"page.html",{"user":obj,"checkall":datecheck})

def visual_todo_lists(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    datecheck = models.DateCheckInfo.objects.all()
    return render(request,"todo.html",{"user":obj,"checkall":datecheck})

def visual_ability(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    return render(request,"ability.html",{"user":obj})

def visual_displaytree(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    return render(request,"displaytree.html",{"user":obj})

def visual_linechart(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    # datetodo = models.DateTodoInfo.objects.all()
    timearray,count=[],[]
    i=0
    for datetodo in models.DateTodoInfo.objects.all():
        flag=False
        temp=0
        for task in datetodo.tasks_todo.all():
            if task in obj.tasks.all():
                if not flag:
                    flag=True
                    timearray.append(datetodo.date.strftime("%Y-%m-%d"))
                temp+=1
        for todo in datetodo.todos.all():
            if todo in obj.todos.all():
                if not flag:
                    flag=True
                    timearray.append(datetodo.date.strftime("%Y-%m-%d"))
                temp+=1
        if flag:
            i+=1
            count.append(temp)
    # print(timearray)
    # print(count)
    # print(len(timearray),len(count))
    return render(request,"linechart.html",{"user":obj,"timearray":timearray,"count":count})

def visual_pinechart(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    todo_count = models.TodoInfo.objects.filter(state=0).count()
    done_count = models.TodoInfo.objects.filter(state=1).count()
    outofdate_count = models.TodoInfo.objects.filter(state=2).count()
    return render(request,"pinechart.html",{"user":obj,"done":done_count,"todo":todo_count,"outofdate":outofdate_count})

def infochange(request):  ##表单示例，例子在ability.html中被注释了
    if request.method == 'POST':  # 检查是否是 POST 请求
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        obj_id = request.session.get('userid')
        obj = models.UserInfo.objects.get(id=obj_id)
        obj.name=uname
        obj.password=password
        obj.save()
        print("修改成功：",uname,password)
        return redirect(request.META['HTTP_REFERER'])  # 返回原页面
    else:
        return redirect(request.META['HTTP_REFERER'])  # 返回原页面

def equip(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    eq = models.EquipmentInfo.objects.all()
    return render(request, "equipment.html", {"user":obj, "eq":eq})

def npc_choice(request,id):
    character=["workspaces/default-zrjlsgmbnfz8scasvt4kbq/characters/feilen",
               "workspaces/default-zrjlsgmbnfz8scasvt4kbq/characters/frieren",
               "workspaces/default-zrjlsgmbnfz8scasvt4kbq/characters/himmel",
               "workspaces/default-zrjlsgmbnfz8scasvt4kbq/characters/stark"
              ]
    character_name=["Feilen","Frieren","Himmel","Stark"]
    request.session['npc_id'] = id
    request.session['npc'] = character[id]
    request.session['npc_name'] = character_name[id]
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    character=request.session.get('npc')
    KEY2="RDBKUXdYbzVPRldQTHpRRWRwNHV2eG05UlZreWJFbVk6VUVRQzNQMWdhdHE3dUdpVGxjUmZ2TWNhZ0VjbnY5SHBJMDNzUVVsQmVqeFI2Vzk1WDNiZFNDV1g1RzdKdWtEag=="
    url = f'https://studio.inworld.ai/v1/{character}:simpleSendText'
    headers = {"Content-Type": "application/json", "authorization": "Basic "+KEY2}
    textList=[]
    text=""
    reply=""
    if request.method == 'POST':  # 检查是否是 POST 请求
        text = request.POST.get('text')
        # print(text)
        myobj = {"character":character, "text":text, "endUserFullname":obj.name, "endUserId":str(obj.id)}

        x = requests.post(url, json = myobj, headers=headers)
        textList=x.json()['textList']
        # print(textList)
        reply=' '.join(textList)
    return render(request, "npc.html", {"user":obj, "reply":reply, "text":text,"npc_id":request.session.get('npc_id'),"npc_name":character_name[id]})

def npc_dialog(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    character=request.session.get('npc')
    KEY2="RDBKUXdYbzVPRldQTHpRRWRwNHV2eG05UlZreWJFbVk6VUVRQzNQMWdhdHE3dUdpVGxjUmZ2TWNhZ0VjbnY5SHBJMDNzUVVsQmVqeFI2Vzk1WDNiZFNDV1g1RzdKdWtEag=="
    url = f'https://studio.inworld.ai/v1/{character}:simpleSendText'
    headers = {"Content-Type": "application/json", "authorization": "Basic "+KEY2}
    textList=[]
    text=""
    reply=""
    if request.method == 'POST':  # 检查是否是 POST 请求
        text = request.POST.get('text')
        # print(text)
        myobj = {"character":character, "text":text, "endUserFullname":obj.name, "endUserId":str(obj.id)}

        x = requests.post(url, json = myobj, headers=headers)
        textList=x.json()['textList']
        # print(textList)
        reply=' '.join(textList)
    return render(request, "npc.html", {"user":obj, "reply":reply, "text":text,"npc_id":request.session.get('npc_id'),"npc_name":request.session.get('npc_name')})

def buy_item(request, item_id):
    item = models.EquipmentInfo.objects.get(id=item_id)
    print(item.name)
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    money=obj.money
    if money >= item.value:
        now = money-item.value
        obj.money=now
        obj.equipements.add(item)
        obj.save()
        return HttpResponse('金币充足，购买成功!')
    else:
        return HttpResponse('金币不足，购买失败!')

def newtasks(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        begin = request.POST.get('begin')
        end = request.POST.get('end')
        obj.tasks.create(name=name,begin=begin,end=end)
    return render(request,"home.html",{"user":obj})

def newtodos(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        obj.todos.create(name=name,date=date,state=0)
    return render(request,"home.html",{"user":obj})

def jiangli(request):
    obj_id = request.session.get('userid')
    obj = models.UserInfo.objects.get(id=obj_id)
    money=obj.money
    ex=obj.experience
    if request.method == 'POST':
        jl = json.loads(request.body.decode('utf-8'))['jl']
        rN = json.loads(request.body.decode('utf-8'))['rN']
        # print(jl,rN)
        if jl==0:
            money+=rN
            obj.money=money
            obj.save()
        else:
            ex+=rN
            obj.experience=ex
            obj.save()
        taskid = json.loads(request.body.decode('utf-8'))['task_id']
        if(taskid!=0):
            task=models.TaskInfo.objects.get(id=taskid)
            models.DateCheckInfo.objects.get_or_create(date=timezone.now().date())
            today=models.DateCheckInfo.objects.get(date=timezone.now().date())
            today.tasks_done.add(task)
        todoid=json.loads(request.body.decode('utf-8'))['todo_id']
        if(todoid!=0):
            todo=models.TodoInfo.objects.get(id=todoid)
            todo.state=1
            todo.save()
        return redirect(request.META['HTTP_REFERER'])  # 返回原页面
    return redirect(request.META['HTTP_REFERER'])  # 返回原页面