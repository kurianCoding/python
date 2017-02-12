class Stack:
    def __init__(self):
        self.stack_list=[]
    def peek(self):
        lastElement=len(self.stack_list)
        element=self.stack_list[lastElement]
        return element
    def push(self,self.stack_list):
        lastElement=len(self.stack_list)
