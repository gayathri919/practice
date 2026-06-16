Simple Python program with enhancements
Print a message
print("Welcome to Python practice!")

Do some math
a = 10
b = 4
sum_result = a + b
product_result = a * b
print(f"The sum of {a} and {b} is: {sum_result}")
print(f"The product of {a} and {b} is: {product_result}")

Use a loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

Define a function with a conditional
def greet(name, age):
    if age < 18:
        return f"Hello, {name}! You're still young."
    else:
        return f"Hello, {name}! You're an adult now."

print(greet("Nagam", 20))

Ask for user input
user_name = input("Enter your name: ")
print("Nice to meet you,", user_name)