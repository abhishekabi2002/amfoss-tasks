r=int(input("Enter the rows and columns : "))
n=r-1
m=[]
for i in range(r):
      m.append([])
      for j in range(r):
            x=int(input("Enter the numbers : "))
            m[i].append(x)
s=0
for i in range(r):
        s+=m[i][i]
s1=0
for i in range(r):
        s1+=m[i][n]
        n-=1

if(s>s1):
        tot=s-s1
else:
        tot=s1-s

print(tot)
