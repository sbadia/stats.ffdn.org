#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
DB_URL = 'https://db.ffdn.org/api/v1/isp/?per_page=9999'
ffdn_isp = 0
ffdn_members = 0

for isp in requests.get(DB_URL).json()['isps']:
    if not isp['is_ffdn_member']:
        continue
    name = isp['ispformat']['name']
    members = isp['ispformat']['memberCount']
    subscribers = isp['ispformat']['subscriberCount'] or 0
    print("ISP: %s has %s members and %s subscribers") % \
        (name, members, subscribers)
    ffdn_isp += 1
    ffdn_members += members

print("Total: %s isp and %s members") % (ffdn_isp, ffdn_members)
