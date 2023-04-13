import os
from datetime import datetime

def load_tasks():
    if not os.path.exists('tasks.txt'):
        return []
    with open('tasks.txt', 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def save_tasks(tasks):
    with open('tasks.txt', 'w') as f:
        f.write('\n'.join(tasks))

def add_task(tasks):
    task = input('Enter a new task: ')
    tasks.append(f'[{datetime.now()}] {task}')


def remove_task(tasks):
    index = int(input('Enter the index of the task to remove: '))
    del tasks[index]

def display_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f'{i}. {task}')


def main():
    tasks = load_tasks()
    while True:
        print('1. Add task')
        print('2. Remove task')
        print('3. Display tasks')
        print('4. Quit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            remove_task(tasks)
        elif choice == 3:
            display_tasks(tasks)
        elif choice == 4:
            save_tasks(tasks)
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
