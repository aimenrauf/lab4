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
    def display(self):
        """Print all element of the list"""
        current = self.head
        while current:
            print(current.data, end = "\n")
            current= current.next
        print("None")
sll = SinglyLinked()
for song in ["song1", "song2", "song3", "song4"]:
    sll.append(song)
sll.display()