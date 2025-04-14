class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
                current.next = new_node
    
    def display(self):
        if self.head is None:
            print("Lista jest pusta")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
    
    def delete(self, data):
        if self.head is None:
            print("Lista jest pusta")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        
        print(f"Węzeł z wartością {data} nie istnieje w liście.")


# Tworzymy nową listę
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.display()

ll.delete(20)
ll.display()

ll.delete(10)
ll.display()

ll.delete(100)
