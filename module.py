# Module is a file containing a set of function to include in your own application
# There are core python modules, you can istall using pip package manager (including Django) as well as custom modules

# Core Modules
import datetime
from datetime import date
import time

# import Camelcase PIP Module
from camelcase import CamelCase

# import custom module
import validator
from validator import validate_email

# Date
today = date.today()

# Time
timestamp = time.time()
print(today, timestamp)

# PIP Package Manager
c = CamelCase()
print(c.hump('hello there world'))


# custom module
email = 'test#email.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is invalid')
