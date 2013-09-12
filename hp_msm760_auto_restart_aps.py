#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2013 fgsoap
# All Rights Reserved.
try:
         import requests, time
except ImportError:
         print "Please make sure the requests is installed!"

# please change the "ip" into your real ip.
headers={
         'Referer':'https://"ip"/home.asp',
         'Host':"ip",'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36',
         }
login_data={
#Please change them.
            'username':'admin',
            'pw':'admin'
            }
datas={
       'Reset':'Restart'
       }
macs={
       'ap_name1':"00:24:A8:89:77:AC",
       'ap_name2':"00:24:A8:89:77:AB",
# you can add a lots of apps here      
      }
s.post(url='https://"ip"/goform/Logout',verify=False,headers=headers,data=login_data)
for mac in macs:
    realmac=macs.get(mac)
    url='https://"ip"/centcfg/ap_overview_details.asp?entity=device&selector=%s&product=20' % realmac
    s.get(url,verify=False)
    s.get('https://"ip"/centcfg/maintenance.asp',verify=False)
    s.post('https://"ip"/goform/FormDeviceSystemRestart',verify=False,data=datas)
    print mac + " " + "has been restarted!"
    time.sleep(1)

