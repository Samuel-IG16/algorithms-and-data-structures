"""Queue Module.

This module implements the Queue data structure using LinkedList.
"""

class Node:
    """Node class"""
    def __init__(self, data=None, next_node=None):
        """Used to create node objects. It's called during object instantiation.
        
        Args:
            data: What you want to store. Optional, defaults to None.
            next_node: The address of the next node. Optional, defaults to None.
        """
        self.data = data    # data is a property of the Node class
        self.next = next_node    # next is a property of the Node class

class Queue:
    """Queue class."""
    def __init__(self, data=None):
        """Used to create Queue objects. It's called during object instantiation.
        
        Args:
            data: What you want to store. Optional, defaults to None.
        """
        # Check if the Queue was initialized with an argument then update the length property of the Queue
        if data is None:
            self.length = 0
        else:
            node = Node(data)   # Create a node with given data
            self.first = node   # Set the node as top of queue
            self.last = node    # Set the node as top of queue
            self.length = 1     # Update the length property of the queue
    
    def getFirst(self):
        """Prints the first in queue."""
        if self.first is None:
            print("First: null")
        else:
            print("First: " + self.first.value)
            
    def getLast(self):
        """Prints the last in queue."""
        if self.last is None:
            print("Last: null")
        else:
            print("Last: " + self.last.value)
    
    def getLength(self):
        """Prints the length of queue."""
        print("Length: " + self.length)
    
    def makeEmpty(self):
        """Empties the queue."""
        self.first = None
        self.last = None
        self.length = 0
        
    def enqueue(self, data=None):
        """Inserts node into a queue. When supplied a list, it creates nodes for each element of the list and 
        insert them into the queue.
        
        Args:
            data: What you want to store. Optional, defaults to None.
        
        Returns:
            Updated Queue.
        """
        # Handle input error
        if data is None:
            print("No data was supplied for push operation!")
            return
        
        node = Node(data)
        
        if type(data) == list:
            for val in data:
                self.enqueue(val)
        else:
            if self.length == 0:
                self.first = node
                self.last = node
            else:
                self.last.next = node
                self.last = node
            self.length += 1
        
        return self

    def dequeue(self):
        """Removes first node from Queue.
        
        Returns:
            Updated Queue.
        """
        # Check if Queue is empty
        if self.length == 0:
            return None
        
        temp = self.first
        
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
            self.length -= 1
        
        return temp
    
    def peek(self):
        """Returns data in front node from Queue.
        
        Returns:
            First node data.
        """
        # Check if Queue is empty
        if self.length == 0:
            return "Queue is Empty"
        
        return self.first.data
            
    def print(self):
        """Prints the queue in human readable format"""
        temp = self.first
        while temp:
            print(temp.data)
            temp = temp.next

myQueue = Queue()
myQueue.enqueue(0)
myQueue.enqueue([1, 2, 3, 4])
myQueue.dequeue()
myQueue.print()