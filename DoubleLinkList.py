
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def addAtFront(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def addAtEnd(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def removeFromFront(self):
        if not self.head:
            return None
        removed_data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return removed_data

    def removeFromEnd(self):
        if not self.tail:
            return None
        removed_data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return removed_data

    def print(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("<->".join(map(str, elements)))

    def size(self):
        return self._size

if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.addAtFront(10)
    dll.addAtEnd(20)
    dll.addAtFront(5)
    dll.print()
    print("Size:", dll.size())
    print("Removed from front:", dll.removeFromFront())
    dll.print()
    print("Removed from end:", dll.removeFromEnd())
    dll.print()
    print("Size:", dll.size())
