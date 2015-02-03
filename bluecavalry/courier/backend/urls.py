#coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('backend.views',
	url(r'^login/$', 'login'),                # 登录
	url(r'^logout/$', 'logout'),              # 退出登录
	url(r'^sendList/$', 'sendList'),          # 寄件列表页面
	url(r'^receiveList/$', 'receiveList'),    # 收件列表页面
	url(r'^login_handle/$', 'login_handle'),  # 登录表单提交验证
)