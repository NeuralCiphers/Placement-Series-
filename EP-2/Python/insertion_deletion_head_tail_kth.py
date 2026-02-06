class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Insert at Head
def insert_at_head(head, val):
    new_node = Node(val)
    new_node.next = head
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
    temp.next = new_node
    return head

# Delete Head
def delete_head(head):
    if not head:
        print("List is empty!")
        return None
    return head.next

# Delete Tail
def delete_tail(head):
    if not head:
        print("List is empty!")
        return None
    
    if not head.next:
        return None
    
    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None
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
    
    while temp and count < k - 1:
        temp = temp.next
        count += 1
    
    if not temp or not temp.next:
        print("Invalid position!")
        return head
    
    temp.next = temp.next.next
    return head

# Display List
def display(head):
    if not head:
        print("List is empty!")
        return
    
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")

if __name__ == "__main__":
    head = None
    
    # Insert at head
    head = insert_at_head(head, 10)
    head = insert_at_head(head, 20)
    head = insert_at_head(head, 30)
    print("After inserting at head: ", end="")
    display(head)
    
    # Insert at tail
    head = insert_at_tail(head, 5)
    head = insert_at_tail(head, 1)
    print("After inserting at tail: ", end="")
    display(head)
    
    # Insert at Kth position
    head = insert_at_k(head, 3, 25)
    print("After inserting 25 at position 3: ", end="")
    display(head)
    
    # Delete head
    head = delete_head(head)
    print("After deleting head: ", end="")
    display(head)
    
    # Delete tail
    head = delete_tail(head)
    print("After deleting tail: ", end="")
    display(head)
    
    # Delete Kth node
    head = delete_at_k(head, 2)
    print("After deleting node at position 2: ", end="")
    display(head)
