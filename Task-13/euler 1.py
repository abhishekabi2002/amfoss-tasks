n=int(input("Enter the number of test cases : "))


for i in range(n):
        x=int(input("Enter the number : "))
        s=0
        for j in range(1,x):
                if(j%3==0 or j%5==0):
                        s+=j
        print(s)
