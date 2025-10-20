import csv
import os
import re

CONTACTS_FILE = "contact.csv"
FIELDNAMES = ["first_name", "middle_name", "last_name", "number", "email"]
contacts = []


def init_contacts():
    directory = os.path.dirname(CONTACTS_FILE)
    if directory:
        os.makedirs(directory, exist_ok=True)
    if not os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
    load_contacts()


def load_contacts():
    contacts.clear()
    try:
        with open(CONTACTS_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != FIELDNAMES:
                print(f"Invalid CSV format. Expected headers: {', '.join(FIELDNAMES)}")
                return
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass  # Because it is handled by init_contacts
    except PermissionError:
        print("Error: Permission denied when reading 'contact list/contact.csv'. Close any programs using the file.")
    except IOError as e:
        print(f"Error loading CSV: {e}")

# Save contacts from memory to CSV
def save_contacts():
    try:
        with open(CONTACTS_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(contacts)
        print("Changes saved.")
    except PermissionError:
        print("Error: Permission denied when saving to 'contact list/contact.csv'. Close any programs using the file.")
    except IOError as e:
        print(f"Error saving to CSV: {e}")

# Helper: print contacts in table format
def print_contacts(contact_list):
    if not contact_list:
        print("No contacts to display.")
        return
    print("\n{:<4} {:<27} {:<15} {:<30}".format("", "Name", "Number", "Email"))
    for i, contact in enumerate(contact_list, start=1):
        full_name = f"{contact['first_name']} {contact['middle_name']} {contact['last_name']}".strip()
        print("{:<4} {:<27} {:<15} {:<30}".format(f"{i}.", full_name, contact["number"], contact["email"]))
    print()

# Add new contact
def add_contact():
    print("\n--- Add Contact ---")
    while True:
        first_name = input("Enter first name: ").strip().title()
        if not validate_name(first_name):
            print("Invalid first name. Use alphabetic characters only.")
            continue
        break
    while True:
        middle_name = input("Enter middle name (press Enter to skip): ").strip().title()
        if not validate_name(middle_name, allow_blank=True):
            print("Invalid middle name. Use alphabetic characters only.")
            continue
        break
    while True:
        last_name = input("Enter last name: ").strip().title()
        if not validate_name(last_name):
            print("Invalid last name. Use alphabetic characters only.")
            continue
        break
    # Duplicate check
    full_name = f"{first_name} {middle_name} {last_name}".strip()
    existing_names = [
        f"{contact['first_name']} {contact['middle_name']} {contact['last_name']}".strip().lower()
        for contact in contacts
    ]
    if full_name.lower() in existing_names:
        print("This contact name already exists.")
        return

    while True:
        number = input("Enter phone number: ").strip()
        if not validate_number(number):
            print("Invalid phone number. Must be exactly 10 digits.")
            continue
        if any(contact["number"] == number for contact in contacts):
            print("This phone number already exists.")
            return
        break

    while True:
        email = input("Enter email: ").strip()
        if not validate_email(email):
            print("Invalid email format.")
            continue
        if any(contact["email"].lower() == email.lower() for contact in contacts):
            print("This email already exists.")
            return
        break
    contacts.append({
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "number": number,
        "email": email
    })
    save_contacts()
    print(f"Contact '{full_name}' added successfully!")

def validate_name(name, allow_blank=False):
    if allow_blank and name == "":
        return True
    return name.isalpha()

def validate_number(number, allow_blank=False):
    if allow_blank and number == "":
        return True
    return number.isdigit() and len(number) == 10

def validate_email(email, allow_blank=False):
    if allow_blank and email == "":
        return True
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# View contacts (names only -> pick index -> show details)
def view_contacts():
    if not contacts:
        print("No contacts to display.")
        return
    sorted_contacts = sorted(
        contacts,
        key=lambda contact: f"{contact['first_name']} {contact['middle_name']} {contact['last_name']}".strip().lower()
    )
    print("\nContacts:")
    for i, contact in enumerate(sorted_contacts, start=1):
        full_name = f"{contact['first_name']} {contact['middle_name']} {contact['last_name']}".strip()
        print(f"{i}. {full_name}")

    while True:
        try:
            choice = int(input("\nEnter the index of the contact to view details: "))
            if 1 <= choice <= len(sorted_contacts):
                selected = sorted_contacts[choice - 1]
                print_contacts([selected])
            else:
                print("Invalid index.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        break
# Delete a contact
def delete_contact():
    if not contacts:
        print("No contacts to delete.")
        return
    # Sort contacts alphabetically by name
    sorted_contacts = sorted(
        contacts,
        key=lambda contact: f"{contact['first_name']} {contact['middle_name']} {contact['last_name']}".strip().lower()
    )
    # Show contacts
    print("\nContacts:")
    for i, contact in enumerate(sorted_contacts, start=1):
        full_name = f"{contact['first_name']} {contact['middle_name']} {contact['last_name']}".strip()
        print(f"{i}. {full_name}")
    while True:
        try:
            choice = int(input("Enter the index of the contact to delete: "))
            if 1 <= choice <= len(sorted_contacts):
                contact = sorted_contacts[choice - 1]
                full_name = f"{contact['first_name']} {contact['middle_name']} {contact['last_name']}".strip()
                confirm = input(f"Are you sure you want to delete {full_name}'s contact? (y/n): ").strip().lower()
                if confirm == "y":
                    contacts.remove(contact)
                    save_contacts()
                    print(f"Contact for {full_name} deleted successfully.")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid index.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break

# Edit a contact
def edit_contact():
    if not contacts:
        print("No contacts to edit.")
        return
    # Sort contacts alphabetically by name
    sorted_contacts = sorted(
        contacts,
        key=lambda c: f"{c['first_name']} {c['middle_name']} {c['last_name']}".strip().lower()
    )
    # Show only names
    print("\nContacts:")
    for i, contact in enumerate(sorted_contacts, start=1):
        full_name = f"{contact['first_name']} {contact['middle_name']} {contact['last_name']}".strip()
        print(f"{i}. {full_name}")
    try:
        choice = int(input("Enter the index of the contact to edit: "))
        if 1 <= choice <= len(sorted_contacts):
            contact_to_edit = sorted_contacts[choice - 1]
            while True:
                print("\nChoose what to edit:")
                print("1. First name")
                print("2. Middle name")
                print("3. Last name")
                print("4. Number")
                print("5. Email")
                print("6. Done")
                try:
                    option = int(input("Enter choice: "))
                except ValueError:
                    print("Enter a valid option!")
                    continue
                if option == 1:
                    print(f"Current first name: {contact_to_edit['first_name']}")
                    new_first = input("Enter new first name: ").strip().title()
                    if validate_name(new_first):
                        contact_to_edit["first_name"] = new_first
                        save_contacts()
                        print("First name updated.")
                    else:
                        print("Invalid first name.")
                elif option == 2:
                    print(f"Current middle name: {contact_to_edit['middle_name'] or '(empty)'}")
                    new_middle = input("Enter new middle name: ").strip().title()
                    if new_middle == "" or validate_name(new_middle):
                        contact_to_edit["middle_name"] = new_middle
                        save_contacts()
                        print("Middle name updated.")
                    else:
                        print("Invalid middle name.")
                elif option == 3:
                    print(f"Current last name: {contact_to_edit['last_name']}")
                    new_last = input("Enter new last name: ").strip().title()
                    if validate_name(new_last):
                        contact_to_edit["last_name"] = new_last
                        save_contacts()
                        print("Last name updated.")
                    else:
                        print("Invalid last name.")
                elif option == 4:
                    print(f"Current number: {contact_to_edit['number']}")
                    new_number = input("Enter new number: ").strip()
                    if not validate_number(new_number):
                        print("Invalid number! Must be exactly 10 digits.")
                        continue
                    if any(contact["number"] == new_number and contact != contact_to_edit for contact in contacts):
                        print("This phone number already exists.")
                        continue
                    contact_to_edit["number"] = new_number
                    save_contacts()
                    print("Number updated.")
                elif option == 5:
                    print(f"Current email: {contact_to_edit['email']}")
                    new_email = input("Enter new email: ").strip()
                    if not validate_email(new_email):
                        print("Invalid email format.")
                        continue
                    if any(contact["email"].lower() == new_email.lower() and contact != contact_to_edit for contact in contacts):
                        print("This email already exists.")
                        continue
                    contact_to_edit["email"] = new_email
                    save_contacts()
                    print("Email updated.")
                elif option == 6:
                    save_contacts()
                    print("Finished editing contact.")
                    break
                else:
                    print("Invalid option. Try again.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Menu
def menu():
    init_contacts()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Edit Contact")
        print("5. Exit")
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Enter a number (1-5).")
            continue
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            edit_contact()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()