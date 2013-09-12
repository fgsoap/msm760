#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2013 fgsoap
# All Rights Reserved.

import requests, time

real_ip="your_ip"

headers={
         'Referer':'https://real_ip/home.asp',
         'Host':'real_ip','User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36',
         }
login_data={
            'username':'admin',
            'pw':'admin'
            }
datas={
       #'Reset':#'Restart'
       }
macs={
       '10F-2':"00:24:A8:89:77:BC",
    

      }
s.post(url='https://real_ip/goform/Logout',verify=False,headers=headers,data=login_data)
for mac in macs:
    realmac=macs.get(mac)
    url='https://real_ip/centcfg/ap_overview_details.asp?entity=device&selector=%s&product=20' % realmac
    s.get(url,verify=False)
    s.get('https://real_ip/centcfg/maintenance.asp',verify=False)
    s.post('https://real_ip/goform/FormDeviceSystemRestart',verify=False,data=datas)
    print mac + " " + "has been restarted!"
    time.sleep(1)

