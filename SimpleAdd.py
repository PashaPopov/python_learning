# Function definition of AddNumbers
def AddNumbers(a, b):
    return a + b


# executable code of SimpleAdd module calling AddNumbers function
if __name__ == '__main__':
      x = int(input('input the value of first number = '))
      y = int(input('input the value of second number = '))
      z = AddNumbers(x, y)
      print('The sum of two numbers = ', z)

# print('the name of module running = ', __name__)
# x = int(input('input the value of first number = '))
# y = int(input('input the value of second number = '))
# z = AddNumbers(x, y)
# print('The sum of two numbers = ', z)
