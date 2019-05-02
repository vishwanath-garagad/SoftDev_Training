import json
#Global Variable
zero=0
one=0
two=0
three=0
four=0
#count the total number of packet types (0,1,2,3 and 4) 
def PacketCheck(check):
    if(check=='0'):
        global zero
        zero=zero+1
    elif(check=='1'):
        global one
        one=one+1
    elif(check=='2'):
        global two
        two=two+1
    elif(check=='3'):
        global three
        three=three+1
    elif(check=='4'):
        global four
        four=four+1
    return(zero,one,two,three,four)
  
f=open("0081F9F04991.txt","r")
while True:
    content=f.readline()
    if content:
        data=json.loads(content)
        check=data["PacketType"]
        zero,one,two,three,four=PacketCheck(check)

    else:
        break
print(zero,one,two,three,four)