
n=list(map(int,input("enter the list:").split()))
sum=0
list=[i for i in n if n.count(i)==1]
print(list)
for i in range(len(list)):
    sum=sum+list[i]
print(sum)

        

    
        