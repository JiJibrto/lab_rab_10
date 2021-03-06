# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение.


def add(workers, las_name, name, tel, date):
    temp = {
        'las_name': las_name,
        'name': name,
        'tel': tel,
        'date': date
    }
    workers.append(temp)
    # Отсортировать список в случае необходимости.
    if len(workers) > 1:
        workers.sort(key=lambda item: item.get('las_name', ''))


def list_def(workers):
    table = []
    line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
        '-' * 4,
        '-' * 15,
        '-' * 15,
        '-' * 20,
        '-' * 20
    )
    table.append(line)
    table.append(
        "| {:^4} | {:^15} | {:^15} | {:^20} | {:^20} |".format(
            "№",
            "Фамилия",
            "Имя",
            "Телефон",
            "Дата рождения"
        )
    )
    table.append(line)
    for idx, worker in enumerate(workers, 1):
        table.append(
            '| {:>4} | {:<15} | {:<15} | {:>20} | {:^20} |'.format(
                idx,
                worker.get('las_name', ''),
                worker.get('name', ''),
                worker.get('tel', 0),
                ".".join(map(str, worker.get('date')))
            )
        )
        table.append(line)
    return '\n'.join(table)


def task(workers, check):
    table = []
    task_list = []
    iz = 0
    for worker in workers:
        if ''.join(map(str, worker.get('date'))) == ''.join(map(str, check)):
            task_list.append(worker)
            iz += 1

    if iz == 0:
        print("Workers not found")
    else:
        line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
            '-' * 4,
            '-' * 15,
            '-' * 15,
            '-' * 20,
            '-' * 20
        )
        table.append(line)
        table.append(
            "| {:^4} | {:^15} | {:^15} | {:^20} | {:^20} |".format(
                "№",
                "Фамилия",
                "Имя",
                "Телефон",
                "Дата рождения"
            )
        )
        table.append(line)
        for idx, worker in enumerate(task_list, 1):
            table.append(
                '| {:>4} | {:<15} | {:<15} | {:>20} | {:^20} |'.format(
                    idx,
                    worker.get('las_name', ''),
                    worker.get('name', ''),
                    worker.get('tel', 0),
                    ".".join(map(str, worker.get('date')))
                )
            )
        return '\n'.join(table)


def load(parts):
    # Прочитать данные из файла JSON.
    with open(parts[1], 'r') as f:
        return json.load(f)



def save(parts):
    # Сохранить данные в файл JSON.
    with open(parts[1], 'w') as f:
        json.dump(workers, f)


def help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить работника;")
    print("list - вывести список работников;")
    print("task - вывести сотрудников определенной даты рождения")
    print("load <имя файла> - загрузить данные из файла;")
    print("save <имя файла> - сохранить данные в файл;")
    print("exit - выход из программы;")


if __name__ == '__main__':
    workers = []
    while True:
        command = input("Enter command> ").lower()

        if command == "exit":
            break

        elif command == "add":
            las_name = str(input("Enter last name>  "))
            name = str(input("Enter first name> "))
            tel = int(input("Enter phone> +"))
            date = list(map(int, input("Enter birthdate separated by space> ").split(" ")))
            add(workers, las_name, name, tel, date)

        elif command == "list":
            print(list_def(workers))

        elif command == "task":
            check = list(map(int, input("Enter birthdate separated by space> ").split(" ")))
            print(task(workers, check))

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            workers = load(parts)

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            save(parts)

        elif command == 'help':
            help()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)