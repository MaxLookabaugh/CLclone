#!/usr/bin/env python

import requests
import time
import json

def make_url_request(url,rtype):
    '''
    Generic URL request function
    '''
    if rtype == 'GET':
        response = requests.get(url).json()
	print (response)
	powerTable = response['ccaps']
	print (powerTable)
	#ccap= attr['']
        #print("ccap is: ",ccap)
	#print (response.text)
	'''
	with open('jsonTestStore.json', 'w') as outfile:
                json.dump(attr, outfile)
	'''
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
	pwrTableUrl = "http://10.10.10.50:4210/dccf/ccaps/%s/cms/%s/cmDsOfdmChannelPowerTable"%(CMTS,MAC)
	print (url)
	
	
	#make_url_request('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms','GET')
	#make_url_request(url, 'GET')
	make_url_request(pwrTableUrl, 'GET')
	#subprocess.call(['./test.sh'])
	time.sleep(1)
