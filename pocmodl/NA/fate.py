from tasks import task
from logics import logic
from presentation import p1

def fate():
    print("fate")


if __name__ == "__main__":
    fate()
    task1 = task(1,"task1" , "running", "Low", "Windows")
    task2 = task(2, "task2", "completed", "high", "Linux")
    
    lgk = logic()

    taskadd = lgk.add(task1)
    print(task1)
    taskadd = lgk.add(task2)
    print(task2)

    taskadd = lgk.add(task1)

    

    
    