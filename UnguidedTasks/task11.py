from datetime import datetime
class Message:
    def __init__(self, text):
        self.text = text  
        self.timestamp = datetime.now()
        self.next = None  
class Chat:
    def __init__(self):
        self.head = None  
    def send_message(self, text):
        new_message = Message(text)
        if self.head is None:
            self.head = new_message 
            print(f"Message sent: {text}")
        else:
            current = self.head
            while current.next:              
                current = current.next
            print(f"Message sent: {text}")
            current.next = new_message
    def display_chat(self):
        current = self.head
        while current:
            print(f"[{current.timestamp}] {current.text}")
            current = current.next
chat = Chat()
chat.send_message("Hello!")
chat.send_message("How are you?")
chat.send_message("I'm doing well!")
print("\nChat History:")
chat.display_chat()