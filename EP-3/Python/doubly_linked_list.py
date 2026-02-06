class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

# Convert Array to Doubly Linked List
def array_to_dll(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    prev_node = head
    
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        prev_node.next = temp
        temp.prev = prev_node
        prev_node = temp
    
    return head

# Insert at Head
def insert_at_head(head, val):
    new_node = Node(val)
    
    if not head:
        return new_node
    
    new_node.next = head
    head.prev = new_node
    return new_node

# Insert at Tail
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

# Insert at Kth Position (1-indexed)
def insert_at_k(head, k, val):
    if k == 1:
        return insert_at_head(head, val)
    
    new_node = Node(val)
    temp = head
    count = 1
    
    while temp and count < k - 1:
        temp = temp.next
        count += 1
    
    if not temp:
        print("Invalid position!")
        return head
    
    new_node.next = temp.next
    new_node.prev = temp
    
    if temp.next:
        temp.next.prev = new_node
    temp.next = new_node
    
    return head

# Delete Head
def delete_head(head):
    if not head:
        print("List is empty!")
        return None
    
    if not head.next:
        return None
    
    head = head.next
    head.prev = None
    return head

# Delete Tail
def delete_tail(head):
    if not head:
        print("List is empty!")
        return None
    
    if not head.next:
        return None
    
    temp = head
    while temp.next:
        temp = temp.next
    
    temp.prev.next = None
    return head

# Delete Kth Node (1-indexed)
def delete_at_k(head, k):
    if not head:
        print("List is empty!")
        return None
    
    if k == 1:
        return delete_head(head)
    
    temp = head
    count = 1
    
    while temp and count < k:
        temp = temp.next
        count += 1
    
    if not temp:
        print("Invalid position!")
        return head
    
    if temp.next:
        temp.next.prev = temp.prev
    
    if temp.prev:
        temp.prev.next = temp.next
    
    return head

# Display List
def display(head):
    if not head:
        print("List is empty!")
        return
    
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("NULL")

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    head = array_to_dll(arr)
    
    print("Initial DLL from array: ", end="")
    display(head)
    
    head = insert_at_head(head, 5)
    print("After inserting at head: ", end="")
    display(head)
    
    head = insert_at_tail(head, 60)
    print("After inserting at tail: ", end="")
    display(head)
    
    head = insert_at_k(head, 3, 15)
    print("After inserting 15 at position 3: ", end="")
    display(head)
    
    head = delete_head(head)
    print("After deleting head: ", end="")
    display(head)
    
    head = delete_tail(head)
    print("After deleting tail: ", end="")
    display(head)
    
    head = delete_at_k(head, 2)
    print("After deleting node at position 2: ", end="")
    display(head)
