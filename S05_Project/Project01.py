names = []
heights = []
weights = [] 
bmis = []
statuses = [] 

def help():
    print("\nOptions")
    print("1 or add: Add new user")
    print("2 or display: Show all users")
    print("3 or edit: Update user weight")
    print("4 or delete: Delete a user")
    print("5 or search1: Search user by name")
    print("6 or search2: Search user by sub name")
    print("7 or exit: Exit\n")


def get_data():
    name = input("Enter name: ")
    if name in names:
        print("This name already exists!")
        return -1
    height = float(input("Enter height (m): "))
    weight = float(input("Enter weight (kg): "))
    return name, height, weight


def calculate_status(bmi):
    if bmi < 18.5:
            status = "Underweight"
    elif bmi < 25:
        status = "Normal"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"
    return status


def add(name, height, weight):
    names.append(name)
    heights.append(height)
    weights.append(weight)
    bmi = weight / (height**2)
    bmi = round(bmi, 2)
    bmis.append(bmi)
    status = calculate_status(bmi)
    statuses.append(status)


def display():
    if len(names) == 0:
        print("No users yet!")

    for i in range(len(names)):
        print(f"{i+1}: {names[i]} | H: {heights[i]} | W: {weights[i]} | BMI: {bmis[i]} | Status: {statuses[i]}")
    print()


def edit(name, new_weight):
    i = names.index(name)
    weights[i] = new_weight
    bmi = new_weight / (heights[i]**2)
    bmi = round(bmi, 2)
    bmis[i] = bmi
    status = calculate_status(bmi)
    statuses[i] = status
    print(f"Updated {name}'s data!")


def remove(name):
    i = names.index(name)
    del names[i]
    del heights[i]
    del weights[i]
    del bmis[i]
    del statuses[i]
    print(f"{name} deleted!")


def search1(name):
    if name in names:
        i = names.index(name) 
        print(f"{names[i]} | H: {heights[i]} | W: {weights[i]} | BMI: {bmis[i]} | Status: {statuses[i]}")
    else:
        print("User not found!")


def search2(sub_name):
    not_found = True
    for i, name in enumerate(names):
        if sub_name in name:
            print(f"{names[i]} | H: {heights[i]} | W: {weights[i]} | BMI: {bmis[i]} | Status: {statuses[i]}")
            not_found = False 
    if not_found:
        print("User not found!")
        

while True:
    choice = input("choose an option (1-7) or help: ").lower()
    if choice == "help":
       help()

    elif choice == "1" or choice == "add":
        result = get_data()
        if result != -1:
            name, height, weight = result
            add(name, height, weight)

    elif choice == "2" or choice == "display":
        display()

    elif choice == "3" or choice == "edit":
        name = input("Enter name: ")
        if name in names:
            new_weight = float(input("Enter new weight: "))
            edit(name, new_weight)
        else:
            print("User not found!")

    elif choice == "4" or choice == "delete":
        name = input("Enter name for remove: ")
        if name in names:
            remove(name)
        else:
            print("User not found!")

    elif choice == "5" or choice == "search1":
        name = input("Enter name: ")
        search1(name)

    elif choice == "6" or choice == "search2":
        sub_name = input("Enter name: ")
        search2(sub_name)

    elif choice == "7" or choice == "exit":
        break
    else:
        print(f"{choice}: not found!")
