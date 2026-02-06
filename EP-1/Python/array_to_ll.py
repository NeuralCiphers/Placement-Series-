class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arr_to_ll(arr):
    """Convert array to linked list"""
    if not arr:
        return None
    
    head = Node(arr[0])
    mover = head
    
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    
    return head

def print_ll(head):
    """Print linked list and return count"""
    temp = head
    cnt = 0
    while temp:
        cnt += 1
        print(temp.data, end=" ")
        temp = temp.next
    return cnt

if __name__ == "__main__":
    arr = [12, 13, 1, 3, 5]
    head = arr_to_ll(arr)
    cnt = print_ll(head)
    print(f"\nTotal number of nodes: {cnt}")
