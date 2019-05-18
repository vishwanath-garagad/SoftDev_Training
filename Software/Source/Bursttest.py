"""Link all the functions into script so that when we run the script it will automatically read the test report file 
and create macid wise text files based on different macids, compute necessary calculation and create macid wise csv files"""
import csv
import json
#Global variable
Total_Dbg_Pkt=0
Total_Acc_Pkt=0
Total_Temp_Pkt=0
Total_Batt_Pkt=0
Total_Brst_Pkt=0
burst_dbg_cnt=0
burst_acc_cnt=0
burst_tmp_cnt=0
burst_bat_cnt=0
burst_bst_cnt=0
macid=[]
count=[]
count1=[]
slno=0

#Local function
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
		global Total_Dbg_Pkt
		Total_Dbg_Pkt=Total_Dbg_Pkt+1

	elif(PacketType=='1'):
		global Total_Acc_Pkt
		Total_Acc_Pkt=Total_Acc_Pkt+1

	elif(PacketType=='2'):
		global Total_Temp_Pkt
		Total_Temp_Pkt=Total_Temp_Pkt+1

	elif(PacketType=='3'):
		global Total_Batt_Pkt
		Total_Batt_Pkt=Total_Batt_Pkt+1

	elif(PacketType=='4'):
		global Total_Brst_Pkt
		Total_Brst_Pkt=Total_Brst_Pkt+1
	return(Total_Dbg_Pkt,Total_Acc_Pkt,Total_Temp_Pkt,Total_Batt_Pkt,Total_Brst_Pkt)
	
# Function to check packet type in specific file 
def PackeTypeCheck(file_mac):  
	Total_Dbg_Pkt=0
	Total_Acc_Pkt=0
	Total_Temp_Pkt=0
	Total_Batt_Pkt=0
	Total_Brst_Pkt=0
	file_name = str(file_mac)+".txt"
	f=open(file_name,"r")
	while True:
		content=f.readline()
		if content:
			data=json.loads(content)
			PacketType=data["PacketType"]
			Total_Dbg_Pkt,Total_Acc_Pkt,Total_Temp_Pkt,Total_Batt_Pkt,Brst_Pkt=PacketCheck(PacketType)
		else:
			break
	return Total_Dbg_Pkt,Total_Acc_Pkt,Total_Temp_Pkt,Total_Batt_Pkt,Brst_Pkt

#Function to find the burst interval time
def bursttime(testtime,burstinterval):
	burstinterval1=testtime/burstinterval
	return(float(burstinterval1))

# Function to calculate packet type loss
def losscal(burstinterval1,dbg_pkt,acc_pkt,batt_pkt,temp_pkt,brst_pkt): 
	global Dbg_Pkt_loss
	Dbg_Pkt_loss = (( burstinterval1 - dbg_pkt ) / burstinterval1 ) * 100
	global Acc_Pkt_loss
	Acc_Pkt_loss = ((( burstinterval1 * 14 ) - acc_pkt ) /( burstinterval1 * 14 )) * 100
	global Temp_Pkt_loss
	Temp_Pkt_loss = (( burstinterval1 - batt_pkt ) / burstinterval1 ) * 100
	global Batt_Pkt_loss
	Batt_Pkt_loss = (( burstinterval1 - batt_pkt ) / burstinterval1 ) * 100
	global Brst_Pkt_loss
	Brst_Pkt_loss = (( burstinterval1 - brst_pkt ) / burstinterval1 ) * 100
	return(round(Dbg_Pkt_loss,2)),round(Acc_Pkt_loss,2),round(Temp_Pkt_loss,2),round(Batt_Pkt_loss,2),round(Brst_Pkt_loss,2)

# Function to check and count burst wise packet types 
def indpacketcheck(packettype):
	if packettype == '0':
		global burst_dbg_cnt
		burst_dbg_cnt = burst_dbg_cnt + 1
	elif packettype =='1':
		global burst_acc_cnt
		burst_acc_cnt = burst_acc_cnt + 1
	elif packettype =='2':
		global burst_tmp_cnt
		burst_tmp_cnt = burst_tmp_cnt + 1
	elif packettype =='3':
		global burst_bat_cnt
		burst_bat_cnt = burst_bat_cnt + 1
	elif packettype =='4':
		global burst_bst_cnt
		burst_bst_cnt = burst_bst_cnt + 1
	return(burst_dbg_cnt,burst_acc_cnt,burst_tmp_cnt,burst_bat_cnt,burst_bst_cnt)

