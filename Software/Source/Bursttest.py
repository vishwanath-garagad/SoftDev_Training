import csv
import json

Dbg_Pkt=0
Acc_Pkt=0
Temp_Pkt=0
Batt_Pkt=0
Brst_Pkt=0
k=0
l=0
m=0
n=0
o=0
macid=[]
count=[]
count1=[]
slno=0
#Function to check if macid is already present in array.
def checkmacid(file_mac):

	global macid
	n = -1
	for i in range (len(macid)):
		if macid[i] == file_mac:
			n = i
	return n

#Function to return the arry of macid
def comparemacid():	
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
	return(macid)

# Function to create and write to the macid text file.
def writefile(file_mac):

	myfile=open("Non-Connected_Data_G2.txt","r")
	while True:
		content=myfile.readline()
		# print(content)
		if content:
			file_obj = json.loads(content)
			mac_id=file_obj["SensorUUID"]
			if mac_id == file_mac:
				file = open(str(mac_id)+".txt","a")
				py_obj = json.dumps(file_obj)
				file.write(py_obj+"\n")
				file.close()
		else:
			break

#Function to check the packettype and the return the count
def PacketCheck(PacketType):

	if(PacketType=='0'):
		global Dbg_Pkt
		Dbg_Pkt=Dbg_Pkt+1

	elif(PacketType=='1'):
		global Acc_Pkt
		Acc_Pkt=Acc_Pkt+1

	elif(PacketType=='2'):
		global Temp_Pkt
		Temp_Pkt=Temp_Pkt+1

	elif(PacketType=='3'):
		global Batt_Pkt
		Batt_Pkt=Batt_Pkt+1

	elif(PacketType=='4'):
		global Brst_Pkt
		Brst_Pkt=Brst_Pkt+1

	return(Dbg_Pkt,Acc_Pkt,Temp_Pkt,Batt_Pkt,Brst_Pkt)

#Function to each packet in specific file
def PackeTypeCheck(file_mac):  
	Dbg_Pkt=0
	Acc_Pkt=0
	Temp_Pkt=0
	Batt_Pkt=0
	Brst_Pkt=0
	file_name = str(file_mac)+".txt"
	f=open(file_name,"r")
	#Dbg_Pkt,Acc_Pkt,Temp_Pkt,Batt_Pkt,Brst_Pkt=0,0,0,0,0
	while True:
		content=f.readline()
		if content:
			data=json.loads(content)
			PacketType=data["PacketType"]
			Dbg_Pkt,Acc_Pkt,Temp_Pkt,Batt_Pkt,Brst_Pkt=PacketCheck(PacketType)
		else:
			break
	return Dbg_Pkt,Acc_Pkt,Temp_Pkt,Batt_Pkt,Brst_Pkt

#Function to find the burst interval time
def bursttime(testtime,burstinterval):
	burstinterval1=testtime/burstinterval

	return(float(burstinterval1))

# Function to calculate packet type loss
def losscal(burstinterval1,a,b,c,d,e): 
    
	global Dbg_Pkt_loss
	Dbg_Pkt_loss = (( burstinterval1 - a ) / burstinterval1 ) * 100

	global Acc_Pkt_loss
	Acc_Pkt_loss = ((( burstinterval1 * 14 ) - b ) /( burstinterval1 * 14 )) * 100

	global Temp_Pkt_loss
	Temp_Pkt_loss = (( burstinterval1 - c ) / burstinterval1 ) * 100

	global Batt_Pkt_loss
	Batt_Pkt_loss = (( burstinterval1 - d ) / burstinterval1 ) * 100

	global Brst_Pkt_loss
	Brst_Pkt_loss = (( burstinterval1 - e ) / burstinterval1 ) * 100

	return(round(Dbg_Pkt_loss,2)),round(Acc_Pkt_loss,2),round(Temp_Pkt_loss,2),round(Batt_Pkt_loss,2),round(Brst_Pkt_loss,2)

