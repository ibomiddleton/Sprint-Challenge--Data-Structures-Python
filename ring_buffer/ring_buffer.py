import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        head = self.storage.head
        tail = self.storage.tail

        if self.storage.length >= self.capacity:
            if self.current is tail:
                self.current = head
                head.value = item
            else:
                self.current.next.value = item
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        list_buffer_contents = []
        current_head = self.storage.head
        for i in range(0, self.storage.length):
            list_buffer_contents.append(current_head.value)
            current_head = current_head.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
