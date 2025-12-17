class differce:
    def __init__(self,n):
        self.n=n
    def element(self):
        self.n.sort() 
        total=self.n[len(self.n)-1]-self.n[0]  
        print(total)
n=list(map(int,input("enter the no:").split()))
ob=differce(n) 
ob.element()       