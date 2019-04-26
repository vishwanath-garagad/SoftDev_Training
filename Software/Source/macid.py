import json
def writefile():
	macid=input("Enter the macid ")
	myfile=open("Non-Connected_Data_G2.txt","r")
	
	while True:
		content=myfile.readline()
		# print(content)
	
		file_obj = json.loads(content)
		file_mac=file_obj["SensorUUID"]
		if file_mac == macid:
			file = open(str(file_mac)+".txt","a")
			py_obj = json.dumps(file_obj)
			file.write(py_obj+"\n")
			file.close()
		else:
			break
writefile()
