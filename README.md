
# Inventory sort and search
## Inventory Explanation
The inventory feature in your task manager project manages tasks and user information, allowing users to add, view, and manage tasks. This feature is essential for keeping track of tasks assigned to different users and ensuring that tasks are completed on time.

# Components of the Inventory Feature
Files:

- tasks.txt: Stores task information in a structured format.
- user.txt: Stores user credentials.
# Functions:

- user_login(file_name): Reads user credentials from the specified file and returns them as a dictionary.

- login(users): Prompts the user to log in using a username and password.
 
- reg_user(): Registers a new user by appending their credentials to the user.txt file.
 
- add_task(): Adds a new task to the tasks.txt file.
 
- view_all(): Displays all tasks from the tasks.txt file.
 
- view_mine(username): Displays tasks assigned to the logged-in user.

- generate_reports(): Generates reports on tasks and users and saves them to task_overview.txt and user_overview.txt
