n=input("enter the string")
count=0
count1=0
for i in n:
    if i.isupper():
        count=count+1
        
    if i.islower():
        count1=count1+1
if(count>count1):
    print(n.upper())
else:
    print(n.lower())    
