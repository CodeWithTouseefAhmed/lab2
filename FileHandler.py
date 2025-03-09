class FileHandler:
    FILE_NAME = "tasks.txt"

    @staticmethod
    def save_tasks(tasks):
        with open(FileHandler.FILE_NAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")

    @staticmethod
    def load_tasks():
        try:
            with open(FileHandler.FILE_NAME, "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []