class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self):
        size=int(input("enter size"))
        for i in range(size):
            data=int(input("Enter data:"))
            newnode=Node(data)
            newnode.next=None
            if(self.head==None):
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                self.temp=newnode
    def rotation(self):
        rot=int(input('enter rotation:'))
        c=1
        curr=self.head
        while(c<rot and curr.next!=None):
            curr=curr.next
            c=c+1
        newhead=curr.next
        curr.next=None
        self.temp.next = self.head
        self.head=newhead
    def display(self):
        self.temp = self.head
        while self.temp!= None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
obj=Linkedlist()
while True:
    print("enter choice 1:create 2:Display 3:rotation 4:exit")
    choice=int(input('enter:'))
    if(choice==1):
        obj.create()
    if(choice==2):
        obj.display()
    if(choice==3):
        obj.rotation()
    if(choice==4):
        break