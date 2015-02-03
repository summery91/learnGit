#coding: utf-8
from django.db import models

# ------------------------------
#  寄件人信息表 Send_user
#  name         : 寄件人姓名
#  phone        : 寄件人姓名
#  addr         : 取件地址
#  time         : 取件时间
#  send_addr    : 邮寄地址
#  description  : 备注
#  value_area   : 收件人地区
#  value_weight : 快件重量
#  value_price  : 价格预估
#  detatime     : 下单时间
#  end_flag     : 是否完结
# ------------------------------
class Send_user(models.Model):
	name         = models.CharField(max_length=20)
	phone        = models.CharField(max_length=20)
	addr         = models.CharField(max_length=100)
	time         = models.CharField(max_length=20)
	send_addr    = models.CharField(max_length=100)
	description  = models.CharField(max_length=140)
	value_area   = models.CharField(max_length=100)
	value_weight = models.CharField(max_length=20)
	value_price  = models.CharField(max_length=20)
	datetime     = models.DateTimeField(auto_now_add = True)
	end_flag     = models.BooleanField(default = False)

# ------------------------------
#  收件人信息表 Receive_user
#  name         : 收件人姓名
#  phone        : 收件人姓名
#  fetch_addr   : 取件地址
#  send_addr    : 送件地址
#  send_time    : 送件时间
#  description  : 备注
#  detatime     : 下单时间
#  end_flag     : 是否完结
# ------------------------------
class Receive_user(models.Model):
	name        = models.CharField(max_length=20)
	phone       = models.CharField(max_length=20)
	fetch_addr  = models.CharField(max_length=100)
	send_addr   = models.CharField(max_length=100)
	send_time   = models.CharField(max_length=20)
	description = models.CharField(max_length=140)
	datetime    = models.DateTimeField(auto_now_add = True)
	end_flag    = models.BooleanField(default = False)