from file_handler import FileHandler

class TaskManager:
    def _init_(self):
        self.tasks = FileHandler.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        FileHandler.save_tasks(self.tasks)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            FileHandler.save_tasks(self.tasks)

    def get_tasks(self):
        return self.tasks