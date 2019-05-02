import json
#Global Variable
a=0
b=0
c=0
d=0
e=0
#count burst wise packet count
def BrstPktCnt(packet):
    if(packet=='0'):
        global a
        a=a+1
    elif(packet=='1'):
        global b
        b=b+1
    elif(packet=='2'):
        global c
        c=c+1
    elif(packet=='3'):
        global d
        d=d+1
    elif(packet=='4'):
        global e
        e=e+1
    return(a,b,c,d,e)
            

count=[]
f=open("0081F9F04991.txt","r")
while True:
    content=f.readline()
    if content:
        data=json.loads(content)
        packet=data["PacketType"]
        a,b,c,d,e=BrstPktCnt(packet)
        if packet == '4':
            #Creat array
            count.append(a)
            count.append(b)
            count.append(c)
            count.append(d)
            count.append(e)

            a,b,c,d,e=0,0,0,0,0

        
    else:
        break

print(count)
