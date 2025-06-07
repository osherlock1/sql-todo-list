"""
SQL based todo-list app

What I need to accomplish --------------------

1. Persistant storage in the SQL databse

2. Table Structre of task_id, text_description, status

3. Add tasks

4. View all tasks

5. Update Task's status

6. Delete Tasks

"""
from task_master import TaskMaster


def main():

    database_path = "todo.db"
    task_manager = TaskMaster(database_path)

    print("Welcome to the Task Manager Menu! \n")
    while True:


        print("""What would you like to do: \n
                1: Add a task
                2: Display all Tasks
                3: Delete a task
                4: Mark a task as complete""")
        user_input = input()

        if user_input == '1':
            
            print("What is the description of your task?")
            description = input()
            task_manager.add_task(description)
            print("Task Added Sucessfully!")

        elif user_input == '2':
            print("Displaying Tasks: ")
            task_manager.display_tasks()

        elif user_input == '3':
            print("Input the ID of the task you want to delete: \n")
            target_id = int(input())
            task_manager.delete_task(target_id)
        
        elif user_input == '4':
            print("Input the task ID you want to mark as complete")
            target_id = int(input())
            task_manager.mark_complete(target_id)

        else:
            print("Please input valid input\n")

if __name__ == "__main__":
    main()
