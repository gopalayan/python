n=list(map(int,input("enter the array").split()))
target=int(input("enter ur no"))
re=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        re=n[i]+re
        print(re)
        if(re==target):
           print(n[i:j+1])
    
    