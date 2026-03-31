import time 

appointments = {}  
next_id = 1    

def help():
    print("\nOptions")
    print("1 or add: Add new appointment")
    print("2 or display: Show all appointments")
    print("3 or edit: Update appointment")
    print("4 or delete: Delete an appointment")
    print("5 or search: Search by patient name")
    print("6 or complete: Complete an appointment and add prescribed drugs")
    print("7 or exit: Exit\n")

def get_data():
    global next_id
    name = input("Patient name: ")
    doctor = input("Doctor name: ")
    while True:
        v_type = input("Type (checkup, test): ").lower()
        if v_type in ["checkup", "test"]:
            break
    status = "Pending"
    current_time = time.localtime()
    date = time.strftime("%Y-%m-%d", current_time)
    time_now = time.strftime("%H:%M:%S", current_time)
    p_id = "p"+str(next_id)
    next_id += 1
    return name, doctor, v_type, status, date, time_now, p_id

def add(name, doctor, v_type, status, date, time_now, p_id):
    p_data = {
        "name": name,
        "doctor": doctor,
        "type": v_type,
        "date": date,
        "time": time_now,
        "status": status,
        "drugs": []
    }
    appointments[p_id] = p_data
    print(f"Appointment ID {p_id} for {name} added!\n")
    
def display():
    if not appointments:
        print("No appointments yet!\n")
        return
    for p_id, data in appointments.items():
        print(f"ID: {p_id} ----> Name: {data['name']}, Doctor: {data['doctor']}, Type: {data['type']}, Date: {data['date']} {data['time']}, Status: {data['status']}")
        drugs = "-".join(data['drugs'])
        print(f"Drugd: {drugs}")

def edit(p_id):
    if p_id in appointments:
        name = input("Name: ") or appointments[p_id]['name']
        doctor = input("Dcotor name: ") or appointments[p_id]['doctor']
        """v_type = input("Type (checkup, test): ").lower() 
        v_type = v_type or appointments[p_id]['type']"""
        appointments[p_id].update({
            "name": name,
            "doctor": doctor
        })
        print(f"Appointment ID {p_id} for {name} updated!\n")
    else:
        print("ID not found!\n")

def delete(p_id):
    if p_id in appointments:
        del appointments[p_id]
        print(f"Appointment ID {p_id} removed!\n")
    else:
        print("ID not found!\n") 

def search(p_id):
    if p_id in appointments:
        data = appointments[p_id]
        print(f"ID: {p_id} ----> Name: {data['name']}, Doctor: {data['doctor']}, Type: {data['type']}, Date: {data['date']} {data['time']}, Status: {data['status']}")  
        drugs = "-".join(data['drugs'])
        print(f"Drugd: {drugs}")
    else:
        print("ID not found!\n") 

def complete(p_id):
    if p_id in appointments:
        data = appointments[p_id]
        data["status"] = "Completed"
        drugs = input("drug names (use comma): ")
        drugs = drugs.split(",")
        data["drugs"] = drugs
        print(f"Appointment ID {p_id} maked as completed!\n")
    else:
        print("ID not found!\n") 

while True:
    choice = input("Choose an option(1-7) or help: ").lower()
    if choice == "help":
        help()
    elif choice == "1" or choice == "add":
        result = get_data()
        add(*result) 
    elif choice == "2" or choice == "display":
        display() 
    elif choice == "3" or choice == "edit":
        p_id = input("Your ID: ").lower()
        edit(p_id) 
    elif choice == "4" or choice == "delete":
        p_id = input("Your ID: ").lower()
        delete(p_id) 
    elif choice == "5" or choice == "search":
        p_id = input("Your ID: ").lower()
        search(p_id) 
    elif choice == "6" or choice == "complete":
        p_id = input("Your ID: ").lower()
        complete(p_id) 
    elif choice == "7" or choice == "exit":
        break 
    else:
        print(f"{choice}: Not Found!")