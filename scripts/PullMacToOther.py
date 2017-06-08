#!/usr/bin/env python

import requests
import time
import subprocess
import netaddr
import json

TestMac = ""

def get_mac_list(url, rtype):
    #function to store all registered CMs in dictionary
    if rtype == 'GET':
        response = requests.get(url)
	attr = response.json()
	MacList=attr["json_data"]
	#need to put into dictionary
	print("MacList is: ", MacList)
	with open('macList.csv', 'w') as outfile:
		json.dump(MacList, outfile)
	#TestMac = MacAddr
	#print("TestMac is: ", TestMac)
	return TestMac

def make_url_request(url,rtype):
    '''
    Generic URL request function
    '''
    if rtype == 'GET':
        response = requests.get(url)
	attr = response.json()
	print (attr)
	#ccap= attr['']
        #print("ccap is: ",ccap)
	#print (response.text)
    elif rtype == 'POST':
        response = requests.post(url)
        #attr=response.json()
	ccap=attr['20170531215439Z']
	print("ccap is ",ccap)
	print (response.text)


for i in range (0,3):

	CMTS = '10.10.10.10'
	MAC = "0008B91854E3"
	url = "http://10.10.10.50:4210/dccf/ccaps/%s/registered31cms" %(CMTS)
	CmUrl = "http://10.10.10.50:4210/dccf/ccaps/%s/cms/%s/cmDsOfdmRxMerTable"%(CMTS,MAC)
	print (url)
#	make_url_request('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms','GET')
	#make_url_request(url, 'GET')
#	make_url_request(url, 'GET')
#	time.sleep(1)
TestMac = get_mac_list(url,'GET')
#make_url_request(CmUrl, 'GET')

