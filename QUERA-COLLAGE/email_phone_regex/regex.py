import re


def validate_email(email: str) -> bool:
    if re.match(r'^[a-zA-Z1-9\.\_]+@[a-zA-Z1-9]+\.[a-zA-Z]{3}$', email):
        return True
    else:
        return False


def validate_phone(number: str) -> bool:

    if re.match(r'((^09)[0-9]{9})?(^\+989[0-9]{9})?(^00989[0-9]{9})?$', number):
        return True
    else:
        return False
