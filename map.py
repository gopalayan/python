def temperature(c):
    f=c*9/5+32
    return f
num=list(map(int,input("enter your numbers")))
#result=list(map(int,num.split()))
result2=map(temperature,num)
print(list(result2))


