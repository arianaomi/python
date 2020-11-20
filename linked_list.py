"""
    Linear data structure, consist of 2 parts : 1- Data 2- Reference ti the next node

    We can be added a new node in three different manners:
    1- At the front of the link list
    2- After a given node
    3- At the end of the linked list
"""

class Node:
    def __init__(self,data): # Constructor
      self.data = data # Data 
      self.next = None # Initialize next as Null

class LinkedList: 
    def __init__(self):
        self.head = None 

    def print_list(self): # Method to print elements of linked list
        if self.head is None:
            print('It has no elements')
            return
        else :
            n = self.head
            while (n):
                print(n.data)
                n = n.next
    
    def insert_at_start (self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_item(self, prev_node,new_data):
        if prev_node is None:
            print('The given previous node must in linked list')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node



if __name__=='__main__':
    linked_list = LinkedList()
    linked_list.head = Node('Monday') # Create a new node
    second_day = Node('Tuesday')
    fourth_day = Node('Thursday')

    linked_list.head.next = second_day # Link first node with second
    second_day.next = fourth_day #Link second node with fourth

    # insert elements
    linked_list.insert_at_start('Sunday') 
    linked_list.insert_after_item(second_day,'Wednesday')
    linked_list.insert_at_end('Friday')
    linked_list.print_list()