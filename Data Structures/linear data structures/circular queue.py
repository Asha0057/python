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
            self.rear.next = self.front
        else:
            self.rear.next=newnode
            self.rear=newnode
            self.rear.next=self.front

    def dequeue(self):
        if (self.front and self.rear == None):
            print('queue is empty')

        elif(self.front==self.rear):
            print(f'{self.front.data} is deteted')
            self.front=self.rear=None
        else:
            print(f'{self.front.data} is deteted')
            self.front= self.front.next
            self.rear.next=self.front

    def peek(self):
        if (self.front and self.rear == None):
            print('queue is empty')
        else:
            print(self.front.data)

    def display(self):
        if (self.front and self.rear == None):
            print('queue is empty')
        temp=self.front
        while temp!=self.rear: #or temp.next!=front
            print(temp.data,end=' ')
            temp=temp.next
        print(temp.data)
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
