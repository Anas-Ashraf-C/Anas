from os import system, name
from sys import exit
from time import sleep

def clear_screen():
    system("cls" if name == "nt" else "clear")

class Tasks:
    def __init__(self):
        self.tasks = []  # Store tasks in a list

    def add_task(self):
        answer = input("Enter your new Task: ")
        self.tasks.append(answer)
        self.see_all_tasks()

    def see_all_tasks(self):
        print("The All Tasks in the list:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"Task {idx} is : {task}")
        sleep(1)
        print("")

    def delete_task(self):
        self.see_all_tasks()
        print("Which task do you want to delete?")
        try:
            RmIt = int(input("Enter Number: "))
        except:
            print("Error: Try Again")
            return
        if RmIt > len(self.tasks) or RmIt <= 0:
            print("This task is not in your list!")
            return
        self.tasks.pop(RmIt - 1)
        print("The new Tasks list is:")
        self.see_all_tasks()

    def end_once_task(self):
        self.see_all_tasks()
        print("Nice! I'm happy for you")
        print("Which task did you finish?")
        try:
            fnIt = int(input("Enter Number: "))
        except:
            print("Error: Try Again")
            return
        if fnIt > len(self.tasks) or fnIt <= 0:
            print("This task is not in your list!")
            return
        self.tasks.pop(fnIt - 1)
        self.see_all_tasks()

class Menu:
    def __init__(self, tasks : Tasks):
        self.tasks = tasks

    def display_main_menu(self):
        print("Welcome to the (TODO List) App!")
        print("Enter Number 1 for Add Task")
        if len(self.tasks.tasks) > 0:
            print("Enter Number 2 for See All Task")
            print("Enter Number 3 to delete a task")
            print("Enter Number 4 to mark a task as completed")
        print("Enter 0 to exit the program")
        choice = input("Enter Number: ")
        return choice

class List:
    def __init__(self):
        self.tasks = Tasks()
        self.menu = Menu(self.tasks)

    def sequence_of_functions(self):
        while True:
            choice = self.menu.display_main_menu()
            if choice == "0":
                print("bye bye!")
                exit(0)
            elif choice == "1":
                clear_screen()
                self.tasks.add_task()
            elif choice == "2":
                clear_screen()
                self.tasks.see_all_tasks()
            elif choice == "3":
                clear_screen()
                self.tasks.delete_task()
            elif choice == "4":
                clear_screen()
                self.tasks.end_once_task()
            else:
                print("Error: Invalid Input, Try Again")

start_project = List()
start_project.sequence_of_functions()
