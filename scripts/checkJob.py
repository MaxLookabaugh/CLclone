#!/usr/bin/env python

import requests
import json
import time
import sys

from TestLibFunctions import make_url_request
from TestLibFunctions import mac_format


def checkJobId(tftp_server, tftp_port, jobID):
	
	url = "http://%s:%s/dccf/jobs/%s"%(tftp_server, tftp_port, jobID)
	res = make_url_request(url, None, None, "GET")
	#print(res)
	for line in res:
		myJson = json.loads(line)
    		print(json.dumps(myJson,indent=2,sort_keys=True))

	'''
	jobStatus = requests.get("https://%s:%s/dccf/jobs/%s")%(tftp_server, tftp_port, jobID)
	json_status = jobStatus.json()
	print (json_status)
	'''

tftp_server = raw_input("enter tftp_server IP: ")
tftp_port = input("input tftp_server Port: ")
jobID = raw_input("input jobID: ")

checkJobId(tftp_server, tftp_port, jobID)




