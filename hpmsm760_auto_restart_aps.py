#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2013 fgsoap
# All Rights Reserved.
# In Python 2.7.5
try:
         import requests, time
         from pyquery import PyQuery as pq
except ImportError:
         print "Please make sure the Requests and the PyQuery are installed!"

# Please change the "ip" into your real ip.
ip = ''
sysadmin = ''
password = ''
headers={
         'Referer':'https://%s/home.asp'%ip,
         'Host':ip,'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36',
         }
login_data={
# Please change them.
            'username':sysadmin,
            'pw':password'
            }
datas={
       'Reset':'Restart'
       }
# Login
s=requests.Session()
s.post(url='https://%s/goform/Logout'%ip,verify=False,headers=headers,data=login_data)

# Get the dictionaries of all the aps.
n=s.get('https://%s/centcfg/ap_overview.asp?entity=vgroup&selector=Synchronized'%ip,verify=False)
html=pq(n.text)
ap_name=[]
ap_mac=[]
i_a=html("li div a")
i_span=html("li div a span")
for i in xrange(len(i_a)):
    ap_name.append(i_span.eq(i).text())
    ap_mac.append(i_a.eq(i).attr("href").strip("&amp;product=20").strip("centcfg/ap_overview_details.asp?entity=device&selector=").replace("%3A", ":"))

aps=dict(zip(ap_name,ap_mac))

#Let's restart all the aps!
for mac in aps:
    realmac=aps.get(mac)
    url='https://%s/centcfg/ap_overview_details.asp?entity=device&selector=%s&product=20'%ip % realmac
    s.get(url,verify=False)
    s.get('https://%s/centcfg/maintenance.asp'%ip,verify=False)
    s.post('https://%s/goform/FormDeviceSystemRestart'%ip,verify=False,data=datas)
    print mac + " " + "has been restarted!"
    time.sleep(1)

