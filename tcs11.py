n=int(input("enter the number:"))
o=n
result=0
while(n!=0):
    re=n%10
    result=result+re**3
    n=n//10
if(o==result):
      print("armstrong no") 
else:
      print(" no") 
       