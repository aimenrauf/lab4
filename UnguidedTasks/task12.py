class User:
    def __init__(self, name):
        self.name = name 
        self.next = None 
        self.connections = [] 
    def add_connection(self, user):
        if user not in self.connections:
            self.connections.append(user)  
            print(f"{self.name} is now connected to {user.name}")
    def show_connections(self):
        print(f"{self.name}'s connections: {[user.name for user in self.connections]}")
class UserProfileSystem:
    def __init__(self):
        self.head = None  
    def add_user(self, name):
        new_user = User(name)
        if not self.head:
            self.head = new_user
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_user
        return new_user
    def display_users(self):
        current = self.head
        while current:
            print(f"User: {current.name}")
            current = current.next
profiles = UserProfileSystem()
alice = profiles.add_user("Alice")
bob = profiles.add_user("Bob")
charlie = profiles.add_user("Charlie")
alice.add_connection(bob)
alice.add_connection(charlie)
bob.add_connection(charlie)
profiles.display_users()
alice.show_connections()
bob.show_connections()
charlie.show_connections()