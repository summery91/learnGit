#coding: utf-8
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# return HttpResponse("0")

# ======================================
#   功能：管理员登录界面
#   人员：黄晓佳
#   日期：2014.10.10
# --------------------------------------
def login(request):
	return render(request, "login.html")

# ======================================
#   功能：登录表单提交验证
#   人员：黄晓佳
#   日期：2014.10.11
# --------------------------------------
@csrf_exempt
def login_handle(request):
	# 登录错误用户提示
	login_error = False

	# 请求方法判断
	if request.method != 'POST':
		login_error = u'请求方法不合法，请重试'
		return render(request, "login.html", {'login_error':login_error})

	# 验证账号
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)

	# 如果验证失败
	if user is None:
		login_error = u'账号或密码错误，请重试'
		return render(request, "login.html", {'login_error':login_error})

	# 验证成功
	auth_login(request, user)
	return HttpResponseRedirect("/backend/sendList/")

# ======================================
#   功能：退出登录
#   人员：黄晓佳
#   日期：2014.10.11
# --------------------------------------
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect("/backend/login/")

# ======================================
#   功能：寄件列表页面
#   人员：黄晓佳
#   日期：2014.10.11
# --------------------------------------
def sendList(request):
	# 若没登录
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/backend/login/")

	return render(request, "index.html", {'title': "寄件"})

# ======================================
#   功能：收件列表页面
#   人员：黄晓佳
#   日期：2014.10.11
# --------------------------------------
def receiveList(request):
	# 若没登录
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/backend/login/")

	return render(request, "index.html", {'title': "收件"})

# ======================================
#   功能：修改密码表单提交验证
#   人员：黄晓佳
#   日期：2014.10.11
# --------------------------------------
def changePwd_handle(request):
	return HttpResponse("0")
