n=int(input("Enter the number of steps : "))
space=n-1

for i in range(1,n+1):
        for j in range(space):
                print(" ",end="")
        space=space-1
        for k in range(i):
                print("#",end="")
        print()
        
