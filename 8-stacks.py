"""Stack Module.

This module implements the Stack data structure using LinkedList.
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
        
class Stack:
    """Stack class."""
    def __init__(self, data=None):
        """Used to create Stack objects. It's called during object instantiation.
        
        Args:
            data: What you want to store. Optional, defaults to None.
        """
        self.top = None
        
        # Check if the stack was initialized with an argument then update the length property of the stack
        if data is None:
            self.length = 0
        else:
            node = Node(data)   # Create a node with given data
            self.top = node     # Set the node as top of stack
            self.length = 1     # Update the length property of the stack
            
    def getTop(self):
        """Prints the top of a stack."""
        if self.top is None:
            print("Top: null")
        else:
            print("Top: " + self.top.value)
            
    def getLength(self):
        """Prints the length of a stack."""
        print("Length: " + self.length)
        
    def makeEmpty(self):
        """Empties the stack."""
        self.top = None
        self.length = 0
        
    def push(self, data=None):
        """Inserts node at top of stack. When supplied a list, it creates nodes for each element of the list and 
        insert them at the top of the stack.
        
        Args:
            data: What you want to store. Optional, defaults to None.
        
        Returns:
            Updated Stack.
        """
        # Handle input error
        if data is None:
            print("No data was supplied for push operation!")
            return
        
        if type(data) == list:
            for val in data:
                self.push(val)
        else:
            node = Node(data)
            
            if self.length == 0:
                self.top = node
            else:
                node.next = self.top
                self.top = node
            self.length += 1
        
        return self
    
    def pop(self):
        """Removes node from end of Stack.
        
        Returns:
            Updated Stack.
        """
        # Check if Stack is empty
        if self.length == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        
        return temp
    
    def print(self):
        """Prints the stack in human readable format"""
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next
            
            
myStack = Stack()
myStack.push(0)
myStack.push([1, 2, 3])
myStack.pop()
myStack.print()