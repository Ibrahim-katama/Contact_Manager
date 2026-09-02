# Contact Manager

A clean, console-based Python application for managing personal contacts efficiently using CSV storage. Features robust input validation, duplicate prevention, full CRUD (Create, Read, Update, Delete) functionality, and two-step verification to protect user data.

---

##  Features

- **Add Contact**:
  - Collects First Name, Middle Name (optional), and Last Name.
  - Validates 10-digit mobile numbers and email formatting[cite: 1].
  - Checks for duplicate records (by full name, phone number, or email) before saving[cite: 1].

- View Contact:
  - Displays an indexed list of all stored contacts by full name[cite: 1].
  - Select any contact index to view complete details (Full Name, Phone Number, Email)[cite: 1].

- Edit Contact:
  - Modify names, phone numbers, or email addresses of any existing contact[cite: 1].
  - Enforces duplicate validation during edits to maintain data integrity[cite: 1].

- Delete Contact:
  - Displays an indexed list of contacts for easy selection[cite: 1].
  - Features a **two-step confirmation prompt** to prevent accidental deletion[cite: 1].

- Persistent CSV Storage:
  - Automatically reads from, appends to, and updates data stored in a local `.csv` file[cite: 1].

---

##  Tech Stack & Requirements

- **Language**: Python 3.x[cite: 1]
- **Standard Libraries**: `csv`, `re` (built-in)
- **Data Persistence**: CSV File (`contacts.csv`)[cite: 1]

---

## Getting Started

### Prerequisites
Make sure Python 3 is installed on your computer. You can check your version in terminal/command prompt:
```bash
python --version
# or
python3 --version