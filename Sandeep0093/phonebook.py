# use a dictionary to implement a phonebook application wher user can add, delete, search contacts
phonebook = {}
def add_contact(name, number):
    phonebook[name] = number
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
def search_contact(name):
    return phonebook.get(name, "Contact not found")     
def display_contacts():
    for name, number in phonebook.items():
        print(f"{name}: {number}")
