#Ongoing taskStatus


#QUESTION: CREATE A LIST WITH DICTIONARY AS ELEMENTS AND CREATE A MENU WITH FUNCTIONS:
#ADD TASK, UPDATE TASK, REMOVE TASK, PRINT ALL TASK AND EXIT

tasks = []

def addTask(taskId, status):
    task = {"taskId": taskId, "status": status}
    tasks.append(task)
    print(f"New task added with taskId: {taskId}, status: {status}")

def updateTask(taskId, newStatus):
    for task in tasks:
        if task["taskId"] == taskId:
            task["status"] = newStatus
            print(f"Status of Task: {taskId} changed to: {newStatus}")
            return
    print("Tasks not found")

def removeTasks(taskId):
    for task in tasks:
        if task["taskId"] == taskId:
            tasks.remove(task)
            print(f"The task: {taskId} has been removed successfully")
            return
    print("Task not found")

def runningTask():
        runningTask = [task for task in tasks if task["status"]=="running"]
        if runningTask:
            for task in runningTask:
                print(f"running Tasks: \nTaskId: {task['taskId']}, Status: {task['status']}")
                return
        print("Task not found")

def completedTask():
        runningTask = [task for task in tasks if task["status"]=="completed"]
        if runningTask:
            for task in runningTask:
                print(f"completed Tasks: \nTaskId: {task['taskId']}, Status: {task['status']}")
                return
        print("Task not found")

while True:

    print("\nOptions:")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Remove Task")
    print("4. Print running Tasks")
    print("5. Print Completed Tasks")
    print("6. Exit")

    choice = input("Choose An Option (1-6): ")

    if choice == '1':
        taskId = int(input("Enter Task Id: "))
        status = input("Enter the status of the Task (running or completed): ")
        addTask(taskId,status)

    elif choice == '2':
        taskId = int(input("Enter the Task Id: "))
        newStatus = input("Running Or Completed?: ")
        updateTask(taskId,newStatus)

    elif choice == '3':
        taskId = int(input("Enter the Task Id to remove the task: "))
        removeTasks(taskId)

    elif choice == '4':
        runningTask()

    elif choice == '5':
        completedTask()

    elif choice == '6':
        break

    else:
        print("Invalid Option")
