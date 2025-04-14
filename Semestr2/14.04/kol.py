class PatientNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class PatientQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_patient(self, name):
        new_patient = PatientNode(name)
        if not self.head:
            self.head = self.tail = new_patient
        else:
            self.tail.next = new_patient
            self.tail = new_patient

    def serve_patient(self):
        if not self.head:
            print("Kolejka jest pusta")
            return None
        served = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return served.name

    def show_queue(self):
        if not self.head:
            print("Kolejka jest pusta")
            return
        current = self.head
        while current:
            print(f"> {current.name}")
            current = current.next

queue = PatientQueue()
queue.add_patient("test 1")
queue.add_patient("test 2")
queue.add_patient("test 3")
print("\nKolejka:")
queue.show_queue()

served = queue.serve_patient()
if served: print(f"\nObsłużono: {served}")

print("\nKolejka:")
queue.show_queue()