#Function to count the packet types in the file and return array of count 
def indpacketcheck(packettype):

    if packettype == '0':
        global k
        k = k + 1
    elif packettype =='1':
        global l
        l = l + 1
    elif packettype =='2':
        global m
        m = m + 1

    elif packettype =='3':
        global n
        n = n + 1

    elif packettype =='4':
        global o
        o = o + 1
    return(k,l,m,n,o)

# Function to count the packet types in the file and return array of count 
def indbrstpktcnt(macid):
	global k
	global l
	global m
	global n
	global o
	brstpktcnt = [ ]
	tempfilename = str(macid)+".txt"
	f2 = open(tempfilename,"r")
	while True:
		data = f2.readline()
		if data:
			data_obj = json.loads(data)
			packettype = data_obj["PacketType"]
			k,l,m,n,o = indpacketcheck(packettype)
			if packettype == '4':
				# Create array of data
				brstpktcnt.append(k)
				brstpktcnt.append(l)
				brstpktcnt.append(m)
				brstpktcnt.append(n)
				brstpktcnt.append(o)
                # Clear count
				k = 0
				l = 0
				m = 0
				n = 0
				o = 0
		else:
			break
	#print(brstpktcnt)
	return brstpktcnt



#Create csv file
def csvfile(file_mac,Test_time,count1,count):

	file_name = str(file_mac)+".csv"
	with open(file_name,"w") as f:
		write=csv.writer(f,delimiter=',', lineterminator='\n')

		Test_Time=["Testtime",Test_time]
		Packet_loss=["Pkt loss %"]
		Packet_count=["Pkt Cnt"]
		Packet=[' ','Dbg Pkt','Acc Pkt','Temp Pkt','Batt Pkt','Brst Pkt']

		write.writerow(Test_Time)
		write.writerow(Packet)
		write=csv.writer(f,lineterminator= ',')
		write.writerow(Packet_loss)
		write=csv.writer(f,lineterminator= '\n')
		write.writerow(count1)
		write=csv.writer(f,lineterminator= ',')
		write.writerow(Packet_count)
		write=csv.writer(f,lineterminator= '\n')
		write.writerow(count)
		write=csv.writer(f,lineterminator= '\n')
		write.writerow(["Sl.No","Burstwise packet count"])

#Function to write Burst packet data in csv file		
def createcsvfile(file_mac,Burstpkt):

	global slno
	tempfname = str(file_mac)+".csv"
	with open(tempfname, mode='a') as f:
		write_file=csv.writer(f,lineterminator='\n' ,delimiter=',')      
		slno = slno + 1
		if Burstpkt: 
			Burstpkt.insert(0,slno)
			write_file.writerow(Burstpkt)
		else:
			slno = 0
		

Test_time=input("Enter the TestTime:")
Burst_interval=float(input("Enter the Burst interval:"))
comparemacid()

for i in range(len(macid)):
	print(i)
	writefile(macid[i])
	Dbg_Pkt,Acc_Pkt,Temp_Pkt,Batt_Pkt,Brst_Pkt=0,0,0,0,0
	a,b,c,d,e=PackeTypeCheck(macid[i])
	count.append(a)
	count.append(b)
	count.append(c)
	count.append(d)
	count.append(e)
	print(count)
	burstinterval1=bursttime(Test_time,Burst_interval)
	#print(float(burstinterval1))
	f,g,h,i,j=losscal(burstinterval1,a,b,c,d,e)
	count1.append(f)
	count1.append(g)
	count1.append(h)
	count1.append(i)
	count1.append(j)
	print(count1)

x=0
y=5

for i in range(len(macid)):
	Burstpkt=indbrstpktcnt(macid[i])
	#print(Burstpkt)
	csvfile(macid[i],Test_time,count1[x:y],count[x:y])
	x=x+5
	y=y+5

	p=0
	q=5
	for j in range(len(Burstpkt)):
		createcsvfile(macid[i],Burstpkt[p:q])
		p=p+5
		q=q+5


print("Successfully completed")



	





