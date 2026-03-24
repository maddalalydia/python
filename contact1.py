file = "contact.txt"

def create():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    f = open(file, "a")
    f.write(name + "," + phone + "\n")
    f.close()
    print("Contact added successfully")

def view():
    f = open(file, "r")
    print(f.read())
    f.close()

def update():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")

    f = open(file, "r")
    lines = f.readlines()
    f.close()

    f = open(file, "w")
    for line in lines:
        n, p = line.strip().split(",")
        if n == name:
            f.write(n + "," + new_phone + "\n")
        else:
            f.write(line)
    f.close()
    print("Contact updated")

def delete():
    name = input("Enter name to delete: ")

    f = open(file, "r")
    lines = f.readlines()
    f.close()

    f = open(file, "w")
    for line in lines:
        n, p = line.strip().split(",")
        if n != name:
            f.write(line)
    f.close()
    print("Contact deleted")

while True:
    print("\n1.Create 2.View 3.Update 4.Delete 5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        create()
    elif ch == "2":
        view()
    elif ch == "3":
        update()
    elif ch == "4":
        delete()
    elif ch == "5":
        break