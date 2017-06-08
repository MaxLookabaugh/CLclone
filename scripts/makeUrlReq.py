#!/usr/bin/env python

import requests

def make_url_request(url,rtype):
    '''
    Generic URL request function
    '''
    if rtype == 'GET':
        response = requests.get(url)
	print(response.text) 
    elif rtype == 'POST':
        response = requests.post(url) 
	print(response.text)


url = input("enter url: ")
rtype = input("enter rtype: ")

make_url_request(url,rtype)

print("about to request")
req1=requests.post('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/topology')	
