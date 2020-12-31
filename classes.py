# Create a class
class User:
    # Constructor goes here
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email

    # def greetings(self):
    #     return f'My name is {self.name} and I am {self.age} amd my balance is {self.balance}'

    def has_birthday(self):
        self.age += 1

# Extend class (inheritence)
class Customer(User):
    # Constructor goes here
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email
        self.balance = 0

    def greetings(self):
        return f'My name is {self.name} and I am {self.age} amd my balance is {self.balance}'

# Method for customer
    def set_balance(self, balance):
        self.balance = balance

# Initialize customer
janet = Customer('Janet', 'janet@gmail.com', 25)
janet.set_balance(500)
print(janet.greetings())


# Init object (Users class)
# brad = User('Traversy', 'traversy@gmail.com', 21)
# brad.has_birthday()
# print(brad.greetings())