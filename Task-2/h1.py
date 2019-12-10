x=list(map(int,input("Enter the numbers : ").split()))
y=list(map(int,input("Enter the numbers : ").split()))

s1=0
s2=0
if(x[0]>y[0]):
        s1+=1
else:
        s2+=1
if(x[1]>y[1]):
        s1+=1
else:
        s2+=1
if(x[2]>y[2]):
        s1+=1
else:
        s2+=1
print(s1,s2)
