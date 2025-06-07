#Class for handing tasks
from task import Task
import sqlite3

class TaskMaster:
    def __init__(self, database_path: str):

        self.database_path = database_path
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()
        self.tasks = []

        #Load all tasks from db
        #Instantiate the task table 

        create_list = """CREATE TABLE IF NOT EXISTS todo(
        task_id INTEGER PRIMARY KEY,
        content TEXT, 
        status INTEGER)"""

        self.cursor.execute(create_list)
        self.load_all_tasks()
        self.connection.commit()
        
    def add_task(self, content: str):
        
        add_task_command = "INSERT INTO todo (content, status) VALUES(?, ?)"
        self.cursor.execute(add_task_command, (content, 0))
        #Get ID
        new_id = self.cursor.lastrowid
        #Add task object to tasks list
        self.tasks.append(Task(new_id, content, 0))

        #Save changes
        self.connection.commit()

    def display_tasks(self):

        for task in self.tasks:
            task.display_task()

    def load_all_tasks(self):

        self.cursor.execute("SELECT * FROM todo")

        all_tasks = self.cursor.fetchall()
        
        for task in all_tasks:

            task_id = task[0]
            task_content = task[1]
            task_status = task[2]
            
            #Append tasks lsit
            self.tasks.append(Task(task_id, task_content, task_status))

    def delete_task(self, task_id: int):

        delete_command = "DELETE FROM todo WHERE task_id = ?"
        self.cursor.execute(delete_command, (task_id,))
        print(f"Task {task_id} was deleted sucessfully!")
        self.connection.commit()

    def mark_complete(self, task_id):

        update_command = "UPDATE todo SET status = 1 WHERE task_id = ?"
        self.cursor.execute(update_command, (task_id,))
        self.connection.commit()
        get_task_command = "SELECT content FROM todo WHERE task_id = ?"
        self.cursor.execute(get_task_command, (task_id,))
        task_content = self.cursor.fetchall()

        print(f"Marked task: {task_content} as complete!")