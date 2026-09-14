# Question 66
# Create a Contact Management System using Functions with add, search, update, delete, and display contacts.

contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone

def search_contact():
    name = input("Name: ")
    print(contacts.get(name, "Contact not found"))

def update_contact():
    name = input("Name: ")
    if name in contacts:
        contacts[name] = input("New phone: ")

def delete_contact():
    name = input("Name: ")
    if name in contacts:
        del contacts[name]

def display_contacts():
    for name, phone in contacts.items():
        print(name, ":", phone)

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = input("Choice: ")
    if choice == "1": add_contact()
    elif choice == "2": search_contact()
    elif choice == "3": update_contact()
    elif choice == "4": delete_contact()
    elif choice == "5": display_contacts()
    elif choice == "6": break
    else: print("Invalid choice")
