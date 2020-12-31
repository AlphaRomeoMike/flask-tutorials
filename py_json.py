import json

# Sample data
userJSON = '{"firstName": "John", "lastName": "Doe", "Age": 3}'

# Parse to a Dictioniary
user = json.loads(userJSON)
print(user['firstName'])