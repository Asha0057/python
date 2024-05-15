class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top = newnode

    def pop(self):
        if self.top is None:
            print('Stack is empty')
        else:
            #temp = self.top
            print("Popped element is:", self.top.data)  # Corrected reference to temp
            self.top = self.top.next
            #del temp

    def display(self):
        temp=self.top
        if temp is None:
            print("stack is empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next
    def peek(self):
        print(self.top.data)

obj=stack()
while(True):
    print('enter 1.push, 2.pop, 3.peek, 4.display, 5exit')
    ch=int(input())
    if(ch==1):
        data=int(input())
        obj.push(data)
    if(ch==2):
        obj.pop()
    if(ch==3):
        obj.peek()
    if (ch == 4):
        obj.display()
    if(ch==5):
        break
