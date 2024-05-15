class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data):
        newnode=Node(data)
        if(self.front==None and self.rear==None):
            self.front=self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        if (self.front and self.rear == None):
            print('queue is empty')
        else:
            print(f'{self.front.data} is deteted')
            self.front= self.front.next
    def peek(self):
        if (self.front and self.rear == None):
            print('queue is empty')
        else:
            print(self.front.data)
    def display(self):
        temp=self.front
        while temp:
            print(temp.data)
            temp=temp.next
obj=queue()
while(True):
    print('enter 1.enqueue 2.dequeue, 3.peek, 4.display, 5.exit')
    ch=int(input())
    if(ch==1):
        data=int(input())
        obj.enqueue(data)
    if(ch==2):
        obj.dequeue()
    if(ch==3):
        obj.peek()
    if (ch == 4):
        obj.display()
    if(ch==5):
        break
