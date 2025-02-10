class Commit:
    def __init__(self, commit_id, message, previous=None):
        self.commit_id = commit_id
        self.message = message 
        self.previous = previous
class Repository:
    def __init__(self):
        self.head = None  
    def commit(self, commit_id, message):
        new_commit = Commit(commit_id, message, self.head)
        self.head = new_commit 
        print(f"Commit {commit_id} created: {message}")
    def log(self):
        current = self.head
        print("\nCommit History:")
        while current:
            print(f"Commit {current.commit_id}: {current.message}")
            current = current.previous 
repo = Repository()
repo.commit(1, "Initial commit")
repo.commit(2, "Added feature A")
repo.commit(3, "Fixed bug in feature A")
repo.log()