from src.manager import add_contact, view_contacts, delete_contact, edit_contact

def main():
    """Main menu loop to drive the contact manager."""
    while True:
        print ( "\n--- Contact Manager ---" )
        print ( "1. Add Contact" )
        print ( "2. View Contacts" )
        print ( "3. Delete Contact" )
        print ( "4. Edit Contact" )
        print ( "5. Exit" )

        try:
            choice = int ( input ( "Choose an option: " ) )
        except ValueError:
            print ( "Enter a number (1-5)." )
            continue

        if choice == 1:
            add_contact ()
        elif choice == 2:
            view_contacts ()
        elif choice == 3:
            delete_contact ()
        elif choice == 4:
            edit_contact ()
        elif choice == 5:
            print ( "Goodbye!" )
            break
        else:
            print ( "Invalid choice." )


if __name__ == "__main__":
    main ()