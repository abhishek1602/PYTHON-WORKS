class logic:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        for tsk in self.tasks:
            if tsk.taskId == task.taskId:
                print("Task already there or not found")
                return False
        self.tasks.append(task)
        print(f"Task added: {task.taskId} Name: {task.taskName}")
        return True
    
    def sortById(self):
        sortedTaskId = sorted(self.tasks, key=lambda task: task.taskName)
        return(sortedTaskId)
    
    def FilterByWindowsLocation(self):
        LocationTasks = filter(lambda task : task.location == "windows", self.tasks)
        return(LocationTasks)
    
    def FilterByLinuxLocation(self):
        LocationLinuxTasks = filter(lambda task : task.location == "linux", self.tasks)
        return(LocationLinuxTasks)
    

            