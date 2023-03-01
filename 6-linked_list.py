"""Linked List Module

This module implements the linkedlist data structure by creating the basic building block (Nodes) and (LinkedList) as classes.
"""

class Node:
    """Node class"""
    def __init__(self, data=None, next=None):                                               # Constructor for the Node class
        """Used to create node objects. It's called during object instantiation
        
        args:
            (optional) data: What you want to store
            (optional) next: The addres of the next node
        """
        self.data = data                                                                    # data is a property of the class Node
        self.next = next                                                                    # next is a property of the class Node

class LinkedList:
    """LinkedList class"""
    def __init__(self, data=None):                                                          # Constructor for the LinkedList class
        """Used to create a linkedlist object. It's called during object instantiation
        
        args:
            (optional) data: What you want to store
        """
        self.head = None                                                # head is a property of the class LinkedList
        self.tail = None                                                # tail is a property of the class LinkedList
        
        if data == None:                                                # check if the linked list was initialized with an argument then update the length ...
            self.length = 0                                             # ... property of the LinkedList
        else:
            newNode = Node(data)                                        # Instantiate a node class
            self.head = newNode                                         # Assign the node as head of linkedlist
            self.tail = newNode                                         # Assign the node as tail of linkedlist
            self.length = 1                                             # Update the length property of the linkedlist
    
    def push(self, data):                                                                   # Insert_at_end method of the LinkedList objects
        """Inserts data at end of linkedlist object
        
        args:
            data: What you want to store
        
        Returns: Updated linkedlist
        """
        newNode = Node(data)                                                                # Instantiate a node class
        if self.head is None:                                                               # checks if head of linkedlist is empty
            self.head = newNode                                                             # Assign the node as head of linkedlist
            self.tail = newNode                                                             # Assign the node as tail of linkedlist
        else:
            self.tail.next = newNode                                                        # Assign the new node to the next property of previous node in linkedlist
            self.tail = newNode                                                             # Assign the new node as tail of the linkedlist
        self.length += 1                                                                    # Update the length property of the linkedlist
        return self                                                                         # Return updated linkedlist
    
    def pop(self):                                                                          # Remove_at_end method of the LinkedList objects
        """Remove data from end of linkedlist object
        
        Returns: Updated linkedlist
        """
        if self.head is None:                                                               # check if linkedlist is empty
            print("No more Nodes to remove")
            return
        
        # We need to transverse through the linked list by checking each individual node at a time and omiting the last node in the linkedlist
        checknode = self.head                                                               # So we start with the head node of the linkedlist
        currentnode = self.head
        while checknode.next:                                                               # While the check node is not the last node
            currentnode = checknode                                                         # Assign checknode as currentnode
            checknode = checknode.next                                                      # Assign the next node as the new checknode
        else:                                                                               # When we finally get to the last node we omit it by not assigning it to the current node and then ...
            self.tail = currentnode                                                         # ... assign currentnode as tail of linkedlist
            self.tail.next = None                                                           # Set it's next to None. This now serves as our last node
            self.length -= 1                                                                # Update the length of the linkedlist
            if self.length == 0:                                                            # To avoid negative length ...
                self.head = None                                                            # ... stop this method from executing by setting head to zero
        return currentnode                                                                  # Return updated linkedlist
    
    def unshift(self, data):                                                                # Insert_at_beginning method of the LinkedList objects
        """Insert data at beginning of linkedlist object
        
        args:
            data: What you want to store
        
        Returns: Updated linkedlist
        """
        newNode = Node(data)                                                                # Instantiate a node class
        if self.head is None:                                                               # checks if head of linkedlist is empty
            self.head = newNode                                                             # Assign the node as head of linkedlist
            self.tail = newNode                                                             # Assign the node as tail of linkedlist
        else:
            newNode.next= self.head                                                         # Assign head of linkedlist to the next property of new node node
            self.head = newNode                                                             # Assign the new node as head of the linkedlist
        self.length += 1                                                                    # Update the length property of the linkedlist
        return self                                                                         # Return updated linkedlist
    
    def shift(self):                                                                        # Remove_at_beginning method of the LinkedList objects
        """Remove data from beginning of linkedlist object
        
        Returns: Updated linkedlist
        """
        if self.head is None:                                                               # check if linkedlist is empty
            print("No more Nodes to remove")
            return

        # We employ the use a dummy variable to set the first node in linkedlist to None
        currentnode = self.head                                                             # So we start by saving the current node at the head of the linkedlist in a dummy variable
        self.head = currentnode.next                                                        # Then set the head of the linkedlist to the next property of the dummy variable
        currentnode.next = None                                                             # Then set the next property of the dummy variable to None
        self.length -= 1                                                                    # Update the length of the linkedlist
        return self                                                                         # Return updated linkedlist
    
    def get(self, index):                                                                   # Get method of the LinkedList objects
        """Gets node at given index of linkedlist object
        
        args:
            index: Index of node
        
        Returns: The Node at given index
        """
        if index < 0 or index >= self.length:                                               # Checks for negative indexing and overflow(non-exixting indexes)
            return None

        # Iterate through the linkedlist to return the required node
        currentnode = self.head                                                             # Start from the head of linkedlist
        for i in range(index):                                                              # Loop through the range up until but not including the index
            currentnode = currentnode.next                                                  # Set the the currentnode foreach iteration to a dummmy variable
        # print(currentnode.data)
        return currentnode                                                                  # Return the required node

    def set(self, index, data):                                                             # Set method of the LinkedList objects
        """Sets data into the data attribute of a given node index
        
        args:
            index: Index of target node
            data: What you want to store
        
        Returns: Updated linkedlist
        """
        if index < 0 or index >= self.length:                                               # Checks for negative indexing and overflow(non-exixting indexes)
            return None
        
        node = self.get(index)                                                              # Gets the node we want to insert data in
        node.data = data                                                                    # Calls the data attribute of node and assign the data value to it
        return self                                                                         # Return updated linkedlist
    
    def insert(self, index, data):                                                          # Insert method of the LinkedList objects
        """Insert a new node with data in front of the node of the given index
        
        args:
            index: Index of target node
            data: What you want to store
        
        Returns: Updated linkedlist
        """
        newNode=Node(data)                                                                  # Create New node with data that you want to insert in linkedlist
        previousNode = self.get(index-1)                                                    # Get the node in front of the node of the given index
        tempNode = previousNode.next                                                        # Set the next value to a temporary variable
        previousNode.next = newNode                                                         # Set the new node to the next value
        newNode.next = tempNode                                                             # Set the next value of the new node to the temporary variable
        self.length +=1                                                                     # Update the length of the linkedlist
        return self                                                                         # Return updated linkedlist
    
    def remove(self, index):                                                                # Remove method of the LinkedList objects
        """Removes node object at a given index
        
        args:
            index: Index of target node
        
        Returns: Updated linkedlist
        """
        if index < 0 or index >= self.length:                                               # Checks for negative indexing and overflow(non-exixting indexes)
            return None
        
        # So we need to know the previous node to be able to remove a node except in the case where index is 0
        if index == 0:
            currentnode = self.head
            self.head = currentnode.next
            currentnode.next = None
            self.length -=1
        else:
            previousNode = self.get(index-1)
            currentnode = self.get(index)
            previousNode.next = currentnode.next
            self.length -=1
        return self
    
    def print(self):                                                                        # Utility function to view the linkedlist as output
        """Prints the linkedlist object in human readable format"""
        if self.head is None:
            print("Linked List is empty")
            # print(self.length)
            return

        # We need to transverse through the linked list by checking each individual node data at a time and printing it out from the linkedlist
        currentnode = self.head                                                             # So we start with the head node of the linkedlist
        linkedListstr = ''                                                                  # We intialize a string to represent the linkedlist
        while currentnode:                                                                  # Loops till we hit a None
            linkedListstr += str(currentnode.data) + ' --> '                                # Concatenate the data of the node to our linkedlist string representation
            currentnode = currentnode.next                                                  # Move to the next node in linkedlist
        print(linkedListstr)                                                                # Print out final string representation of linkedlist
        # print(self.length)


# So let test out the linkedlist
myLinkedList = LinkedList()
myLinkedList.push(1)
myLinkedList.push(2)
myLinkedList.pop()

# myLinkedList.pop()
# myLinkedList.pop()

myLinkedList.unshift(9)
myLinkedList.unshift(8)
myLinkedList.shift()

# myLinkedList.shift()
# myLinkedList.shift()
# myLinkedList.shift()

myLinkedList.set(1, 5)
myLinkedList.insert(1, 3)
myLinkedList.remove(1)

myLinkedList.print()

myLinkedList.get(1)
