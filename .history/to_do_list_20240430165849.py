# An empty list to store tasks
li_task=[]
# Function to display list of tasks
def display_list():
    if not li_task:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(li_task, start=1):
            status = "Done" if task["completed"] else "Not Done yet"
            print(f"{i}.{task['task']}-{status}")
# Function to add task in list of tasks
def add_task(task_tobeadded):
    task = {"task": task_tobeadded, "completed": False}
    li_task.append(task)
    print(task_tobeadded,"is added to your list of tasks")

# To Mark task as a completed
def mark_task_completed(task_number):
    if len(li_task)==0:
        print("your lis of task is empty")
    
    elif 1<=task_number<=len(li_task):
        li_task[task_number]="completed"
        print("task",task_number,":",li_task(task_number),"is completed")
    else:
        print("invalid choice,please select a valid task number")

#  to remove a task from list
def remove_task(task_number):
    if len(li_task)==0:
        print("your list of task is empty")
    elif 1<=task_number<=len(li_task):
        del li_task[task_number]
        print(li_task[task_number],"is removed from your list")
    else:
        print("invalid choice,please select a valid task number")
while True:
    print("1.Display list of tasks")
    print("2.To add task to list")
    print("3.To mark the task as completed")
    print("4.To remove the task from list")  
    print("5.quit") 
    choice=int(input("enter the option"))
    if choice==1:
        display_list()
    elif choice==2:
        task_tobeadded=input('enter the task which is to be added')
        add_task(task_tobeadded)
    elif choice==3:
        task_number=int(input("enterthe task number to mark as complete"))
        mark_task_completed(task_number)
    elif choice==4:
        task_number=int(input("enterthe task number to remove"))
        remove_task(task_number)
    else:
        print("invalid choice")




