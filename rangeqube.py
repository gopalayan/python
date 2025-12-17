n=int(input("enter the 1st number:"))
m=int(input("enter the 2nd number:"))
result=0
for i in range(n,m+1,1):
    result=result+i**3
print(result)    