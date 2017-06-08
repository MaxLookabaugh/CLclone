#!/usr/bin/env python3
import requests

MAC= " "

req=requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms')

#prints json response
#print (req.text)
attr = req.json()
#print (req.status_code)
#print the modem MAC address
#print (attr['json_data'])
#MAC = attr['json_data']
print (attr['json_data'])
MAC = attr['json_data']
'''
x = 0
while x < len(MAC):
	if MAC ! == '8':
		MAC = MAC.replace(x,"!")
	x+=1
print ("Mac is: ",MAC)

'''
if attr["json_data"] == ['0008B91854E3']:
        print ("true")

