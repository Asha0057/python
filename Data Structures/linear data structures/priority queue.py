class Node:
    def __init__(self,data,priority):
        self.data=data
        self.next=None
        self.priority=priority
class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data,priority):
        newnode=Node(data,priority)
        if(self.front==None and self.rear==None):
            self.front=self.rear=newnode
        elif(priority<=self.front.priority):
                self.rear.next=newnode
                self.rear=newnode
        else:
            temp = self.front
            while temp is not None and priority > self.front.priority:
                newnode.next = self.front
                self.front = newnode
                temp=temp.next
    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
obj=queue()
while(True):
    print('enter 1.enqueue 2.display, 5.exit')
    ch=int(input())
    if(ch==1):
        data=int(input())
        priority=int(input())
        obj.enqueue(data,priority)
    if(ch==2):
        obj.display()
    if(ch==5):
        break