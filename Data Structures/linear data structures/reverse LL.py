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
    def reverse(self):
        prev=None
        temps=self.head
        while(temps!=None):
            nxt=temps.next
            temps.next=prev
            prev=temps
            temps=nxt
        self.head=prev

    def display(self):
        self.temp = self.head
        while self.temp!= None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
obj=Linkedlist()
while True:
    print("enter choice 1:create 2:Display 3:reverse 4.exit")
    choice=int(input('enter:'))
    if(choice==1):
        size = int(input("enter size"))
        obj.create(size)
    if(choice==2):
        obj.display()
    if(choice==3):
        obj.reverse()
    if (choice == 4):
        break