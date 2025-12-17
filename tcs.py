n=int(input("enter ur no"))
store={}
for i in range(n):
    item=input("enter ur item:")
    price=int(input("enter ur price:"))
    quantity=int(input("enter ur quantity:"))
    totalprice=price*quantity
    store[item]=store.get(item,0)+totalprice
total=0
maxCost=0
maxCostItem=""

for key,value in store.items():
    if maxCost<value:
        maxCostItem=key
        maxCost=value 
        total=total+value
avr=total//n          
print(maxCostItem)    
print(total)
print(avr)
   