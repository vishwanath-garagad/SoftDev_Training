import json

def readfile():
	myfile=open("Non-Connected_Data_G2.txt","r")
	while(1):
		content=myfile.readline()
	#print(content)
		if content:
			file_obj = json.loads(content)
			file_mac=file_obj["SensorUUID"]
			print(file_obj)
			print(file_mac)
		else:
			break

	
readfile()
	