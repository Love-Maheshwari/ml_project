import sqlite3

# Function to initialize the database and create the tasks table
def initialize_database():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status TEXT DEFAULT 'pending'
    )
    """)
    connection.commit()
    connection.close()

# Function to add a new task
def add_task(title):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    connection.commit()
    connection.close()
    print(f"Task '{title}' added!")

# Function to view all tasks
def view_tasks():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    connection.close()

    if tasks:
        print("\nTasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[2]}")
    else:
        print("\nNo tasks found.")

# Function to update a task's status
def update_task(task_id, new_status):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    connection.commit()
    connection.close()
    print(f"Task ID {task_id} updated to '{new_status}'.")

# Function to delete a task
def delete_task(task_id):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()
    print(f"Task ID {task_id} deleted.")

# Main menu to interact with the application
def main():
    initialize_database()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_status = input("Enter new status (pending/completed): ")
            update_task(task_id, new_status)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
