# An empty list to store tasks
li_task=[]
# Function to display list of tasks
def display_list():
    if len(li_tasks)==0:
        print("your list of tasks is empty")
    else:
        for i in li_task:
            task=li_task(i)
            if task["completed"]:
                status="Done"
            else:
                status="not done yet"
            print(li_tasks(i),":",status)                    
# Function to add task in list of tasks
def add_task(task_tobeadded):
    task = {"task": task_tobeadded, "completed": False}
    tasks.append(task)
    print(task_tobeadded,"is added to your list of tasks")
# To Mark task as a completed
def mark_task_completed(task_number):
    if 1<=task_number<=len(li_task):
        li_task(task_number)["completed"]=True
        print("task",task_number,":",li_task(task number),"is completed")
    elif len(li_task)==0:
        print("your lis of task is empty")
    else:
        print("invalid choice,please select a valid task number")
#                



