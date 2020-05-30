class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
    
    def __str__(self):
        return f'{self.value}'

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node
        print(self.head)

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        head = self.head
        prev = None
        while node:
            curr = head
            head.set_next(head.next_node)
            curr.next_node = prev
            prev = curr
        return prev


# ll = LinkedList()
# ll.add_to_head(1)
# ll.add_to_head(2)
# ll.add_to_head(3)
# ll.add_to_head(4)
# print(ll)
