import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store contact information (name as key and details as value)
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        update_contact_list()
        clear_input_fields()
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

# Function to view all contacts
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, name + " - " + details['Phone'])

# Function to search for contacts
def search_contact():
    search_term = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term in name.lower() or search_term in details['Phone']:
            contact_list.insert(tk.END, name + " - " + details['Phone'])

# Function to update contact details
def update_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_contact = contact_list.get(selected_index[0])
        selected_name = selected_contact.split(" - ")[0]
        new_phone = phone_entry.get()
        new_email = email_entry.get()
        new_address = address_entry.get()

        if selected_name in contacts:
            contacts[selected_name]['Phone'] = new_phone
            contacts[selected_name]['Email'] = new_email
            contacts[selected_name]['Address'] = new_address
            update_contact_list()
            clear_input_fields()

# Function to delete a contact
def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_contact = contact_list.get(selected_index[0])
        selected_name = selected_contact.split(" - ")[0]

        if selected_name in contacts:
            del contacts[selected_name]
            update_contact_list()
            clear_input_fields()

# Function to clear input fields
def clear_input_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Contact List App")
window.geometry("400x400")  # Set the window size

# Labels
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
phone_label = tk.Label(window, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)
email_label = tk.Label(window, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5)
address_label = tk.Label(window, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=5)

# Entry fields
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)
phone_entry = tk.Entry(window)
phone_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry = tk.Entry(window)
email_entry.grid(row=2, column=1, padx=10, pady=5)
address_entry = tk.Entry(window)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(window, text="Add Contact", command=add_contact, bg='green', fg='white')
add_button.grid(row=4, column=0, columnspan=2, sticky="we", padx=10, pady=10)
update_button = tk.Button(window, text="Update Contact", command=update_contact, bg='orange', fg='white')
update_button.grid(row=6, column=0, columnspan=2, sticky="we", padx=10, pady=10)
delete_button = tk.Button(window, text="Delete Contact", command=delete_contact, bg='red', fg='white')
delete_button.grid(row=7, column=0, columnspan=2, sticky="we", padx=10, pady=10)
search_button = tk.Button(window, text="Search", command=search_contact, bg='blue', fg='white')
search_button.grid(row=5, column=0, columnspan=2, sticky="we", padx=10, pady=10)

# Contact list
contact_list = tk.Listbox(window)
contact_list.grid(row=0, column=2, rowspan=11, columnspan=5, padx=10, pady=10,sticky='nswe')  # Make the listbox span more rows

# Search field
search_label = tk.Label(window, text="Search:")
search_label.grid(row=9, column=0, padx=10, pady=5)
search_entry = tk.Entry(window)
search_entry.grid(row=9, column=1, padx=10, pady=5)

# Start the application
window.mainloop()
