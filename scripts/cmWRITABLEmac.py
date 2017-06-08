#!/usr/bin/env python3
import requests
import time
import json

from TestLibFunctions import mac_format
from TestLibFunctions import make_url_request




req=requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms')
ccap = "10.10.10.10"
attr = req.json()
chUrl = "http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/FC528D5E8802/cmDsOfdmChanTable"

MAC = attr['json_data']
for item in MAC:

	print (" ")
	L1 = item
	#print(L1)
	newMac = mac_format(L1)
	print(newMac)
	chUrl = "http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/%s/cmDsOfdmRxMerTable"%(newMac)
	#print ("chUrl is: ", chUrl)
	resp = make_url_request(chUrl, None, None, "GET")
	
	json_str = json.dumps(resp)
	newResp = json.loads(json_str)
	#print ("DATA IS: ",newResp['ccaps']['10.10.10.10']['cms'][newMac]['data'])
	pnmData = newResp["ccaps"]['10.10.10.10']['cms'][newMac]['data']["cmDsOfdmRxMerTable"]	
	
	'''
	try for loop with looping time stamps
	'''
	measured_values = ["docsPnmCmDsOfdmRxMerMean","docsPnmCmDsOfdmRxMerThrVal","docsPnmCmDsOfdmRxMerStdDev"]
	my_dict = pnmData
	print ("measured value is: ",measured_values[1])
	#print (my_dict)
	val_count = 0
	ts_keys = my_dict.keys()
	for t in sorted(ts_keys):
		#replace here if neccesarry
		for list in my_dict[t]:
			count = 0
			for x in (list):	
				#print(x)
				#print ("measured value is: ",measured_values[val_count])
				if (count%3 == 1 and count%6 != 1):
					print ("gauge value for", measured_values[val_count],"is:", x)
					gauge_value = x
					'''
					if (gauge_value <= 100):
						print("gauge is less than 100")
					'''
				if(val_count < 3):
					#print("val_count is equal to", val_count)
					#print (measured_values[val_count])
					val_count+=1
				if (val_count >= 3):
					val_count = 0					
				count+=1
				
				'''
				if x == "GAUGE":
					#position = list.index("GAUGE")
					#position += 1
					print("")
					#print (list.index(position))
				'''	
		'''
		#This works also instead of list of lists
		for items in my_dict[t]:
			#t is the timestamp on each modem. ideally it will loop over the timestamp for every modem 
			#print(my_dict[t])
			for item in my_dict[t]:
				print ()
		'''	
		print (" ")
	



