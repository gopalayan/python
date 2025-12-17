num=list(map(int,input("enter the no:" ).split()))

for i in range(len(num)):
    if(num[i]<0):
         num.remove
    if(len(num)%2==0):
        m=len(num)//2
        print(num[m-2])
    if(len(num)%2!=0):
            m=(len(num)+1)//2
            print(num[m-2])
