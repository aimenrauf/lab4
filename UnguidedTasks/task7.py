class Node:
    def __init__(self,patient):
        self.patient = patient
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
    def append(self,patient):
        patient = Node(patient)
        if self.head is None:
            self.head = patient
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = patient
    def treat(self):
        number = 0
        current = self.head
        while current:
            number+=1
            print(f"Patient # {number}: {current.patient}")
            current = current.next
        print("All patients are treated!")
pat = Queue()
pat.append("Aimen")
pat.append("Haseeb")
pat.append("Sadia")
pat.treat()