n=int(input("enter the no"))
num=[]
for i in range(n):
    num.append(int(input("enter ur list")))

n1=int(input("enter yor sub array no"))


sublists = [num[i:i+3] for i in range(0, n1, 1)]


print(sublists)  
list=[]
for i in range(0,n1,1):
    list.append(max(sublists[i]))
print(list)