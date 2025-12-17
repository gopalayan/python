n=int(input("enter the number:"))
num=[]
for i in range(n):
    num.append(int(input("enter ur list:")))
n1=int(input("enter yr sub array:"))    
sublist=[num[i:i+3] for i in range(0,n1)]
print(sublist)
list=[]
for i in range(0,n1):
    list.append(max(sublist[i]))
print(list)    


