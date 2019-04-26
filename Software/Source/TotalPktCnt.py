import json
def check():
    zero=0
    one=0
    two=0
    three=0
    four=0
    f=open("0081F9F04991.txt","r")
    while True:
        content=f.readline()
        if content:
            data=json.loads(content)
            check=data["PacketType"]
            if(check=='0'):
                zero=zero+1
            elif(check=='1'):
                one=one+1
            elif(check=='2'):
                two=two+1
            elif(check=='3'):
                three=three+1
            elif(check=='4'):
                four=four+1
            else:
                print("Invalid")
        else:
            break
    print("zero="+str(zero)) 	
    print("one="+str(one))		
    print("two="+str(two))
    print("three="+str(three))
    print("four="+str(four))

check()






