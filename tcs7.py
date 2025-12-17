
num=[]
for i in range(150,100,-1):
   result=0
   o=i

   
   while(i!=0):
      re=i%10
      result=10*result+re
      i=i//10
   if(result==o):
      num.append(o)
         
print(num)    