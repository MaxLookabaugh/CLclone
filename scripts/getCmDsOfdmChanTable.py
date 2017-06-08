#!/usr/bin/env python3

import requests
from requests import Response

#ccap = input("Enter ccap IP: ")
#cmMac = input ("Enter CM MAC: ")





req = requests.get('http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/0008B91854E3/cmDsOfdmChanTable')
print (req.text)

