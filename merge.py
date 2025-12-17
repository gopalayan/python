class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def merge_sort(head):
    if not head or not head.next:
        return head

    # Split the list into halves
    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    # Recursively sort the sublists
    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    # Merge the sorted halves
    sorted_list = merge(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result

# Example usage
if __name__ == "__main__":
    llist = LinkedList()
    llist.add(15)
    llist.add(10)
    llist.add(5)
    llist.add(20)
    llist.add(3)
    llist.add(2)

    print("Original List:")
    llist.print_list()

    llist.head = merge_sort(llist.head)

    print("Sorted List:")
    llist.print_list()
