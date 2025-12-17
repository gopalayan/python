n=int(input("enter ur no"))
f0=0
f1=1
print(f0,f1)
for i in range(2,n):
    f2=f0+f1
    print(f2)
    f0=f1
    f1=f2
    