import json

file_name = "students.json"

def load_data():
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(file_name, "w") as f:
        json.dump(data, f)


def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll: ")
    data = load_data()
    data.append({"name": name, "roll": roll})
    save_data(data)
    print("Student added")


def show_students():
    data = load_data()
    for s in data:
        print(s["name"], s["roll"])


def search_student():
    roll = input("Enter roll: ")
    data = load_data()
    for s in data:
        if s["roll"] == roll:
            print("Found:", s["name"])


def delete_student():
    roll = input("Enter roll: ")
    data = load_data()
    data = [s for s in data if s["roll"] != roll]
    save_data(data)
    print("Deleted")


while True:
    print("\n1 Add")
    print("2 Show")
    print("3 Search")
    print("4 Delete")
    print("5 Exit")

    ch = input("Choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        show_students()
    elif ch == "3":
        search_student()
    elif ch == "4":
        delete_student()
    elif ch == "5":
        break
