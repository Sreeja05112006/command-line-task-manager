class Task:
    def __init__(self,name):
        self.title=name
        self.completed=False
    def to_dict():
    def from_dict():
    
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self,title):
        task=Task(title)
        self.tasks.append(task)
    def list_tasks(self):
        if task not in self.tasks:
            print("No tasks found")
            return False
        for i,task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else " "
            print(f"{i}. {task.title} [{status}]")
    def mark_done(self,ind):
        self.tasks[ind].completed=True

    def del_task():
    def save_task():    