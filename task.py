#Class for individual tasks

class Task:
    def __init__(self, task_id, task_description, task_status) -> None:

        self.task_id = task_id
        self.task_description = task_description
        self.task_status = task_status

    def display_task(self):
        if self.task_status == 0:
            current_status = "Pending..."
        else:
            current_status = "Complete!"
        print(f"Task #: {self.task_id} Description: {self.task_description} Status: {current_status}\n")
