class Task():

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = False
    def changeStatus(self, status):
        self.status=status
class TaskManager():
    def __init__(self):
        self.tasks = []
    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)
    def mark_task(self,task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].changeStatus(True)
    def get_all_tasks(self):
        return self.tasks
    def get_tasks_without_status(self):
        tasks1=[]
        for task in self.tasks:
            if task.status!=True:
                tasks1.append(task)
        return tasks1

TM=TaskManager()
TM.add_task('Послушать лекцию по Python от 10.07','13.07.2024')
TM.add_task('Послушать лекцию по Аналитике данных от 10.07','13.07.2024')
TM.add_task('Сделать домашнее задание по Python от 10.07','13.07.2024')
print("Полный список задач:")
tasks_all=TM.get_all_tasks()
for t in tasks_all:
    print(t.description)
TM.mark_task(0)
print("Текущий список задач:")
tasksWithoutStatus=TM.get_tasks_without_status()
for t in tasksWithoutStatus:
    print(t.description)


