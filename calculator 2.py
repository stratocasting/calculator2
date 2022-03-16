def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

num1 = int(input ("what is the first number? :"))
num2 = int(input ("what is the seccond number? :"))
for symbol in operations:
    print (symbol)
operation_symbol = input("pick an operation:\n")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print (f"{num1} {num2} = {answer}")
