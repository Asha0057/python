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
    def del_Nth(self,size):
        n = int(input('enter N:'))
        self.size = size
        if (n == size):
            self.head = self.head.next
        else:
            f=self.head
            s=self.head
            c=-1
            for i in range(n):
                f=f.next
            while(f.next!=None):
                f=f.next
                s=s.next
            s.next=s.next.next
        self.size-=self.size #decrement the size after every deletion else it will be always the same

    def display(self):
        self.temp = self.head
        while self.temp!= None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
obj=Linkedlist()
while True:
    print("enter choice 1:create 2:Display 3:Delete 4.exit")
    choice=int(input('enter:'))
    if(choice==1):
        size = int(input("enter size"))
        obj.create(size)
    if(choice==2):
        obj.display()
    if(choice==3):
        obj.del_Nth(size)
    if (choice == 4):
        break