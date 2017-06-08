curl -X GET http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/registered31cms | \
  python3 -c "import sys, json; print(json.load(sys.stdin)['json_data'])"
curl -X GET http://10.10.10.50:4210/dccf/ccaps/10.10.10.10/cms/0008B91854E3/cm
  #python3 -c "import sys, json; print(json.load(sys.stdin)['sysObjectID'])"

