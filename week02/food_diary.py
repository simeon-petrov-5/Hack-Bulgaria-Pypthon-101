#Food diary
from datetime import datetime
today = datetime.now()
date = "{}.{}.{}".format(today.day, today.month, today.year)
diary = {}

def add_meal(food):
    if date in diary:
        diary[date].append(food)
        print(diary[date] + " 1")
    else:
        diary[date] = food
        print(diary[date] + " 2")
    return "Okay, it's done"

def show_list(date):
    if date in diary:
        output = "\n".join(diary[date])
        return output
    else:
        return "There's no record for that day."


while True:
    print("""
    Hello and Welcome!
    Choose a command.
    1. meal - to write what are you eating now.
    2. list <dd.mm.yyyy> - lists all the meals that you ate that day
    3. exit""")
    decision = input("Enter command> ").lower()
    decision = decision.split()
    command, parameter = decision[0], decision[1]

    if command == "meal":
        add_meal(parameter)
    elif command == "list":
        show_list(parameter)
    elif command == "exit":
        break


