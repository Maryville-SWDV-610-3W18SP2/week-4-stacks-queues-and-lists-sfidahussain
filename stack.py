from node import *

# Stack Implementation using a Linked List
class Stack:
    # Constructor
    def __init__( self):
        self.length = 0
        self.top = None

    def push(self, item):
        self.length += 1
        # Create a new node with the value
        n = Node(item)
        # if list is empty, set the next value to null
        if self.top == None:
            n.next = None
        # if it's not empty, set the next value to top
        else:
            n.next = self.top
        # set top to the new node
        self.top = n
    
    def pop(self):
        if self.top == None:
            print('Cannot pop on empty stack.')
        else:
            # Copy into temporary variable to return value of later
            n = self.top
            # Set the top equal to the next value, cancelling out top
            self.top = self.top.next
            self.length-=1
            return n.getData()
    
    def peek(self):
        return self.top.getData()
    
    def isEmpty(self):
        return self.top == None
    
    def size(self):
        return self.length
    
def main():
    s = Stack()

# Stack Testing
    print('STACK TESTING')
    print(s.isEmpty()) # True
    s.push(4)
    s.push('dog')
    print(s.peek()) # dog
    s.push(True)
    print(s.size()) # 3
    print(s.isEmpty()) # False
    s.push(8.4) 
    print(s.pop()) # 8.4
    print(s.pop()) # True
    print(s.size()) # 2


main()


