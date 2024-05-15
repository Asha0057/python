#using circular queueue known as deque:double ended queue
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
            self.rear.next = self.front
    def enqueueFront(self,data):
        newnode=Node(data)
        if(self.front==None and self.rear==None):
            self.front=self.rear=newnode
            self.rear.next = self.front
        else:
            newnode.next=self.front
            self.front=newnode
            self.rear.next = self.front
    def dequeue(self):
        if (self.front and self.rear == None):
            print('queue is empty')
        elif (self.front == self.rear):
            print(f'{self.front.data} is deteted')
            self.front = self.rear = None
        else:
            print(f'{self.front.data} is deteted')
            self.front = self.front.next
            self.rear.next = self.front
    def dequeueEnd(self):
        if (self.front and self.rear == None):
            print('queue is empty')

        elif (self.front == self.rear):
            print(f'{self.front.data} is deteted')
            self.front = self.rear = None

        else:
            current = self.front
            while current.next != self.rear:
                current = current.next
            print(f"Deleted element: {self.rear.data}")
            current.next = self.front
            self.rear = current


    def peek(self):
        if (self.front and self.rear == None):
            print('queue is empty')
        else:
            print(self.front.data)
    def display(self):
        temp=self.front
        while temp!=self.rear:
            print(temp.data,end=' ')
            temp=temp.next
        print(temp.data)
obj=queue()
while(True):
    print('enter 1.enqueue 2.enqueueFront, 3.dequeue,'
          '4.dequeueEnd, 5.peek, 6.display, 7.exit')
    ch=int(input())
    if(ch==1):
        data=int(input('enter data'))
        obj.enqueue(data)
    if (ch == 2):
        data = int(input('enter data'))
        obj.enqueueFront(data)
    if(ch==3):
        obj.dequeue()
    if(ch==4):
        obj.dequeueEnd()
    if(ch==5):
        obj.peek()
    if (ch == 6):
        obj.display()
    if(ch==7):
        break
