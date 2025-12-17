def sum(i,j):
    return ((j *(j+1) // 2) - i*(i-1)//2)
n=int(input("enter the number:"))
for i in range(n):
    user=input()
    values=user.split()
    if(len(values)<2):
        print("invaliss")
        continue
    i,j=map(int,values)
    if(i>=j or i<0 or j>=10000):
        print("invalid ")
    else:
        print(sum(i,j),end=" ")    