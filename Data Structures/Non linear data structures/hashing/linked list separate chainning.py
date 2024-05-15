class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def probing(self, arr, size):
        table = [None] * size
        for key in arr:
            index = (2 * key + 3) % size
            if table[index] is None:
                table[index] = Node(key)
            else:
                curr = table[index]
                while curr.next is not None:
                    curr = curr.next
                curr.next = Node(key)
        for node in table:
            curr = node
            while curr is not None:
                print(curr.key, end=' -> ')
                curr = curr.next
            print("None")

obj = LinkedList()
size = 10
arr = [12, 13, 11, 10, 2, 1]
obj.probing(arr, size)
