class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    def display_forward(self):
        if not self.head:
            print("Lista jest pusta")
            return
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()
    def display_backward(self):
        if not self.head:
            print("Lista jest pusta")
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.data, end=' ')
            curr = curr.prev
        print()
    def delete(self, data):
        if not self.head:
            print("Lista jest pusta")
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        if not curr:
            print("Nie znaleziono elementu")
            return
        if curr.next:
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next
# Kod testujący
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
print("Wyświetlanie do przodu:")
dll.display_forward()     # 10 20 30
print("Wyświetlanie do tyłu:")
dll.display_backward()    # 30 20 10
dll.delete(20)
print("Po usunięciu 20:")
dll.display_forward()     # 10 30