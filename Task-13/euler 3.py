n=int(input("Enter the number of test cases : "))

for i in range(n):
        x=int(input("Enter the number : "))
        f=[]
        for j in range(2,x):
                if(x%j==0):
                        f.append(j)
        if(len(f)==0):
                f.append(x)
        prime=[]
        for k1 in f:
                for k in range(2,k1+1):
                        if(k1%k!=0):
                                prime.append(k1)
        print("The largest prime factor of",x ," is ",max(prime))

                        
