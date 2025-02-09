class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinked:
    def __init__(self):
        self.head = None
    def append(self,data):
        """Append the new Note at the end of List """
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def delete(self,data):
        """Delete the node from the linked list"""
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
            previous = current
            current = current.next
    def display(self):
        """Print all element of the list"""
        current = self.head
        while current:
            print(current.data, end = "-> ")
            current= current.next
        print("None")
    
sll = SinglyLinked()
sll.append("Aimen Rauf")
sll.append("ABdul Haseeb")
sll.append("Sadia Rauf")
sll.display()
sll.delete("Sadia Rauf")
sll.display()