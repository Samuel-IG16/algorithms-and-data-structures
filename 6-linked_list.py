"""Linked List Module

This module implements the likedlist data structure by creating the basic building block (Nodes) and (LinkedList) as classes.
"""

class Node:
    """Node class"""
    def __init__(self, data=None, next=None):                                               # Constructor for the Node class
        """Used to create node objects. It's called during object instantiation
        
        args:
            (optional) data - What you want to store
            (optional) next - The addres of the next node
        """
        self.data = data                                                                    # data is a property of the class Node
        self.next = next                                                                    # next is a property of the class Node

class LinkedList:
    """LinkedList class"""
    def __init__(self, data=None):                                                          # Constructor for the LinkedList class
        """Used to create a linkedlist object. It's called during object instantiation
        
        args:
            (optional) data - What you want to store
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
    
    def insert_at_end(self, data):                                                          # Insert method of the LinkedList objects
        """Inserts data to the end of linkedlist object
        
        args:
            data - What you want to store
        
        Returns: Updated linkedlist
        """
        newNode = Node(data)                                                                # Instantiate a node class
        if self.head is None:                                                               # checks if head of linkedlist is empty
            self.head = newNode                                                             # Assign the node as head of linkedlist
            self.tail = newNode                                                             # Assign the node as tail of linkedlist
        else:
            self.tail.next = newNode                                                        # Assign the new node to the next property of previous node
            self.tail = newNode                                                             # Assign the new node as tail of the linkedlist
        self.length += 1                                                                    # Update the length property of the linkedlist
        return self                                                                         # Return updated linkedlist
    
    def remove_at_end(self):                                                                # Pop method of the LinkedList objects
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
        return currentnode
    
    def print(self):                                                                        # Utility function to view the linkedlist as output
        """Prints the linkedlist object in human readable format"""
        if self.head is None:
            print("Linked List is empty")
            # print(self.length)
            return
        
        currentnode = self.head
        linkedListstr = ''
        while currentnode:
            linkedListstr += str(currentnode.data) + ' --> '
            currentnode = currentnode.next
        print(linkedListstr)
        # print(self.length)

myLinkedList = LinkedList()
myLinkedList.insert_at_end(1)
myLinkedList.insert_at_end(2)
#myLinkedList.insert_at_end(3)
#myLinkedList.insert_at_end(4)
# myLinkedList.remove_at_end()
# myLinkedList.remove_at_end()
# myLinkedList.remove_at_end()
# myLinkedList.remove_at_end()
# myLinkedList.remove_at_end()
myLinkedList.print()