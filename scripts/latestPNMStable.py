#!/usr/bin/env python3
import requests
import time
import json

from TestLibFunctions import mac_format
from TestLibFunctions import make_url_request
from pollingLibFucntions import initializePoll


polled = "false"




def pnmTable():
	req=requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms')
	ccap = "10.10.10.10"
	attr = req.json()
	chUrl = "http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/FC528D5E8802/cmDsOfdmChanTable"


	MAC = attr['json_data']
	for item in MAC:
	
		#hardcoding host IP, 
		initializePoll("10.10.10.10",item,"10.10.10.50","4210")
		
		print (" ")
		L1 = item
		#print(L1)
		newMac = mac_format(L1)
		print(newMac)
		Url = "http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/%s/cmDsOfdmRxMerTable"%(newMac)
		#print ("Url is: ", Url)
		resp = make_url_request(Url, None, None, "GET")
	
		json_str = json.dumps(resp)
		newResp = json.loads(json_str)
		#print ("DATA IS: ",newResp['ccaps']['10.10.10.10']['cms'][newMac]['data'])
		pnmData = newResp["ccaps"]['10.10.10.10']['cms'][newMac]['data']["cmDsOfdmRxMerTable"]	
	
	
	
		measured_values = ["docsPnmCmDsOfdmRxMerMean","docsPnmCmDsOfdmRxMerThrVal","docsPnmCmDsOfdmRxMerStdDev"]
		my_dict = pnmData
		#print (my_dict)
		val_count = 0
		ts_keys = my_dict.keys()
		for t in sorted(ts_keys):
			#replace here if neccesarry
			for list in my_dict[t]:
				count = 0
				for x in (list):	
					#print(x)
					#drags for most recent value
					if (x == "docsPnmCmDsOfdmRxMerMean"):	
						current_val = "docsPnmCmDsOfdmRxMerMean"
					#	print (current_val)
					if (x == "docsPnmCmDsOfdmRxMerThrVal"):
						current_val = "docsPnmCmDsOfdmRxMerThrVal"
					#	print (current_val)
					if (x == "docsPnmCmDsOfdmRxMerStdDev"):
						current_val = "docsPnmCmDsOfdmRxMerStdDev"
					#	print(current_val)
				
					#checks gauge for most recent value
					if (count%3 == 1 and count%6 != 1):
						#print("val is: ", x)
						#need the acceptable values for mean thermal val and std Dev
						if (current_val == "docsPnmCmDsOfdmRxMerMean" and (x < 150 and x > 0)):
							print(current_val,"is ", x)	
						elif (current_val == "docsPnmCmDsOfdmRxMerThrVal" and (x < 150 and x > 0)):
							print(current_val,"is ", x)
						elif (current_val == "docsPnmCmDsOfdmRxMerStdDev" and (x < 150 and x > 0)):
							print(current_val,"is ", x)
							
					count+=1
		 
		
			print (" ")
	
pnmTable()
'''
while("true"):
	pnmTable()
	print ("exit if neccesarry...")
	time.sleep(5)
'''
