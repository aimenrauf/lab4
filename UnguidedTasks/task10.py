class Node:
    def __init__(self,rate,type):
        self.rate = rate
        self.type = type
        self.next = None
class Movies:
    def __init__(self):
        self.head = None
    def append(self, rate,type):
        node = Node(rate,type)
        if self.head is None:
            self.head = node
            print(f"Rating: {rate}, Type: {type}")
        else:
            current = self.head
            while current.next:
                current = current.next
            print(f"Rating: {rate}, Type: {type}")
            current.next = node
    def movie(self,rate):
        current = self.head
        while current:
            if current.rate == rate:
                if current.type == "Action":
                    print(f"Suggestions:\n1. The Union\n2. Mad Max\n3. Heart of Stone") 
                elif current.type == "Intelligence":
                    print(f"Suggestions:\n1. Intersteller\n2. The Imitation Game\n3. Spy") 
                elif current.type == "Horror":
                    print(f"Suggestions:\n1. The Mummy\n2. Stranger things\n3. FInal Detination")
            current = current.next
mov  = Movies()
mov.append(1, "Intelligence")
mov.append(2,"Action")
mov.append(3,"Horror")
mov.movie(2)
         
