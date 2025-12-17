num=input("enter ur no:")
list1=list(map(int,num.split()))
num1=input("enter ur no:")
list2=list(map(int,num1.split()))
list3=list1+list2
print("before sorted the list",list3)
n=len(list3)
temp=0
for i in range(n):
    for j in range(n-i-1):
        if list3[j]>list3[j+1]:
            temp=list3[j]
            list3[j]=list3[j+1]
            list3[j+1]=temp

print("after sorted the list",list3)
            
