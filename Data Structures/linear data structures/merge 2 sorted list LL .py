class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.temp=None
        self.size = 0
    def create(self,size):
        self.size = size
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
    def merge(self,L2):
        t1=self.head
        t2=L2.head
        dummy=Node(-1)
        c=dummy
        while t1 and t2:
            if t1.data<=t2.data:
                c.next=t2
                t1=t1.next
            elif t2.data<=t1.data:
                c.next=t1
                t2=t2.next
            c=c.next
        return dummy.next
    def display(self):
        t = self.head
        while t!= None:
            print(t.data,end=' ')
            t=t.next
L1=Linkedlist()
L2=Linkedlist()
while True:
    print("enter choice 1: l1-create 2: l2-create 3:Display  4.exit")
    choice=int(input('enter:'))
    if(choice==1):
        size = int(input("enter size"))
        L1.create(size)
    if(choice==2):
        size = int(input("enter size"))
        L2.create(size)
    if(choice==3):
        L1.display()
        print()
        L2.display()
    if(choice==5):
        L1.merge(L2)
    if (choice == 4):
        break