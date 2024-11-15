class task:

    def __init__(self, taskId, taskName, status, priority, location):
        self.taskId = taskId
        self.taskName = taskName
        self.status = status
        self.priority = priority
        self.location = location

    def __str__(self):
        return f"TaskId : {self.taskId} \nTask Name : {self.taskName} \nStatus : {self.status} \nPriority : {self.priority} \nLocation : {self.location}"
        
    