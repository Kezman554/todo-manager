from todo import Task


class TaskManager:
    """Manages a collection of tasks"""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description, priority="Medium"):
        """Add a new task to the list"""
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Added: {task}")
    
    def show_all_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks yet!")
            return
        
        print("\n=== Your To-Do List ===")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    
    def complete_task(self, task_number):
        """Mark a task as complete by its number"""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_complete()
            print(f"Completed: {self.tasks[task_number - 1].description}")
        else:
            print("Invalid task number!")


# Test the TaskManager
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Learn Git", "High")
    manager.add_task("Practice branching", "High")
    manager.add_task("Build a project", "Medium")
    manager.show_all_tasks()
    manager.complete_task(1)
    manager.show_all_tasks()