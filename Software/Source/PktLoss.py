import json
#Global Variable
zero=0
one=0
two=0
three=0
four=0
zero_los=0
one_loss=0
three_loss=0
four_loss=0
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

def losscal(): 
    f=open("B0912265674C.txt","r")
    while True:
        content=f.readline()
        if content:
            data=json.loads(content)
            check=data["PacketType"]
            data1=PacketCheck(check)
            #print(zero,one,two,three,four)
        
        else:
            break
    print(data1)
    #Calculate packetwise loss percentage 
    Test_Time=input("Enter the TestTime in min:")
    var1=float(Test_Time/3)
    print(float(var1))
    global zero_loss
    zero_loss=((var1-zero)/var1)*100
    global one_loss
    one_loss=(((var1*14)-one)/(var1*14))*100
    global two_loss
    two_loss=((var1-two)/var1)*100
    global three_loss
    three_loss=((var1-three)/var1)*100
    global four_loss
    four_loss=((var1-four)/var1)*100



    return(zero_loss,one_loss,two_loss,three_loss,four_loss)

zero_loss,one_loss,two_loss,three_loss,four_loss=losscal()
print(round(zero_loss,2)),round(one_loss,2),round(two_loss,2),round(three_loss,2),round(four_loss,2)

    


