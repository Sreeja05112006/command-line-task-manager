import json
class Task:
    def __init__(self,name):
        self.title=name
        self.completed=False
    def to_dict(self):
        return {
            "title":self.title,
            "completed":self.completed
        }    
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
    def del_task(self,ind):
        del self.tasks[ind]
    def save_tasks(self):
        data=[]
        for task in self.tasks:
            data.append(task.to_dict())
        with open("tasks.json","w")as file:
            json.dump(data,file,indent=4)
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)

                for item in data:
                    task = Task(item["title"])
                    task.completed = item["completed"]
                    self.tasks.append(task)

        except FileNotFoundError:
            pass