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
    def display(self):
        self.temp = self.head
        while self.temp!= None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
    def sorting(self):
        t = self.head
        while t:
            t2 = t.next
            while t2:
                if(t.data>t2.data):
                    t.data,t2.data=t2.data,t.data
                t2=t2.next
            t=t.next
    def sortingReverse(self):
        t = self.head
        while t:
            t2 = t.next
            while t2:
                if(t.data<t2.data):
                    t.data,t2.data=t2.data,t.data
                t2=t2.next
            t=t.next
obj=Linkedlist()
while True:
    print("enter choice 1:create 2:Display 3:sort,4:sortingreverse,5:exit")
    choice=int(input('enter:'))
    if(choice==1):
        obj.create()
    if(choice==2):
        obj.display()
    if(choice==3):
        obj.sorting()
    if(choice==4):
        obj.sortingReverse()
    if(choice==5):
        break