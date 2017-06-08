#!/usr/bin/env python3
import requests
import time
import json

from TestLibFunctions import mac_format
from TestLibFunctions import make_url_request


def initializePoll(ccap, MAC, tftp_server, tftp_port):
	'''
	initializes polling for associated MAC address
	'''
	#CCAP API posts
	url = "http://%s:%s/dccf/ccaps/%s/initialize"%(tftp_server, tftp_port, ccap)
	make_url_request(url, None, None, "POST")
	url = "http://%s:%s/dccf/ccaps/%s/cmPNMDsRxMerAll"%(tftp_server, tftp_port, ccap)
	make_url_request(url, None, None, "POST")
	url = "http://%s:%s/dccf/ccaps/%s/registered31cms"%(tftp_server, tftp_port, ccap)
	make_url_request(url, None, None, "POST")
	url = "http://%s:%s/dccf/ccaps/%s/system"%(tftp_server, tftp_port, ccap)
	make_url_request(url, None, None, "POST")
	url = "http://%s:%s/dccf/ccaps/%s/topology"%(tftp_server, tftp_port, ccap)
	make_url_request(url, None, None, "POST")
	
	
	#CCAP, CMAC posts
	url = "http://%s:%s/dccf/ccaps/%s/cms/%s/cmDeltaDsFecStats"%(tftp_server, tftp_port, ccap, MAC)
	make_url_request(url, None, None, "POST")
	url = "http://%s:%s/dccf/ccaps/%s/cms/%s/cmDsFecStats"%(tftp_server, tftp_port, ccap, MAC)
	make_url_request(url, None, None, "POST")
	url = "http://%s:%s/dccf/ccaps/%s/cms/%s/cmDsOfdmChanTable"%(tftp_server, tftp_port, ccap, MAC)
	make_url_request(url, None, None, "POST")
	url = "http://%s:%s/dccf/ccaps/%s/cms/%s/cmDsOfdmChannelPowerTable"%(tftp_server, tftp_port, ccap,MAC)
	make_url_request(url, None, None, "POST")
	url = "http://%s:%s/dccf/ccaps/%s/cms/%s/cmDsOfdmRxMerTable"%(tftp_server, tftp_port, ccap, MAC)
	make_url_request(url, None, None, "POST")
	url = "http://%s:%s/dccf/ccaps/%s/cms/%s/cmPNMDsRxMer"%(tftp_server, tftp_port, ccap, MAC)
	make_url_request(url, None, None, "POST")
	print("finished url post requests for MAC: ", MAC)

req=requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms')
ccap = input("enter CMTS IP: ")
tftp_server = input("enter tftp_server IP: ")
tftp_port = input ("enter tftp port: ")
attr = req.json()
MAC = attr['json_data']
for item in MAC:

	L1 = item
	newMac = mac_format(L1)
	#chUrl = "http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/%s/cm"%(newMac)
	#print ("chUrl is: ", chUrl)
	#resp = make_url_request(chUrl, None, None, "GET")
	#print (resp)
	initializePoll(ccap, newMac, tftp_server,tftp_port)
	'''
	json_str = json.dumps(resp)
	newResp = json.loads(json_str)
	print ("newResp is: ", newResp)
	print ("DATA IS: ",newResp['ccaps']['10.10.10.10']['cms'][newMac]['data']['cmDsOfdmRxMerTable']['20170531215439Z'])
	'''
	#print(type(L1))
	#chan = requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/0008B91854E3/CmDsOfdmChanTable')
	#getCmDsOfdmChanTable(item, ccap)


