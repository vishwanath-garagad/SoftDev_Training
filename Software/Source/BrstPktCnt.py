import json
def check():
    count=0
    f=open("0081F9F04991.txt","r")
    while True:
        content=f.readline()
        if content:
            data=json.loads(content)
            check=data["PacketType"]
            if(check=='4'):
                count=count+1
        elif(content==''):
            continue
        else:
            break
    print(count)

check()



