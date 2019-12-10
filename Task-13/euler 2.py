t=int(input("Enter the number of test cases : "))

for i in range(t):
        n=int(input("Enter the number : "))
        x=0
        y=1
        c=0
        f=[]

        if(n<=0):
                print("Enter the positive number : ")
        elif(n==2):
                print("0")
        else:
                while(c<n):
                        f.append(x)
                        s=x+y
                        x=y
                        y=s
                        c+=1

        s=0
        for i in f:
                if(i<n):
                        if(i%2==0):
                                s+=i
        print(s)
        
    
        
        
