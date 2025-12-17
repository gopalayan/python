n=int(input("enter ur no"))
s=0
while(n!=0):
    #q=n/10
    r=n%10
    s=s*10+r
   
    n=n//10
print(s)    