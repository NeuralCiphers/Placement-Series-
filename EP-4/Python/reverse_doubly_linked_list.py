class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

# Method 1: By Swapping Next and Prev Pointers
def reverse_dll(head):
    if not head or not head.next:
        return head
    
    curr = head
    temp = None
    
    while curr:
        # Swap prev and next pointers
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        
        # Move to next node (which is now prev due to swap)
        curr = curr.prev
    
    # temp.prev is the new head (last node we processed)
    if temp:
        head = temp.prev
    
    return head

# Method 2: Recursive Approach
def reverse_dll_recursive(head):
    if not head or not head.next:
        return head
    
    new_head = reverse_dll_recursive(head.next)
    
    head.next.next = head
    head.prev = head.next
    head.next = None
    
    return new_head

# Insert at Tail (Helper function for testing)
def insert_at_tail(head, val):
    new_node = Node(val)
    
    if not head:
        return new_node
    
    temp = head
    while temp.next:
        temp = temp.next
    
    temp.next = new_node
    new_node.prev = temp
    return head

# Display List
def display(head):
    if not head:
        print("List is empty!")
        return
    
    temp = head
    print("NULL <-> ", end="")
    while temp:
        print(f"{temp.data} <-> ", end="")
        temp = temp.next
    print("NULL")

if __name__ == "__main__":
    head = None
    
    # Create a doubly linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5
    head = insert_at_tail(head, 1)
    head = insert_at_tail(head, 2)
    head = insert_at_tail(head, 3)
    head = insert_at_tail(head, 4)
    head = insert_at_tail(head, 5)
    
    print("Original List: ", end="")
    display(head)
    
    # Reverse the list
    head = reverse_dll(head)
    
    print("Reversed List: ", end="")
    display(head)
    
    # Reverse again to get original
    head = reverse_dll(head)
    
    print("Reversed Again: ", end="")
    display(head)
