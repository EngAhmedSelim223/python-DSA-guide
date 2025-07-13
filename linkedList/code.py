# STEP 1: Create Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return f"Node(value = {self.value})"

# STEP 2: Create Linked List Class
class LinkedList:
    # Linked List Constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
        
        
        
    # Print Linked List Elements
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
mine = LinkedList(5)
mine.print_list()
