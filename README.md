# Python ToDo List Application

This is an extensive ToDo list application that was initially a **Command Line Interface (CLI)** project. Now, it's in the process of being ported to a **Graphical User Interface (GUI)** using **PyQt5**. While all the features are not fully functional yet, the project is open to contributions for further development.

## Features

### CLI Version:
The CLI version of the application allows users to:
- **Add a Task**: Input a new task to the list.
- **View Tasks**: Display all the current tasks in the list.
- **Delete a Task**: Remove a selected task from the list.
- **Edit a Task**: Modify the content of an existing task.
- **Quit the Application**: Exit the application.

#### CLI Sample Workflow:
```python
# Welcome to the Todo Application
# Press 1 to add a task
# Press 2 to view todos
# Press 3 to delete the task
# Press 4 to edit the task
# Press 5 to quit the application

# Example flow:
# Input:
# 1 -> Add a task
# 2 -> View todos
# 3 -> Delete a task
# 4 -> Edit a task
# 5 -> Quit the application
```
## You can uncomment the above line to get the CLI version
### GUI Version (In Progress):
The application is now being ported to a **GUI** using **PyQt5**. The GUI version offers a more user-friendly experience, with buttons and visual elements that replace the CLI commands.

Current features in the GUI:
- **Task Viewing**: You can see your list of tasks in the GUI.
- **Add/Edit/Delete** functionality is being ported but may not work perfectly at the moment.

## Technologies Used

- **Python**: Core language used for the application.
- **PyQt5**: For creating the graphical user interface.
- **SQLite**: (Optional, for future enhancements like storing tasks persistently).

## Installation

### Requirements:
- Python 3.x
- PyQt5

Install dependencies using pip:
```bash
pip install pyqt5
```

### How to Run:

1. Clone the repository:
   ```bash
   git clone https://github.com/afolabisamguy/Python-Todo_List.git
   ```

2. Navigate into the project directory:
   ```bash
   cd todo-list-app
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Contributing

This project is open to contributions! If you'd like to help:
- Port remaining functionalities from the CLI to the GUI.
- Improve the overall UI/UX of the application.
- Add features such as persistent storage (e.g., using SQLite).

Feel free to fork this project, make your changes, and submit a pull request.

## Future Goals
- Complete the GUI migration.
- Add persistent storage for todos.
- Improve task management, such as task categories, due dates, and priorities.
- Make it cross-platform compatible for easier use on Windows, macOS, and Linux.
