class stack():
    def __init__ (self, length): #constructor
        self.length = length
        self.list = []
    def pushing(self, item):
        if len(self.list) < self.length:
            self.list.append(item)
        else:
            print ("stack is full)")
    def pop(self):
        self.list.pop(len(self.list)-1)
    def display(self):
        print(self.list)
    def top(self):
        print(self.list[len(self.list)-1])


stack1 = stack(7)
stack1.display()

stack1.pushing(2)
stack1.display()

stack1.pushing(32)
stack1.display()

stack1.pushing(67)
stack1.display()

stack1.pushing(78)
stack1.display()

stack1.pushing(112)
stack1.display()

stack1.pushing(123)
stack1.display()

stack1.pushing(133)
stack1.display()

stack1.pushing(165)
stack1.display()

stack1.pushing(222)

stack1.pop()
stack1.display()

stack1.pop()
stack1.display()

stack1.top()