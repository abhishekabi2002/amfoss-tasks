n=int(input("Enter the number of candles : "))
c=[]

for i in range(n):
        c.append(int(input("Enter the height of the candles : ")))
m=max(c)

c1=0
for i in c:
        if(i==m):
                c1+=1
print("Number of candles she can blow : ",c1)
