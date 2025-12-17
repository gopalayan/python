class div:
    def __init__(self,n):
        self.n=n
       
    def check(self) :
        if self.n%9==0 :
            print("divisible" )
        else:
            print("not divisible")
n=int(input("no. "))
ob=div(n)
ob.check()                 