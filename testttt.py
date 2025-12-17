n1=int(input("enter the number input1:"))
n2=int(input("enter the number input2:"))
large=max(n1,n2)
while True:
   if large%n1==0 and large%n2==0:
      print(large)
      break
   else:
      large=large+max(n1,n2)
      
          
         
    
   
  