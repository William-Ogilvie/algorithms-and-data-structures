"""
Linked Lists
--------------
Sequence of nodes, each node stores data and a reference (pointer) to the next node.
Elts are not stored in continous memory as connected by pointers.

Three key types:

Singly linked list: Each node has one pointer to the next node
Doubly linked list: each node has two pointers, one to the next and one to the previous node
Circular linked list: the last node's pointer links back to the head node

The head node is the first node in the list, this is how you would access the list through the head pointer.
Sometimes you can also have a tail pointer that points to the end of the list as well.

Basic operations:

Access by index: (get(k))
Time complexity = O(n), must traverse list sequentially

Insert at head: (prepend(x))
Time complexity = O(1), just relink head pointer

Insert at tail: (append(x))
Time complexity = O(1) if tail pointer kept, else O(n)

Insert at index: (insert(k,x))
Time complexity = O(n), need to traverse to k-1th node

Delete head: (delete_head())
Time complexity = O(1), update head pointer

Delete tail: (delete_tail)
Time complexity = O(n), must traverse to (n-1)th node

Delete at index: (delete(k))
Time complexity = O(n), need to find node and relink

Search (by value): (find(x))
Time complexity = O(n), traverse until found

Reverse list: (reverse())
Time complexity = O(n), Iterative pointer manipulation

Length: (length())
Time complexity = O(n), unless stored as property
"""


class Node:
    def __init__(self, value):
        self.value = value # data
        self.next = None # pointer

# Singly linked list example
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        # Pointer
        p = self.head

        # Essentially we loop through whilst p.next is not None (i.e. not at the end of the list)
        while p.next != None:
            p = p.next # move pointer one down the list

        # Append to end of list 
        p.next = new_node
    
    def prepend(self, value):
        new_node = Node(value)

        # Set new node to point to current head
        new_node.next = self.head

        # Set head to point to new node
        self.head = new_node
    
    def delete_at_index(self, index):
        # Handle empty list
        if not self.head:
            return

        if index == 0:
            # Update head node
            self.head = self.head.next
            return

        # ptr 
        p = self.head

        # Current index
        i = 0

        # Traverse to the node before the target
        while p.next and i < index - 1: 
            i += 1
            p = p.next

        # Check if index is out of bounds
        if not p.next:
            raise IndexError(f"Index {index} out of bounds")

        # Skip the node to delete
        p.next = p.next.next


    def print_list(self):
        p = self.head

        # Need to do while p != None so we print the last node, otherwise we get to the last node but don't print
        while p != None:
            print(p.value)
            p = p.next

linked_list = LinkedList()

linked_list.append(3)
linked_list.append(4)
linked_list.append(1)
linked_list.append(5)

linked_list.delete_at_index(0) # delete 3, this is the same as deleted head as O(1)
linked_list.prepend(7)
linked_list.delete_at_index(1) # should delete 4
#linked_list.delete_at_index(10) # should throw index error

linked_list.print_list()