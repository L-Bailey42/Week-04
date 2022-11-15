#!/usr/bin/env python3

from statistics import mean

WIDTH = 32


def task_1(num):
    if 1 >= num >= 100:
        return False
    else:
        return True


def task_2(string):
    lower_count = 0
    upper_count = 0
    for char in string:
        if char.islower():
            lower_count += 1
        else:
            upper_count += 1

    return lower_count, upper_count


def task_3():
    name = input("\nEnter your name: ").title()
    print(name)


def task_4(word):
    word = word[:-1]

    return word


def task_5(temp, choice):
    if choice == '1':
        temp = (temp * (9 / 5) + 32)
    elif choice == '2':
        temp = ((temp - 32) * 5 / 9)
    else:
        print(f"{choice} is not an option.")

    return temp


def task_7(temps):
    maximum = max(temps)
    minimum = min(temps)
    avg = mean(temps)

    return maximum, minimum, avg


if __name__ == "__main__":
    print(f"{'=' * WIDTH}\n{'PROGRAMMING PORTFOLIO':^{WIDTH}}\n{'=' * WIDTH}")

    print(f"\n{'TASK 1':^{WIDTH}}\n{'-' * 6:^{WIDTH}}")
    num = int(input("\nEnter a number: "))
    print(task_1(num))

    print(f"\n{'TASK 2':^{WIDTH}}\n{'-' * 6:^{WIDTH}}")
    string = input("\nEnter a string: ")
    case_count = task_2(string)
    print(f"Lowercase: {case_count[0]}\nUppercase: {case_count[1]}")

    print(f"\n{'TASK 3':^{WIDTH}}\n{'-' * 6:^{WIDTH}}")
    task_3()

    print(f"\n{'TASK 4':^{WIDTH}}\n{'-' * 6:^{WIDTH}}")
    word = input("Enter a word: ")
    print(task_4(word))

    print(f"\n{'TASK 5 + 6':^{WIDTH}}\n{'-' * 10:^{WIDTH}}")
    print(f"\n{'1. Celsius to Farenheit':^{WIDTH}}\n{'2. Farenheit to Celsius':^{WIDTH}}")
    choice = input("\nEnter a choice (1/2): ")
    temp = int(input("\nEnter a temperature: "))
    print(f"Result: {task_5(temp, choice)}")

    print(f"\n{'TASK 7':^{WIDTH}}\n{'-' * 6:^{WIDTH}}")
    temps = []
    for count in range(6):
        temp = int(input("Enter a temperature in Celsius: "))
        temps.append(temp)
    stats = task_7(temps)
    print(f"\nMaximum: {stats[0]}\nMinimum: {stats[1]}\nAverage (Mean): {stats[2]}")

    print(f"\n{'TASK 8':^{WIDTH}}\n{'-' * 6:^{WIDTH}}")
    temps = []
    while True:
        temp = input("Enter a temperature in Celsius: ")
        if not temp:
            break
        temps.append(int(temp))
    stats = task_7(temps)
    print(f"\nMaximum: {stats[0]}\nMinimum: {stats[1]}\nAverage (Mean): {stats[2]}")
