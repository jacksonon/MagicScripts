#!/usr/bin/python
# coding: UTF-8
# python2 xxx.py
import webbrowser as web
import time
import os
import random
data = raw_input('请输入网址：')
count = random.randint (3,5)
j = 0
while j <count:
  i = 0
  while i <= 3:
    web.open_new_tab(data)
  i=i+1
  time.sleep(0.8)
else:
  os.system('taskkill /F /IM chrome.exe')
  print j, 'times closing Browser !'
  j = j+1%  
