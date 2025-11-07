class Task:
    """Represents a single task"""
    
    def __init__(self, description, priority="Medium"):
        self.description = description
        self.priority = priority
        self.completed = False
    
    def mark_complete(self):
        """Mark this task as completed"""
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.description} (Priority: {self.priority})"


# Test the class
if __name__ == "__main__":
    task1 = Task("Learn Git branching", "High")
    print(task1)
    task1.mark_complete()
    print(task1)