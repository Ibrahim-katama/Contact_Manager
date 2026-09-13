import re

def validate_name(name, allow_blank=False):
    #Ensures the name contains only letters
    if allow_blank and not name:
        return True
    return name.isalpha()

def validate_number(number, allow_blank=False):
    #Ensures the phone number is exactly 10 digits
    if allow_blank and not number:
        return True
    return number.isdigit() and len(number) == 10

def validate_email(email, allow_blank=False):
    #Validates standard email formatting using Regex
    if allow_blank and not email:
        return True
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))