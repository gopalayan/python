class add:
    def method(self, n1, n2):
        self.n1=n1
        self.n2=n2
        result=0
        for i in range(n1,n2+1):
            result=result+i
        return result
obj=add()

print(obj.method(0,3))

   