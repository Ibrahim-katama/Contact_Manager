# Contact Manager

A simple console-based Python application for managing personal contacts efficiently. 

---

## Features

* **Add Contact:** Collects names, validates 10-digit mobile numbers and emails, and checks for duplicates before saving.
* **View Contacts:** Displays an alphabetically sorted list of all stored contacts with selectable indexes for full details.
* **Edit Contact:** Modifies names, phone numbers, or email addresses with built-in duplicate validation to maintain data integrity.
* **Delete Contact:** Displays an indexed list for easy selection and features a two-step confirmation prompt to prevent accidental deletion.
* **Persistent CSV Storage:** Automatically initializes, reads from, and updates data stored in a local `.csv` file.

---

## Project Structure

```text
contact_manager/
│
├── data/
│   └── contact.csv
├── src/
│   ├── __init__.py
│   ├── models.py        
│   ├── storage.py       
│   └── manager.py       
│
├── main.py              
├── .gitignore
└── README.md
```
## Tech Stack & Setup

* **Language**: Python 3.x

* **Standard Libraries**: csv, re, os
---

## Execution Steps:

* Clone the repository to your local machine.

* Navigate to the root project directory (contact_manager/).

* Run the application via the main orchestrator script using the command

``` bash
  Bash 
  
  python main.py
```