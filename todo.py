import json
import os

FILE_NAME = "tasks.json"

tasks = []

def load_tasks():
    """Завантажує завдання з файлу"""
    global tasks
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    else:
        tasks = []

def save_task():
    """Зберігає завдання у файл"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def show_menu():
    print("\n=== TO-DO List ===")
    print("1. Додати завдання")
    print("2. Показати всі завдання")
    print("3. Видалити завдання")
    print("4. Вийти")

def add_task():
    task = input("Введіть нове завдання: ")
    tasks.append(task.strip())
    save_task()
    print(f"Ваше завдання {task} додано до списку")

def show_task():
    if not tasks:
        print("Список завдань порожній!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    show_task()
    try:
        num = int(input("Введіть номер для видалення завдання: "))
        removed = tasks.pop(num -1)
        print(f"Завдання '{removed}' видалено!")
    except(ValueError, IndexError):
        print("Не правильний номер!")

def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Оберіть дію (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Не вірний вибір!")
    

if __name__ == "__main__":
    main()



        
        