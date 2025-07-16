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


    # NOTE:(Function 1) Append Item to the end of the linked list
    def append(self, value):
        node_to_append = Node(value)
        if self.head is None:
            self.head = node_to_append
            self.tail = node_to_append
            self.length = 1
        else:
            self.tail.next = node_to_append
            self.tail = node_to_append
            self.length += 1


    # NOTE:(Function 3)  Pop Last element from the linked list
    def pop(self):
        if self.length == 0:
            return None

        else:
            pre = self.head
            temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value

    # NOTE:(Function 4)  add item at the beginning of linked list
    def prepend(self, value):
        node_to_append = Node(value)
        if self.length == 0:
            self.head = node_to_append
            self.tail = node_to_append
        else:
            node_to_append.next = self.head
            self.head = node_to_append
        self.length += 1

    # NOTE:(Function 5)  Pop the first item from linked list
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            poped_node = self.head
            self.head = self.head.next
            poped_node.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return poped_node

    # NOTE:(Function 6) Get element at index
    def get(self, index):
        if index >= self.length or index < 0:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    # NOTE: (Function 7) Set element in index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # NOTE: (Function 8) insert new Node
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    # NOTE: (Function 9) Remove Node in an index from the linked List
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp
    
    # NOTE: (Function 10) Reverse linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    # NOTE:(Function 2) Print Linked List Elements
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

mine = LinkedList(5)
mine.append(10)
print(mine.get(3))