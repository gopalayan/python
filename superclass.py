class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age) 
    def add(self):
        print(5)    
class student(person):
    def __init__(self,name,age):
        self.sname=name
        self.sage=age
        super().__init__('gopal',21)
    def diplayinfo1(self):
        print(self.sname)
        print(self.sage) 
s1=student('sarkar',21)
s1.display()
s1.diplayinfo1()
s1.add()                       