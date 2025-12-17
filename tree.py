class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root is None:
             self.root=node(value)
        else:
            self._insert(value,self.root)     
    def _insert(self,value,currentnode):
        if value<currentnode.value:
            if currentnode.left is None:
                currentnode.left=node(value)
            else:
                self._insert(value,currentnode.left)   
        elif value>currentnode.value:
              if currentnode.right is None:
                currentnode.right=node(value)
              else:
                 self._insert(value,currentnode.right) 
        else:
            print("elment is already exist")

    def prin_t(self):
        if self.root is not None:
            self._prin_t(self.root)
    def _prin_t(self,current_node):
         if current_node is not None:
             self._prin_t(current_node.left)
             print(current_node.value)
             self._prin_t(current_node.right)
tree=bst()
tree.insert(10)
tree.insert(5)
tree.insert(8)
tree.insert(2)
tree.prin_t()