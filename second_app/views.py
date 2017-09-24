# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Test
from json import dumps

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def hello(request):
    context = {
        "hello": u"捣蛋"
    }
    return render(request, "index.html", context)

def createRecord(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

@login_required
def json(request):
    context = {
        u"alias": u"捣蛋",
        "name": u"测试人员"
    }
    # return HttpResponse(dumps(context),content_type="application/json")
    return HttpResponse(dumps(context),content_type="application/json")
