import json
macid=[]
#Function to check if macid is already present in array.
def checkmacid(file_mac):
	global macid
	n = -1
	for i in range (len(macid)):
		if macid[i] == file_mac:
			n = i
	return n
f=open("Non-Connected_Data_G2.txt","r")
while True:	
	content=f.readline()	
	if content:
		file_obj = json.loads(content)
		file_mac = file_obj["SensorUUID"]
	else: 
		break	#if no content
	n=checkmacid(file_mac)
	if n ==-1:
		macid.append(file_mac)
print(macid)
