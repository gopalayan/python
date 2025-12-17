n=list(map(int,input("enter the array:").split()))
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if(n[i]<n[j]):
            temp=n[j]
            n[j]=n[i]
            n[i]=temp
print(n[1])
               
