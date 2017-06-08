#!/usr/bin/env python
import requests
import netaddr

print("enter quit at any time to exit program")

def cmPNMDsRxMerAllPOST():
        req = requests.post('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cmPNMDsRxMerAll')
        print (req.text)

def cmPNMDsRxMerAllGET():
	req = requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cmPNMDsRxMerAll')
        print (req.text)

def initialize(): 
	req = requests.post('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/initialize')
        print (req.text)


def registered31cmsPOST():
	req = requests.post('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms')
        print (req.text)

def registered31cmsGET():
        req = requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms')
        print (req.text)

def systemPOST():
        req = requests.post('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/system')
        print (req.text)

def systemGET():
        req = requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/system')
        print (req.text)

def topologyPOST():
        req = requests.post('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/topology')
        print (req.text)

def topologyGET():
        req = requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/topology')
        print (req.text)


while True:
	switch = input ("input which ccap API call to test: ")

	if switch == 1:
		cmPNMDsRxMerAllPOST()

	if switch == 2:
		cmPNMDsRxMerAllGET()

	if switch == 3:
                initialize()
	
	if switch == 4:
		registered31cmsPOST()

	if switch == 5:
		registered31cmsGET()

	if switch == 6:
		systemPOST()

	if switch == 7:
		systemGET()

	if switch == 8:
		topologyPOST()

	if switch == 9:
		topologyGET()

	if switch == quit or  switch == exit:
		print ("exiting...")
		break





