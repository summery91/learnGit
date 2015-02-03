#coding: utf-8
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context,Template,RequestContext

# ======================================
# 	名字：前台手机界面
#   功能：收件和发件
#   人员：梁银乔
#   日期：2014.10.10
# --------------------------------------
def send(request, template_name):
	return render(request, template_name)

def receive(request, template_name):
	return render(request, template_name)