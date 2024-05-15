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
    def swap(self):
        x=int(input())
        y=int(input())
        temp1=None
        curr1=self.head
        while(curr1 and curr1.next.data!=x):
            temp1=curr1
            curr1=curr1.next
        temp2=self.head
        curr2=self.head
        while(temp2.next.data!=y):
            temp2=curr2
            curr2=curr2.next
        if temp1:
            temp1.next=curr2
        else:
            head=curr2
        if temp2:
            temp2.next=curr1
        else:
            head=curr1
        curr1.next,curr2.next=curr2.next,curr1.next



    def display(self):
        self.temp = self.head
        while self.temp!= None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
while True:
    print("enter choice 1:create 2:Display 3:swap")
    choice=int(input('enter:'))
    if(choice==1):
        obj=Linkedlist()
        obj.create()
    if(choice==2):
        obj.display()
    if(choice==3):
        obj.swap()