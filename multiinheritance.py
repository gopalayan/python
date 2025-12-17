class name:
    def __init__(self,fn):
        self.fn=fn
        #print(self.fn)
class title:
    def __init__(self,ln):
        self.ln=ln
       # print(self.ln)
class fullname(name,title):
    def __init__(self):
        super().__init__('gopal')
        super().__init__('sarkar')
    def printstr(self):
        print(self.fn+self.ln)  
Name=fullname()
Name.printstr()              