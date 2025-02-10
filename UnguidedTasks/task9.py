class Node:
    def __init__(self, file, name):
        self.file = file
        self.name = name 
        self.next = None
class FileSystem:
    def __init__(self):
        self.head = None  
    def file(self, file, name):
        newfile = Node(file, name)
        if self.head is None:
            self.head = newfile
            print(f"file {file} created: {name}")
        else:
            current = self.head
            while current.next:              
                current = current.next
            print(f"file {file} created: {name}")    
            current.next = newfile
    def log(self):
        current = self.head
        print("\nFile Stored:")
        while current:
            print(f"File {current.file}: {current.name}")
            current = current.next 
repo = FileSystem()
repo.file(1, "lab1")
repo.file(2, "lab2")
repo.file(3, "lab3")
repo.log()