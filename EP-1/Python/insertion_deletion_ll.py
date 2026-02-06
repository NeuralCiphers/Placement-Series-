class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Insertion:
    
    def insert_at_head(self, head, data):
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    def insert_at_tail(self, head, data):
        new_node = Node(data)
        if not head:
            return new_node
        
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return head
    
    def insert_at_kth_pos(self, head, k, data):
        new_node = Node(data)
        if k == 1:
            return self.insert_at_head(head, data)
        
        temp = head
        prev = None
        while temp and k > 1:
            k -= 1
            prev = temp
            temp = temp.next
        
        prev.next = new_node
        new_node.next = temp
        return head
    
    def arr_to_ll(self, arr):
        if not arr:
            return None
        
        head = Node(arr[0])
        mover = head
        
        for i in range(1, len(arr)):
            temp = Node(arr[i])
            mover.next = temp
            mover = temp
        
        return head
    
    def print_ll(self, head):
        temp = head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

class Deletion:
    
    def delete_head(self, head):
        if not head:
            return None
        return head.next
    
    def delete_tail(self, head):
        if not head or not head.next:
            return None
        
        temp = head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return head

if __name__ == "__main__":
    arr = [12, 13, 1, 3, 5]
    it = Insertion()
    head = it.arr_to_ll(arr)
    
    head = it.insert_at_head(head, 5)
    it.print_ll(head)
    print()
    
    head = it.insert_at_tail(head, 10)
    it.print_ll(head)
    print()
    
    head = it.insert_at_kth_pos(head, 3, 45)
    it.print_ll(head)
    print()
    
    dt = Deletion()
    head = dt.delete_head(head)
    it.print_ll(head)
    print()
    
    head = dt.delete_tail(head)
    it.print_ll(head)
