class node:
    def __init__(self,d):
        self.d=d
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def append(self,d):
        new_node=node(d)
        if self.head is None:
            self.head=new_node
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=new_node
    def print_link(self):
        p=self.head
        while p:
            print(p.d)
            p=p.next
l=linklist()
l.append(1)
l.append(2)
l.append(3)
l.print_link()            


                                