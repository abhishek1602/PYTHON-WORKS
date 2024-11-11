from tasks import task
from logics import logic


def fate():
    print("fate")


if __name__ == "__main__":
    fate()
    task3 = task(3,"task3" , "running", "low", "windows")
    task4 = task(4, "task4", "completed", "high", "linux")
    task1 = task(1, "task1","completed", "low", "windows")
    task2 = task(2, "task2","running", "low", "linux")


    lgk = logic()
    sortById = lgk.sortById()

    taskadd = lgk.add(task3)
    taskadd = lgk.add(task4)
    taskadd = lgk.add(task1)
    taskadd = lgk.add(task2)

    sortById = lgk.sortById()

    print("\nSorted By Id:")
    for task in sortById:
        print(f"Task Id: {task.taskId} Name: {task.taskName}")


    filterByWindowsLocation = lgk.FilterByWindowsLocation()

    print("\nFiltered By Location: Windows")
    for task in filterByWindowsLocation:
        print(f"Task Running on windows: {task.taskId} Name: {task.taskName}")


    filterByLinuxLocation = lgk.FilterByLinuxLocation()

    print("\nFiltered By Location: Linux")
    for task in filterByLinuxLocation:
        print(f"Task Running on linux: {task.taskId} Name: {task.taskName}")

    

    

    





    

    

    
    