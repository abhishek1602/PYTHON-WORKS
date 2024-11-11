class logic:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        for tsk in self.tasks:
            if tsk.taskId == task.taskId:
                print("Task already there or not found")
                return False
        self.tasks.append(task)
        print("Task added")
        return True
            