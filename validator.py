import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$", email))