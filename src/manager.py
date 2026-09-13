from src.storage import load_contacts, save_contacts
from src.models import validate_name, validate_number, validate_email

def _get_sorted_contacts():
    return sorted (
        load_contacts (),
        key=lambda c: f"{c['first_name']} {c['middle_name']} {c['last_name']}".strip ().lower ()
    )


def _select_contact(contacts):
     # Displays names and returns the selected contact dictionary
    if not contacts:
        print ( "No contacts available." )
        return None

    print ( "\nContacts:" )
    for i, c in enumerate ( contacts, start=1 ):
        print ( f"{i}. {c['first_name']} {c['middle_name']} {c['last_name']}".strip () )

    try:
        choice = int ( input ( "\nEnter contact index: " ) )
        if 1 <= choice <= len ( contacts ):
            return contacts[choice - 1]
        print ( "Invalid index." )
    except ValueError:
        print ( "Please enter a valid number." )
    return None


def add_contact():
    contacts = load_contacts ()
    print ( "\n--- Add Contact ---" )

    while True:
        first = input ( "First name: " ).strip ().title ()
        if validate_name ( first ): break
        print ( "Invalid first name." )

    while True:
        middle = input ( "Middle name (Enter to skip): " ).strip ().title ()
        if validate_name ( middle, allow_blank=True ): break
        print ( "Invalid middle name." )

    while True:
        last = input ( "Last name: " ).strip ().title ()
        if validate_name ( last ): break
        print ( "Invalid last name." )

    full_name = f"{first} {middle} {last}".strip ().lower ()
    if any (
            f"{c['first_name']} {c['middle_name']} {c['last_name']}".strip ().lower () == full_name for c in contacts ):
        print ( "Contact name already exists." )
        return

    while True:
        number = input ( "Phone number (10 digits): " ).strip ()
        if not validate_number ( number ):
            print ( "Invalid number." )
            continue
        if any ( c["number"] == number for c in contacts ):
            print ( "Phone number already exists." )
            return
        break

    while True:
        email = input ( "Email: " ).strip ()
        if not validate_email ( email ):
            print ( "Invalid email." )
            continue
        if any ( c["email"].lower () == email.lower () for c in contacts ):
            print ( "Email already exists." )
            return
        break

    contacts.append (
        {"first_name": first, "middle_name": middle, "last_name": last, "number": number, "email": email} )
    save_contacts ( contacts )
    print ( "Contact added successfully!" )


def view_contacts():
    contact = _select_contact ( _get_sorted_contacts () )
    if contact:
        print ( f"\nName:   {contact['first_name']} {contact['middle_name']} {contact['last_name']}".strip () )
        print ( f"Number: {contact['number']}" )
        print ( f"Email:  {contact['email']}" )


def delete_contact():
    contacts = _get_sorted_contacts ()
    contact = _select_contact ( contacts )
    if contact:
        confirm = input ( f"Delete {contact['first_name']}? (y/n): " ).strip ().lower ()
        if confirm == 'y':
            contacts.remove ( contact )
            save_contacts ( contacts )
            print ( "Contact deleted." )
        else:
            print ( "Deletion cancelled." )


def edit_contact():
    contacts = _get_sorted_contacts ()
    contact = _select_contact ( contacts )
    if not contact:
        return

    print ( "\nEdit: \n1. First \n2. Middle \n3. Last \n4. Number \n5. Email \n6. Cancel" )
    choice = input ( "Enter choice: ").strip ()

    if choice == '1':
        new_val = input ( "New first name: " ).strip ().title ()
        if validate_name ( new_val ): contact['first_name'] = new_val
    elif choice == '2':
        new_val = input ( "New middle name: " ).strip ().title ()
        if validate_name ( new_val, allow_blank=True ): contact['middle_name'] = new_val
    elif choice == '3':
        new_val = input ( "New last name: " ).strip ().title ()
        if validate_name ( new_val ): contact['last_name'] = new_val
    elif choice == '4':
        new_val = input ( "New number: " ).strip ()
        if validate_number ( new_val ): contact['number'] = new_val
    elif choice == '5':
        new_val = input ( "New email: " ).strip ()
        if validate_email ( new_val ): contact['email'] = new_val
    elif choice == '6':
        print ( "Cancelled." )
        return
    else:
        print ( "Invalid choice." )
        return

    save_contacts ( contacts )
    print ( "Contact updated." )