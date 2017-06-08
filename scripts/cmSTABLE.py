#!/usr/bin/env python3
import requests
import time
import json

from TestLibFunctions import mac_format
from TestLibFunctions import make_url_request

def getCmDsOfdmChanTable(MAC, CMTS):
	chanTblReq = requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/FC528D5E8802/cmDsOfdmChanTable')
	attr = chanTblReq.json()
	print(attr)
	time.sleep(3)





req=requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms')
ccap = "10.10.10.10"
#prints json response
#print (req.text)
attr = req.json()
chUrl = "http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/FC528D5E8802/cmDsOfdmChanTable"
'''
print (req.status_code)
print the modem MAC address
print (attr['json_data'])
MAC = attr['json_data']
print (attr['json_data'])
'''
MAC = attr['json_data']
for item in MAC:

	L1 = item
	#print(L1)
	newMac = mac_format(L1)
	print(newMac)
	#chUrl = "http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/%s/cmDsOfdmRxMerTable"%(newMac)
	chUrl = "http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/%s/cmDsOfdmRxMerTable"%(newMac)
	print ("chUrl is: ", chUrl)
	resp = make_url_request(chUrl, None, None, "GET")
	print (resp)

	'''
	json_str = json.dumps(resp)
	newResp = json.loads(json_str)
	print ("newResp is: ", newResp)
	print ("DATA IS: ",newResp['ccaps']['10.10.10.10']['cms'][newMac]['data']['cmDsOfdmRxMerTable']['20170531215439Z'])
	'''
	#print(type(L1))
	#chan = requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/0008B91854E3/CmDsOfdmChanTable')
	#getCmDsOfdmChanTable(item, ccap)


