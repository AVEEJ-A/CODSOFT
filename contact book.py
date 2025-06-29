# Simple Contact Manager

contact_list = []

def show_menu():
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    print("\nAdd New Contact")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    contact_list.append(contact)
    print("Contact saved.")

def view_contacts():
    if not contact_list:
        print("\nNo contacts found.")
        return

    print("\nSaved Contacts:")
    for index, contact in enumerate(contact_list):
        print(f"{index + 1}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("\nEnter name or phone to search: ")
    found = False
    
    for contact in contact_list:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print("\nContact Found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    
    if not found:
        print("No matching contact found.")

def update_contact():
    name = input("\nEnter the name of the contact to update: ")
    
    for contact in contact_list:
        if contact['name'].lower() == name.lower():
            print("Leave input empty to keep current value.")
            new_phone = input(f"New Phone ({contact['phone']}): ")
            new_email = input(f"New Email ({contact['email']}): ")
            new_address = input(f"New Address ({contact['address']}): ")
            
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address

            print("Contact updated.")
            return
    
    print("Contact not found.")

def delete_contact():
    name = input("\nEnter the name of the contact to delete: ")
    
    for contact in contact_list:
        if contact['name'].lower() == name.lower():
            contact_list.remove(contact)
            print("Contact deleted.")
            return
    
    print("Contact not found.")

def run():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
run()
