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
    def insertFront(self):
        #self.temp=self.head
        newnode=Node(int(input('Enter data to insert:')))
        newnode.next=self.head
        self.head=newnode
    def insertEnd(self):
        self.temp=self.head
        while(self.temp.next!=None):
            self.temp=self.temp.next
        newnode = Node(int(input('Enter data to insert:')))
        self.temp.next=newnode
    def insertMid(self):
        newnode = Node(int(input('Enter data to insert:')))
        pos=int(input("\nenter pos:"))
        i=1
        self.temp=self.head
        while(i<pos):
            self.temp=self.temp.next
            i=i+1
        newnode.next=self.temp.next
        self.temp.next=newnode
    def deleteFront(self):
        self.temp=self.head
        self.head=self.head.next
        del self.temp
    def deleteEnd(self):
        self.temp=self.head
        prev=None
        while(self.temp.next!=None):
            prev=self.temp
            self.temp=self.temp.next
        if(self.head==self.temp):
            self.head=None
        else:
            prev.next=None
        del self.temp
    def detemid(self):
        self.temp=self.head
        pos=int(input("enter pos"))
        i=1
        nextnode=None
        while(i<pos):
            self.temp=self.temp.next
            i=i+1
        nextnode=self.temp.next
        self.temp.next=nextnode.next
        del nextnode
    def count(self):
        self.temp = self.head
        c=0
        while self.temp != None:
            c=c+1
            self.temp = self.temp.next
        print(c)
    def search(self):
        s=int(input("enter elemant to search:"))
        self.temp=self.head
        while(self.temp):
            if(self.temp.data==s):
                print(s," is prestent")
                break #or return
            self.temp=self.temp.next
        print(s," not found")


obj=Linkedlist()
while True:
    print("enter choice 1:create 2:Display 3:insertFront 4:insertEnd 5:insertmid"
          " 6:deletefront 7:deleteEnd 8:deleteMid 9:count 10:search 11:exit")
    choice=int(input('enter:'))
    if(choice==1):
        obj.create()
    if(choice==2):
        obj.display()
    if(choice==3):
        obj.insertFront()
    if(choice==4):
        obj.insertEnd()
    if(choice==5):
        obj.insertMid()
    if(choice==6):
        obj.deleteFront()
    if (choice == 7):
        obj.deleteEnd()
    if (choice == 8):
        obj.deletemid()
    if (choice == 9):
        obj.count()
    if (choice == 10):
        obj.search()
    if(choice==11):
        break


