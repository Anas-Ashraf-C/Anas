from os import system, name
from sys import exit
from time import sleep

# Clear the terminal screen depending on the operating system
def clear_screen():
    system("cls" if name == "nt" else "clear")

class Tasks:
    def __init__(self):
        # Each Menu object will have its own list of tasks
        self.tasks = [] 
        
    def add_task(self):
        # Add a new task to the list
        answer = input("Enter your new Task: ")
        self.tasks.append(answer)
        self.see_all_tasks()  # Show the updated list

    def see_all_tasks(self):
        # Display all tasks in the list
        print("The All Tasks in the list:")
        x = 1
        for i in self.tasks:
            print(f"Task {x} is : {i}")
            x += 1
        sleep(2)  # Pause briefly so the user can read the output
        print("") # New Line

    def delete_task(self):
        # Remove a task from the list by its number
        self.see_all_tasks()
        print("Which task do you want to delete?")
        try:
            RmIt = int(input("Enter Number: "))
        except:
            # If user enters something that is not a number
            print("Error: Try Again")
            return
        if RmIt > len(self.tasks):
            # If the number is out of range
            print("I'm sorry! This task is not in your list of tasks")
            return
        # Remove the chosen task
        self.tasks.pop(RmIt - 1)
        print("The new Tasks list is:")
        self.see_all_tasks()

    def end_onec_task(self):
        # Mark a task as completed (remove it from the list)
        self.see_all_tasks()
        print("Nice! I'm happy for you")
        print("Which task did you finish?")
        try:
            fnIt = int(input("Enter Number: "))
        except:
            # Handle non-numeric input
            print("Error: Try Again")
            return
        if fnIt > len(self.tasks):
            # Handle invalid task number
            print("I'm sorry! This task is not in your list of tasks")
            return
        # Remove the completed task
        self.tasks.pop(fnIt - 1)
        self.see_all_tasks()  # Show updated list after removing

class Menu(Tasks):
    def __init__(self):
        super().__init__()

    def display_main_manu(self):
        # Main loop to display the menu and handle user choices
        print("Welcome to the (TODO List) App!")
        while True:
            print("Enter Number 1 for Add Task")
            if len(self.tasks) > 0:
                print("Enter Number 2 for See All Task")
                # Only show these options if there are tasks in the list
                print("Enter Number 3 to delete a task from existing tasks")
                print("Enter Number 4 to mark a task as completed")
            print("Enter 0 to exit the program")
            choise = input("Enter Number: ")

            # Check user input and call the appropriate method
            if choise == "0":
                print("bye bye!")
                exit(0)  # End the program
            elif choise == "1":
                clear_screen()
                self.add_task()
            elif choise == "2":
                clear_screen()
                self.see_all_tasks()
            elif choise == "3":
                clear_screen()
                self.delete_task()
            elif choise == "4":
                clear_screen()
                self.end_onec_task()
            else:
                # Invalid input message
                print("Error: Invalid Input, Try Again")

# Create a Menu object and start the program
start_project = Menu()
start_project.display_main_manu()
