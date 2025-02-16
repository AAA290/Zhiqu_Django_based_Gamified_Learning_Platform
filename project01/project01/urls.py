"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from TestModel import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("visualization/", views.visual_everyday_tasks),   #当访问www.xxx.com/visualization时执行views中的visual函数

    path("visualization/todo_list/",views.visual_todo_lists),

    path("visualization/ability/",views.visual_ability),

    path("visualization/displaytree/",views.visual_displaytree),

    path("visualization/linechart/",views.visual_linechart),

    path("visualization/pinechart/",views.visual_pinechart),

    path("equipment/",views.equip),

    path("npc/",views.npc_dialog),

    path("dialog/",views.npc_dialog),

    path('infochange/', views.infochange, name='infochange'),   ##尝试表单

    path("home/",views.visual_home),

    path("login/",views.visual_login),

    path("login_form/",views.login_form),

    path("register/",views.register),

    path("npcchoice/<int:id>/",views.npc_choice),

    path('buy_item/<int:item_id>/', views.buy_item),

    path("newtasks/",views.newtasks),

    path("newtodos/",views.newtodos),

    path("jiangli/",views.jiangli)

]
