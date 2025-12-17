def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return(n1-n2)
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if(n2!=0):
       return n1/n2
    
operations={
    "add":add,
    "sub":sub,
    "mul":mul,
    "div":div
}
n1=list(map(int,input("enter ur no:")))
n2=list(map(int,input("enter ur no:")))
operation=input(" add, sub, mul, div:")
if operation in operations:
    result=map(operations[operation],n1,n2)
    print(list(result))

