# A function is a block of code that only runs when it is called to. In python we don't use curly braces, we use indents with tabs or spaces

# CREATE FUNCTION 
def sayHello(name):
    print(f'Hello {name}')

def getSum(num1, num2):
    total = num1 + num2
    return total

# A lambda function is a samll anaonymous function 
# A lambda function can take any number of arguments but can only have one expression. Similar to JS arrow function

getDiff = lambda num1, num2: num1 - num2
num = getDiff(10,5)
print(num)
