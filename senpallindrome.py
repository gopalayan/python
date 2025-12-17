n=int(input("enter the number:"))
a=0
b=1
print(a)
print(b)
sum=0
for i in range(2,n):
    c=a+b
    sum=sum+c
    print(c)
    a=b
    b=c
print(sum+1)