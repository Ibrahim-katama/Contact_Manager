import csv
import os

CONTACTS_FILE = "data/contact.csv"
FIELDNAMES = ["first_name", "middle_name", "last_name", "number", "email"]

def init_file():
    os.makedirs(os.path.dirname(CONTACTS_FILE), exist_ok=True)
    if not os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "w", newline="") as file:
            csv.DictWriter(file, fieldnames=FIELDNAMES).writeheader()

def load_contacts():
    #Reads the CSV and returns a list of contact dictionaries
    init_file()
    try:
        with open(CONTACTS_FILE, "r", newline="") as file:
            return list(csv.DictReader(file))
    except IOError as e:
        print(f"Error loading CSV: {e}")
        return []

def save_contacts(contacts_list):
    #Writes the current list of contacts back to the CSV
    try:
        with open(CONTACTS_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(contacts_list)
    except IOError as e:
        print(f"Error saving CSV: {e}")