num=list(map(int,input("enter the number").split()))
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]<num[j]:
            temp=num[j]
            num[j]=num[i]
            num[i]=temp
print(num)           
k=int(input("enter ur element"))
print(num[k-1])