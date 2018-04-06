from node import *

# Implement a deque using linked lists
class Deque:
    def __init__(self):
        self.length = 0
        self.front = None
        self.rear = None
        
    def addFront(self, item):
        self.length += 1
        n = Node(item)
        n.next = None
        # if it's no items
        if self.front == None:
            self.front = n
            self.rear = n
        else:
            # set the next value of the node to front
            n.next = self.front
            # set front to the new node
            self.front = n
    
    def addRear(self, item):
        self.length += 1
        # set node with the new item
        n = Node(item)
        n.next = None
        # if there is no items
        if self.rear == None:
            self.front = n
            self.rear = n
        else:
            # sets new node after rear
            self.rear.next = n
            # moves rear to new node
            self.rear = n 
    
    def removeFront(self):
        if self.front == None:
            print('Cannot delete from an empty queue.')
        else:
            # store front data to return later
            n = self.front.data
            # moving front one node ahead
            self.front = self.front.next
            self.length -= 1
            return n
        
    def removeRear(self):
        if self.front == None:
            print('Cannot delete from an empty queue.')
        # if there's only one node left
        elif self.front == self.rear:
            n = self.front.data
            self.front = None
            self.rear = None
            self.length -= 1
            return n
        else:
            # store n to return later
            n = self.rear.data
            # loop from the front to get the node right before rear
            temp = self.front
            while temp.next != self.rear:
                temp = temp.next
            # set the rear to the temp value
            self.rear = temp
            # set the next to none
            self.rear.next = None
            self.length -= 1
            return n
    
    def isEmpty(self):
        return self.front == None
    
    def size(self):
        return self.length
    
def main():
    d = Deque()

# Deque Testing
    print()
    print('DEQUE TESTING')
    print(d.isEmpty()) # True
    d.addFront(4)
    d.addRear('dog')
    d.addFront(True)
    print(d.size()) # 3
    print(d.isEmpty()) # False
    d.addRear(8.4) 
    print(d.removeFront()) # True 4 dog 8.4   -> True
    print(d.removeRear()) # 4 dog 8.4  -> 8.4
    print(d.removeRear()) # 4 dog  -> dog
    print(d.size()) # 1
    print(d.removeRear()) # 4  -> 4
    print(d.size()) # 0


main()



