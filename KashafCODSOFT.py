#!/usr/bin/env python
# coding: utf-8

# # Task 01: To Do List

# In[3]:


# Initialize an empty to-do list
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

# Function to display the current to-do list
def display_tasks():
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("The to-do list is empty.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


# # Task 02: Calculator

# In[7]:


# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Prompt the user for input
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Input from the user
choice = input("Enter choice (1/2/3/4): ")

# Check if the input is valid
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
else:
    print("Invalid input. Please select a valid operation (1/2/3/4).")


# # Task 03: Password Generator

# In[10]:


# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print(p)


# # Task 04: Rock-Paper Scissors Game

# In[11]:


while True:
    import random
    def game(comp,you):
        if comp==you:
            return None
        elif comp=='rock':
            if you=='scissors':
                return False
            elif you=='paper':
                return True
        elif comp=='paper':
            if you=='rock':
                return False
            elif you=='scissors':
                return True
        elif comp=='scissors':
            if you=='paper':
                return False
            elif you=='rock':
                return True
    print("Computers turn: Rock(r) Paper(p) or Scissors(s)?")
    randno=random.randint(1,3)
    if randno==1:
        comp='rock'
    elif randno==2:
        comp='paper'
    elif randno==3:
        comp='scissors'
    you=input("Your turn: Rock(r) Paper(p) or Scissors(s)?").lower()
    a=game(comp,you)
    print(f"Computer choose {comp}.")
    print(f"You choose {you}.")
    if a==None:
        print("The game is a TIE")
    elif a:
        print("You Win")
    else:
        print("You Loose")
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        break


# # Task 05: Contact Book

# In[12]:


# Create an empty dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"{name} added to contacts.")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("Contacts:")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")
        print("-" * 20)

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter a name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_term in name or search_term == info["phone"]:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact: {name}")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address

        print(f"Contact {name} updated.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

# Main program loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:




