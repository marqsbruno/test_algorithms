""" Create a hashmap (or a simple object in PHP) that contains the elementary functions of addition, subtraction, multiplication, and division.
Take into account that the division must not allow 0 dividend
The sum function allows an array as an input parameter and adds all its elements.
The subtraction function allows an array as an input parameter and subtracts all its elements.
Multiplication Function - Ditto
The division function accepts two parameters: a and b.
 """

list = [2, 3, 5, 10, 0]


def addition(list):
    result = 0
    for i in range(len(list)):
        result = result + list[i]

    return result


def subtraction(list):
    result = 0
    for i in range(len(list)):
        result = result - list[i]

    return result


def multiplication(list):
    result = 1
    for i in range(len(list)):
        result = result * list[i]

    return result


def division(a, b):

    result = a / b
    return result


print(addition(list))
print(subtraction(list))
print(multiplication(list))
print(division(6, 2))