# Function to count the packet types in the file and return array of count 
def indbrstpktcnt(macid):
	global burst_dbg_cnt
	global burst_acc_cnt
	global burst_tmp_cnt
	global burst_bat_cnt
	global burst_bst_cnt
	brstpktcnt = [ ]
	tempfilename = str(macid)+".txt"
	f2 = open(tempfilename,"r")
	while True:
		data = f2.readline()
		if data:
			data_obj = json.loads(data)
			packettype = data_obj["PacketType"]
			burst_dbg_cnt,burst_acc_cnt,burst_tmp_cnt,burst_bat_cnt,burst_bst_cnt = indpacketcheck(packettype)
			if packettype == '4':
				# Create array of data
				brstpktcnt.append(burst_dbg_cnt)
				brstpktcnt.append(burst_acc_cnt)
				brstpktcnt.append(burst_tmp_cnt)
				brstpktcnt.append(burst_bat_cnt)
				brstpktcnt.append(burst_bst_cnt)
                #Clear count
				burst_dbg_cnt = 0
				burst_acc_cnt = 0
				burst_tmp_cnt = 0
				burst_bat_cnt = 0
				burst_bst_cnt = 0
		else:
			break
	return brstpktcnt

# Function to Create csv file
def csvfile(file_mac,Test_time,count1,count):
	file_name = str(file_mac)+".csv"
	with open(file_name,"w") as f:
		write=csv.writer(f,delimiter=',',lineterminator='\n')
		Test_Time=["Testtime",Test_time]
		Packet_loss="Pkt loss %"
		Packet_count="Pkt Cnt"
		Packet=[' ','Dbg Pkt','Acc Pkt','Temp Pkt','Batt Pkt','Brst Pkt']
		count1.insert(0,Packet_loss)
		count.insert(0,Packet_count)
		# write the data in csv file
		write.writerow(Test_Time)
		write.writerow(Packet)
		write.writerow(count1)
		write.writerow(count)
		write.writerow(["Sl.No","Burstwise packet count"])

#Function to write Burst packet data in csv file		
def createcsvfile(file_mac,Burstpkt):
	global slno
	tempfname = str(file_mac)+".csv"
	with open(tempfname, mode='a') as f:
		write_file=csv.writer(f,delimiter=',',lineterminator='\n')     
		slno = slno + 1
		if Burstpkt: 
			Burstpkt.insert(0,slno)
			# write the data in csv file
			write_file.writerow(Burstpkt)
		else:
			slno = 0

# Prompt user to enter test time and burst interval	
Test_time=input("Enter the TestTime:")
Burst_interval=float(input("Enter the Burst interval:"))

#Check macid in the file and create array of macid
comparemacid()

for i in range(len(macid)):
	print(i)
	writefile(macid[i])
	Total_Dbg_Pkt=0
	Total_Acc_Pkt=0
	Total_Temp_Pkt=0
	Total_Batt_Pkt=0
	Total_Brst_Pkt=0
	dbg_pkt,acc_pkt,temp_pkt,batt_pkt,brst_pkt=PackeTypeCheck(macid[i])
	count.append(dbg_pkt)
	count.append(acc_pkt)
	count.append(batt_pkt)
	count.append(batt_pkt)
	count.append(brst_pkt)
	print(count)
	burstinterval1=bursttime(Test_time,Burst_interval)
	Dbg_Pkt_loss,Acc_Pkt_loss,Temp_Pkt_loss,Batt_Pkt_loss,Brst_Pkt_loss=losscal(burstinterval1,dbg_pkt,acc_pkt,batt_pkt,batt_pkt,brst_pkt)
	count1.append(Dbg_Pkt_loss)
	count1.append(Acc_Pkt_loss)
	count1.append(Temp_Pkt_loss)
	count1.append(Batt_Pkt_loss)
	count1.append(Brst_Pkt_loss)
	print(count1)

x=0
y=5
for i in range(len(macid)):
	Burstpkt=indbrstpktcnt(macid[i])
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



	

 



