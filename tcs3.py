n=[3,4,-7,1,3,3,1,-4]
target=7
sum=0
for i in range(8):
    for j in range(i+1,8):
        sum=sum+n[j]
        if((n[i]+sum)==target):
            print(n[i:j+1])