
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2

calculator={
    "1":add,
    "2":sub
}
while(True):
    n1=int(input("entr ur no"))
    n2=int(input("entr ur no"))
    ch=input("1 for add,2 for substarct")
    if ch in calculator:
        re=calculator[ch](n1,n2)
        print(re)
       
        
     




