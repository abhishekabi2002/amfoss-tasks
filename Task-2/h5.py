s=input("Enter the time : ")
t=s[2:10]
if(s[8]+s[9]=="PM"):
        if(s[0]+s[1]=="01"):
                print("13"+t)
        elif(s[0]+s[1]=="02"):
                print("14"+t)
        elif(s[0]+s[1]=="03"):
                print("15"+t)
        elif(s[0]+s[1]=="04"):
                print("16"+t)
        elif(s[0]+s[1]=="05"):
                print("17"+t)
        elif(s[0]+s[1]=="06"):
                print("18"+t)
        elif(s[0]+s[1]=="07"):
                print("19"+t)
        elif(s[0]+s[1]=="08"):
                print("20"+t)
        elif(s[0]+s[1]=="09"):
                print("21"+t)
        elif(s[0]+s[1]=="10"):
                print("22"+t)
        elif(s[0]+s[1]=="11"):
                print("23"+t)
        else:
                print("00"+t)
else:
        print(s)
        
