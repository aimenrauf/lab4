class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinkedList:
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
    def search(self,data):
        current = self.head
        
        while current:
            if current.data == data:
                print(f"\nSearch Contact: {current.data}")
            current = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data, end= "->")
            current = current.next
class ContactList:
    def __init__(self):
        self.contacts = SinglyLinkedList() 
    def add_task(self, name):
        self.contacts.append(name)
    def search_task(self, name):
        self.contacts.search(name)
    def show_tasks(self):
        self.contacts.display()
contact = ContactList()
contact.add_task("Aimen Rauf")
contact.add_task("Abdul Haseeb")
contact.add_task("Sadia Rauf")
contact.show_tasks()
contact.search_task("Sadia Rauf")
