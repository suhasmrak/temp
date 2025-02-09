from collections import Counter

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("The sum of the list is:", total)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = 10
print("Fibonacci sequence:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")


def is_palindrome(s):
    return s == s[::-1]

word = "racecar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")



items = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
count = Counter(items)
print("Element counts:", count)


def calculator():
    operation = input("Enter operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation!")
        return

    print(f"The result is: {result}")

calculator()
