# Write a function calculate that takes in two numbers and a callback function as arguments. The calculate function should call the callback function, passing in the two numbers as arguments, and return the result.


def calculate():
  num1 = float(input('Enter first number: '))
  num2 = float(input('Enter second number: '))
  operation = input('Enter the operation (+, -, *, /): ')

  if operation == '+':
    result = num1 + num2
  elif operation == '-':
    result = num1 - num2
  elif operation == '*':
    result = num1 * num2
  elif operation == '/':
    result = num1 / num2
  else:
    print('Invalid operation entered.')
    return
  print('result: ', result)

calculate()
