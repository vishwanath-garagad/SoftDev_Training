import json
macid=[]

def searchmacid():
	f=open("Non-Connected_Data_G2.txt","r")
	while True:	
		content=f.readline()	
		# print(content)
		if content:
			file_obj = json.loads(content)
			file_mac = file_obj["SensorUUID"]
		
		else:
			break	
		
		find = checkmacid(file_mac)
		if find == 0:
			macid.append(file_mac)
			print(macid)
		
			
	return macid

#To check macid
def checkmacid(file_mac):
	n = 0
	global macid
	for i in range (len(macid)):
		if macid[i] == file_mac:
			n = i
	return n
searchmacid()
checkmacid(file_mac)		

				

