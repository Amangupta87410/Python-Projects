def Task():
    tasks=[]
    print("<---------Welcome to The Task Management APP----------->")
    total_task=int(input("Enter How Many Task You Want To Add = "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's Tasks are \n {tasks}")
    while True:
        operation=int(input("Enter 1-Add \n2-Update\n3-Delete\n4-view\n5-Exit/Stop "))
        if operation==1:
            add=input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added... ")
        elif operation==2:
            updated_val=input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up=input("Enter new Task = ")
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print(f"updated task {up}")
                
        elif operation==3:
            del_val=input("Which task you want to delete = ")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")
        elif operation==4:
            print(f"Total Task are = {tasks}")
        
        elif operation==5:
            print("Closing the Program....")
            break
        
        else:
            print("Invalid Input")

Task()
            