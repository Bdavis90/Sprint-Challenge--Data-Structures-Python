from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.storage = DoublyLinkedList()
        self.capacity = capacity
        self.head = None

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.head = self.storage.head
        else:
            if not self.head.next:
                self.head.value = item
                self.head = self.storage.head
            else:
                self.head.value = item
                self.head = self.head.next

    def get(self):
        items = []
        head = self.storage.head
        while head:
            items.append(head.value)
            head = head.next
        return items