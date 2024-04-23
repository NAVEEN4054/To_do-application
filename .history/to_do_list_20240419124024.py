# An empty list to store tasks
li_task=[]
# Function to display list of tasks
def display_list():
    if len(li_tasks)==0:
        print("your list of tasks is empty")
    else:
        for i in li_task:
            if task["completed"]:
                status="Done"
            else:
                status="not done yet"
            print(li_tasks(i),":",status)                    

