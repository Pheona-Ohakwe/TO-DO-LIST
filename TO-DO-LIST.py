
print("To-Do List")
print(" Menu: "
      " Add a task, " " View list, " " Update a task to complete, " " Delete a task, " " Quit ")

complete =[]
incomplete = []

def add_task(incomplete):
    task =input("What task would you like to add to your to-do list?")
    if task not in incomplete:
        incomplete.append(task)
        print(f"Your to-do list is now updated. See list {incomplete}")
    else:
        print(f"That task is. already on your incomplete list. See list {incomplete}")

def view_task(incomplete, complete):
       task = input("Which tasks would you like to view on your to do list? incomplete or complete ")
       if task == "incomplete":
            print("This is a list of incomplete tasks:")
            for task in incomplete:
                print (task)
       elif task =="complete":
            print("This is a list of complete tasks")
            for task in complete:
                print(task)
       else:
            print("Please select between complete or incomplete.")


def update_task(incomplete, complete):
    task = input("To update a task on your incomplete to-do list as updated enter 'update' or enter 'leave' to return to menu:")
    if task == "update":
        print(f"Your incomplete to-do list includes these tasks: {incomplete}")
        try:
            completed_task= input("What task would you like to update?: ")
            incomplete.remove(completed_task)
            complete.append(completed_task)
            print("This is the new list of completed tasks: {completed_task}")
            print("This is the new list of incomplete tasks: {incomplete}")
        except ValueError:
            print("Your to-do-list does not contain that task!")
            option_to_add = input("Would you like to add to it to your completed tasks? Enter: yes  or no ")
            if option_to_add == "yes":
                complete.append(completed_task)
                print(f"Task added. Updated list: {completed_task}.")
            elif option_to_add == "no":
                print(f"No changes made. List: {complete}")
    elif task == "leave":
        print("No changes made.")
    else:
        print("Please enter a valid response. Enter complete or incomplete." )
    

def delete_task(incomplete, complete):
    task = input("To delete a task from incomplete list enter 'incomplete', to delete a task from complete list enter 'complete': ")
    if task == "incomplete":
       print(f"Your current incomplete to-do list includes these tasks:{incomplete} ")
       try:
          incomplete_delete = input("What task would you like to delete?: ")
          incomplete.remove(incomplete_delete)
          print(f"Task deleted. Updated list: {incomplete}")
       except ValueError:
          print("Incomplete to-do-list does not contain that task")
    elif task == "complete":
        print("Current complete to-do list: {complete}")
        complete_delete = input(" What task would you like to delete?: ")
        try:
          complete.remove(complete_delete)
          print(f"Completed to-do-list does not contain that task!")
        except ValueError:
          print("Your incomplete to-do list does not contain that task")
    else:
        print("Invalid response. Enter incomplete or complete.")
                    
            
        

while True:
    response= input("Would you like to add, remove, view, update, or quit?")
    if response == "add":
        add_task(incomplete)
    elif response == "remove":
        delete_task(incomplete,complete)
    elif response == "view":
        view_task(incomplete, complete)
    elif response == "update":
        update_task(incomplete, complete)
    elif response == "quit":
         print("Leaving to-do-list")
         break
    else:
        print("Please enter a valid response. Would you like to add, remove, view, update, or quit?")






