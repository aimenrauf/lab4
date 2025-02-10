class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Navigation:
    def __init__(self):
        self.head = None
    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def navigate(self):
        number=0
        current = self.head
        while current:
            number+=1
            print(f"search # {number}: {current.data}")
            current = current.next
        print("No more searches!")
pat = Navigation()
pat.append("What is java")
pat.append("WHat is python")
pat.append("I love link List")
pat.navigate()