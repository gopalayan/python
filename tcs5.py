n1=int(input("nter the no"))
a=0
b=1
print(a)
print(b)
s=0
for i in range(2,n1):

    c=a+b
    s=s+c
    print(c)
    
    a=b
    b=c
print(s+1)    
