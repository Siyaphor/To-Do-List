tasks = []

def show_menu():
    print("\n📋 TO-DO LIST MENU")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save to file")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks in your list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the new task: ")
    tasks.append(task)
    print("✅ Task added!")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Task '{removed}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def save_to_file():
    with open("todo_list.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("💾 Tasks saved to todo_list.txt")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            save_to_file()
        elif choice == '5':
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
