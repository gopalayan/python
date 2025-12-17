n=int(input("enter the number:"))
prime=[]
total=0
for num in range(2,n+1):
    for i in range(2,num):
      if num%i==0:
           break
    else:
       prime.append(num)    
print(sum(prime)) 