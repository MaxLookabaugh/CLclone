#!/usr/bin/env python

import requests
import time
import subprocess

def make_url_request(url,rtype):
    '''
    Generic URL request function
    '''
    if rtype == 'GET':
        response = requests.get(url)
	#attr = response.json()
	#MAC = attr['json_data']
        #print(MAC)
	print (response.text)
    elif rtype == 'POST':
        response = requests.post(url)
        #attr=response.json()
	#MAC=attr['json_data']
	#print(MAC)
	print (response.text)

for i in range (0,3):
	make_url_request('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms','GET')
	time.sleep(5)
