"""Linked List Module.

This module implements the LinkedList data structure by creating the basic building block (Nodes) and (LinkedList) as classes.
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

class LinkedList:
    """LinkedList class."""
    def __init__(self, data=None):
        """Used to create a LinkedList objects. It's called during object instantiation.
        
        Args:
            data: What you want to store. Optional, defaults to None.
        """
        self.head = None    # head is a property of the class LinkedList
        self.tail = None    # tail is a property of the class LinkedList
        
        # Check if the linked list was initialized with an argument then update the length property of the LinkedList
        if data is None:
            self.length = 0
        else:
            node = Node(data)   # Create a node with given data
            self.head = node    # Set the node as head of LinkedList
            self.tail = node    # Set the node as tail of LinkedList
            self.length = 1     # Update the length property of the LinkedList
    
    def push(self, data=None):
        """Inserts node at end of LinkedList. When supplied a list, it creates nodes for each element of the list and 
        insert them at the end of the LinkedList.
        
        Args:
            data: What you want to store. Optional, defaults to None.
        
        Returns:
            Updated LinkedList.
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
            
            # Check if LinkedList is empty and assign newly created node accordingly
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            self.length += 1
        
        return self
    
    def pop(self):
        """Removes node from end of LinkedList.
        
        Returns:
            Updated LinkedList.
        """
        # Check if LinkedList is empty
        if self.head is None:
            print("No more Nodes to remove from LinkedList")
            return
        
        # We need to transverse through the linked list with two variables. Both will start at head of the LinkedList
        temp = self.head    # Used to hold the second to last node
        check = self.head   # Used to hold last node
        
        if self.length == 1:
            self.head = None
            self.length -= 1
        else:
            # Check each node's next value and passes it to temp except the last node
            while check.next:
                temp = check
                check = check.next
            else:                       # When we finally get to the last node we omit it by not assigning it to temp
                self.tail = temp        # temp being on the second to last node is now set as tail of LinkedList
                self.tail.next = None   # Tail is made to always point to None
                self.length -= 1        # Update the length of the LinkedList

        return self
    
    def unshift(self, data=None):
        """Inserts node at beginning of LinkedList.
        
        Args:
            data: What you want to store. Optional, defaults to None.
        
        Returns:
            Updated LinkedList.
        """
        # Handle input error
        if data is None:
            print("No data was supplied for unshift operation!")
            return
        
        node = Node(data)
        
        # Check if LinkedList is empty and assign newly created node accordingly
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        
        return self
    
    def shift(self):
        """Removes node from beginning of LinkedList.
        
        Returns:
            Updated LinkedList.
        """
        # Check if LinkedList is empty
        if self.head is None:
            print("No more Nodes to remove from LinkedList")
            return

        # Set the next node after head as new head
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        
        return self
    
    def get(self, index=None):
        """Gets node at given index of LinkedList.
        
        Args:
            index: Index of node. Optional, defaults to None.
        
        Returns:
            The Node at given index.
        """
        # Handle input error
        if index is None:
            print("Index is required for this operation!")
            return
        
        # Handle input error. Checks for negative indexing and overflow(non-exixting indexes)
        if index < 0 or index >= self.length:
            print("Cannot process negative or non-exixting index!")
            return

        # Iterate through the LinkedList to return the required node
        node = self.head
        
        for i in range(index):
            node = node.next
        
        return node

    def set(self, index=None, data=None):
        """Overwrites the data attribute of a node at a given index.
        
        Args:
            index: Index of target node. Optional, defaults to None.
            data: What you want to store. Optional, defaults to None.
        
        Returns:
            Updated LinkedList.
        """
        # Handle input error
        if index is None and data is None:
            print("No data or index was supplied for set operation!")
            return
        
        if index is None:
            print("Index is required for this operation!")
            return
        
        if data is None:
            print("Data is required for this operation!")
            return
        
        # Handle input error. Checks for negative indexing and overflow(non-exixting indexes)
        if index < 0 or index >= self.length:
            print("Cannot process negative or non-exixting index!")
            return
        
        node = self.get(index)  # Gets the node we want to insert data in
        node.data = data        # Calls the data attribute of node and assign the data value to it
        
        return self
    
    def insert(self, index=None, data=None):
        """Inserts a node in front of another node at a given index.
        
        Args:
            index: Index of target node. Optional, defaults to None.
            data: What you want to store. Optional, defaults to None.
        
        Returns:
            Updated LinkedList.
        """
        # Handle input error
        if index is None and data is None:
            print("No data or index was supplied for set operation!")
            return
        
        if index is None:
            print("Index is required for this operation!")
            return
        
        if data is None:
            print("Data is required for this operation!")
            return
        
        # Handle input error. Checks for negative indexing and overflow(non-exixting indexes)
        if index < 0 or index >= self.length:
            print("Cannot process negative or non-exixting index!")
            return
        
        # Check if we want to insert in front of head
        if self.get(index) == self.head:
            self.unshift(data)  # Inserts in front of head
        else:
            node = Node(data)
            prevNode = self.get(index-1)    # Get the node to the left of insert position
            curr = prevNode.next            # Get the node to the right of insert position
            prevNode.next = node            # Set the new node to the next value of node on left
            node.next = curr                # Set the new node next to the node on right
            self.length +=1                 # Update the length of the LinkedList
        
        return self
    
    def remove(self, index=None):
        """Removes node object at a given index.
        
        Args:
            index: Index of target node. Optional, defaults to None.
        
        Returns:
            Updated LinkedList.
        """
        # Handle input error
        if index is None:
            print("Index is required for this operation!")
            return
        
        # Handle input error. Checks for negative indexing and overflow(non-exixting indexes)
        if index < 0 or index >= self.length:
            print("Cannot process negative or non-exixting index!")
            return
        
        # Check if we want to remove head or tail
        if self.get(index) == self.head:
            self.shift()  # Removes head
        elif self.get(index) == self.tail:
            self.pop()  # Removes tail
        else:
            temp = self.get(index)          # Get the node to remove 
            prevNode = self.get(index-1)    # Get the node to the left of remove position
            nextNode = self.get(index+1)    # Get the node to the right of remove position
            prevNode.next = nextNode        # Set the next of left to right node
            temp.next = None                # Set the node to remove to None
            self.length -= 1                # Update the length of the LinkedList
       
        return self
    
    def reverse(self):
        """Reverse the LinkedList.
        
        Returns:
            Reversed LinkedList.
        """
        # Check if LinkedList is not empty
        if self.head is not None:
            curr = self.head                    # Start at head and is used to change direction of next
            self.head = self.tail               # Rename tail as head of LinkedList
            self.tail = curr                    # Rename head as tail of LinkedList
            next = curr.next                    # The next node to the current node
            prev = None                         # The previous node to the current node
            
            # We will be working with three variables while iterating through the list 
            for i in range(self.length):
                next = curr.next                # Move next a step forward
                curr.next = prev                # Move the link in the opposite direction 
                prev = curr                     # Move previous node to current position
                curr = next                     # Move current node to next position
        else:
            return
        
        return self
    
    def print(self):
        """Prints the LinkedList in human readable format"""
        # We intialize a string to represent the LinkedList
        linkedListstr = ''
        start = self.head
        
        # Loops till we hit a None
        while start:
            linkedListstr += str(start.data) + ' --> '  # Concatenate the data of the node to our LinkedList string representation
            start = start.next                          # Move to the next node in LinkedList
        
        # Check if LinkedList is empty
        if linkedListstr == '':
            print("LinkedList is empty!")
            print("Length of LinkedList: ", self.length)
        else:
            print(linkedListstr)
            print("Length of LinkedList: ", self.length)

# So let test out the LinkedList Class and its methods
myFirstLinkedList = LinkedList()
myFirstLinkedList.push(3)           
myFirstLinkedList.push([2, 1])
myFirstLinkedList.reverse()
myFirstLinkedList.pop()
myFirstLinkedList.unshift(0)
myFirstLinkedList.shift()
myFirstLinkedList.set(0, 1)
myFirstLinkedList.insert(0, 0)
myFirstLinkedList.remove(1)
print(type(myFirstLinkedList.get(0)))
myFirstLinkedList.print()