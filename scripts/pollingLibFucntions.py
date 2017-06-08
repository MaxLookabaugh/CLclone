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

