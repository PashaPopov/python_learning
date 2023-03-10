# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import sys
import area
import area as ar
from area import AreaOfCircle as circle, AreaOfRectangle as rectangle
from area import *


# def fib(value):
#     if value < 0 or value == 0:
#         return 0
#     elif value == 1:
#         return 1
#     else:
#         return value * fib(value - 1)

# a = 8
#
# def TestVar():
#     global a
#     a = a + 4
#     print('value of a = ', a)
#
# TestVar()
# print (a)
# z = 9
# def TestVar():
#     z = 15
#     z = z + 20
#     globals()['z'] = globals()['z'] + 10
#     print('value of local z = ', z)
#     print('value of global z = ', globals()['z'])
#
# TestVar()
# print(z)

def print_hi(name):

    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # inp = int(input('Provide input: '))
    # print(fib(inp))
    # print(8//2)
    # print(5//2)
    # print((9+8)*5-6)
    # print(3*3*3*3)
    # print(3**4)
    # print(6/2)
    # print(7/2)
    # print(7%2)
    #
    # x = 5
    # x += 2
    # print(x)
    # x, y, z = 5, 3, 7
    # print(x, y, -z)
    #
    # print(6 != 7)
    #
    # a, b = 5, 9
    # print(a < 6 and b > 7)
    # print(a > 6 and b < 7)
    # print(a < 6 and b < 7)
    # print(a > 6 and b > 7)
    # print(a > 6 and b > 7)
    # print(a < 6 and b > 7)
    # print(a < 6 or b > 7)
    # print(a > 6 or b > 7)
    # print(a < 6 or b < 7)
    # print(a > 6 or b < 7)
    # print(not (a < 6))

    # print('boston')
    # print("boston")
    # print('boston\'s population')
    # print("boston\"s population")
    # print('President said, "we\'ll control the pandemic"')
    #
    # print('New ' + 'York')
    # print(4 * 'bla..')
    # a = 'gravity'
    # b = '1966'
    # print(a+b)
    # print(f'Newton discovered {a} in {b}')
    # print('Newton discovered {} in {}'.format(a, b))

    # s = 'pythongeek'
    #
    # print(s[-1])
    # print(s[9])
    # print(s[0:4])
    # print(s[2:6])
    # print(s[2:6])
    # print(s[4:])
    # print(s[-4:])
    # print(s[:4])
    # print(s[4:14])
    # print(s[4:14])
    # print(s[2:-2])
    # print(s[:6])
    # print(s[:6] + ' rocks')
    # del s
    # print(s)
    # x = 'USA'
    # y = 5
    # print(id(x))
    # z=x
    # print(id(z))

    # a = 1  # перше число
    # b = 1  # друге число
    # count = 10
    # print(a)  # виводимо перше число
    # print(b)
    # for i in range(count-2):  # повторюємо два рази для третього і четвертого числа
    #     c = a + b # обчислюємо наступне число як суму попередніх двох
    #     print(c)  # виводимо наступне число
    #     a = b  # оновлюємо значення першого числа як друге число
    #     b = c  # оновлюємо значення другого числа як наступне число
    # a = int(input('Provide int number: '))
    # b = int(input('Provide int number: '))
    # r = 'Numbers are equal' if (a == b) else 'Numbers are not equal'
    # print(r)
    # import sys
    # country = input('input country - A or B : ').upper() or ' '
    # weight = int(input('input parcel weight in Kgs : ') or 0)
    # if country in ['A', 'B'] and weight > 0:
    #     if country == 'A':
    #         if weight <= 10:
    #             charge = '$5'
    #         elif weight <= 30:
    #             charge = '$10'
    #         else:
    #             charge = '$20'
    #
    #     if country == 'B':
    #         if weight <= 10:
    #             charge = '$7'
    #         elif weight <= 30:
    #             charge = '$12'
    #         else:
    #             charge = '$22'
    # else:
    #     print('country A or B & weight above zero only allowed')
    #     sys.exit()
    # print(f'charges for delivery in {country} are {charge}')

    # '''Program to demonstrate While Loop
    #
    # User has to input a positive number until which
    # program will print all the even numbers
    # starting the range from 0
    # '''
    # import sys
    # print('Program to print even numbers in positive range')
    # cnt = 0
    # lim = int(input('input positive number to set range : ') or 0)
    # if lim < 0:
    #     print('negative range is not allowed')
    #     sys.exit()
    # while cnt <= lim:
    #     if cnt % 2 == 0:
    #         print(cnt, 'is an even number')
    #     cnt += 1
    # print('All even numbers up to', lim)

    # Program to demostrate Python For... loop
    # '''Prints all even numbers in the given range
    #
    #    Write a program to print all the +ve even numbers in
    #    given range of two numbers. User to input the start
    #    and end numbers of the range. The end number is to be
    #    included. Remember that end number by default is excluded
    #    from the range.
    # '''
    # print('Program to print even numbers in positive range')
    # StartNum = int(input('Input starting number (lower) : ') or 0)
    # EndNum = int(input('Input ending number (higher) : ') or 0)
    # if StartNum < EndNum and StartNum >= 0 and EndNum >= 0:
    #     z = range(StartNum, EndNum + 1)  # EndNum + 1 to include the end number
    #     for i in z:
    #         if i % 2 == 0:
    #             print(i, 'is even number')
    #     else:
    #         print(f'all even numbers between {StartNum} and {EndNum}')
    # else:
    #     print('Not valid range')

    # program code starts below
    # print('Program to check if word is palindrome')
    # word = input('input the word here (max length 30) : ') or ' '
    # word_lower = word.lower()
    # # upper() is used to convert the whole string into uniformly upper case
    # x = ''  # x initialized to none i.e. empty string
    # print(x)
    # if word_lower != ' ' or len(word_lower) > 30:
    #     for i in word_lower:
    #         x = i + x
    #         print(x) #remove '#' before print to understand how it works
    #     else:
    #         if x == word_lower:
    #             print(f'{word} is palindrome')
    #         else:
    #             print(f'{word} is not palindrome')
    # else:
    #     print("word can't be blank or longer than 30")

    # '''Program to find first number divisible by 3 & 5
    #
    # Write a program to print the first +ve number 'n' in a given
    # range found to be divisiable by 3 as well as 5.
    # input -> two numbers for a range r1(lower) & r2(higher)
    # Result output -> <n> is first number divisible by 3 & 5 between <r1> & <r2>
    # '''
    # print('Find first number divisible by 3 & 5 in given range')
    # r1 = int(input('Enter lower range number : ') or 0)
    # r2 = int(input('Enter higher range number : ') or 0)
    # if r1 != r2:
    #     rng = range(r1, r2 + 1)
    #     for i in rng:
    #         if i % 3 == 0 and i % 5 == 0:
    #             print(f'{i} is divisible by 3 & 5 in range {r1} to {r2}')
    #             #break  # comment break while you uncomment the print below
    #         # print(f'{i} not divisible by 3 & 5')#uncomment print to understand break for study
    #     else:
    #         print(f"There's no number divisible by 3 & 5 between {r1} to {r2}")
    # else:
    #     print('not valid range')

    # '''Guess the number from 0 to 20 in 5 attemps
    #     '''
    # print('Guess number from 0 to 20')
    # value = random.randrange(0, 20, 1)
    # print(value)
    #
    # rng = range(0, 6)
    # for i in rng:
    #     prov = int(input('Try to guess: '))
    #     if prov == value:
    #         print(f'Your input {prov} matched')
    #         break
    #         # print(f'{i} not divisible by 3 & 5')#uncomment print to understand break for study
    #     else:
    #         print(f'Your input {prov} is not what was guessed')

    # ''' Program to print positive numbers divisible by 3 in given range
    #
    # write a program to print all such numbers in a given range
    # which are divisible by 3 while skipping all those which are not
    # input -> r1(lower range limit) r2(higher range limit)
    # output -> n is divisible by 3
    # '''
    # # Below is the program
    # print('Find numbers divisible by 3 in given range')
    # r1 = int(input('Enter lower range number : ') or 0)
    # r2 = int(input('Enter higher range number : ') or 0)
    # if r1 != r2:
    #     rng = range(r1, r2 + 1)
    #     for i in rng:
    #         if i % 3 != 0:
    #             continue  # this statement jumps loop to next iteration
    #         print(f'{i} divisible by 3')
    #     else:
    #         print(f"All numbers divisible by 3 between {r1} to {r2} printed")
    # else:
    #     print('not valid range')

    # ''' Program to print positive numbers divisible by 3 in given range
    #
    # write a program to print all such numbers in a given range
    # which are divisible by 3 while skipping all those which are not
    # input -> r1(lower range limit) r2(higher range limit)
    # output -> n is divisible by 3
    # Use "pass" statement
    # '''
    # # Below is the program
    # print('Find numbers divisible by 3 in given range')
    # r1 = int(input('Enter lower range number : ') or 0)
    # r2 = int(input('Enter higher range number : ') or 0)
    # if r1 != r2:
    #     rng = range(r1, r2 + 1)
    #     for i in rng:
    #         if i % 3 != 0:
    #             pass
    #         else:
    #             print(f'{i} divisible by 3')
    #     else:
    #         print(f"All numbers divisible by 3 between {r1} to {r2} printed")
    # else:
    #     print('not valid range')

    # ''' Program to compare numbers
    # '''
    # # Below is the program
    # print('Program to compare two numbers')
    # r1 = input('Enter 1st number : ')
    # r2 = input('Enter 2nd : ')
    # try:
    #     num1 = int(r1)
    #     num2 = int(r2)
    #     if num1< 0 or num2 < 0:
    #         raise Exception('Only positive integers allowed')
    # except ValueError:
    #     print('Wrong input - only integers allowed')
    # except Exception as e:
    #     print('ERROR : ', e)
    # else:
    #     if num1 == num2:
    #         print('Numbers are equal')
    #     elif num1>num2:
    #         print('Num1 is greater than Num2')
    #     else:
    #         print('Num2 is greater than Num1')
    #
    # print('blablabla')

    # x = int(input('Input an integer less than 100 : ') or 0)
    # if x>100:
    #     raise Exception('you must enter number less than 100')
    # else:
    #     print(f'the number you entered {x}')

    # def greet():
    #     print('Welcome')
    #
    # #greet()
    #
    # def greet(name = 'test'):
    #     print('Welcome', name)
    #
    # greet('Pasha')
    #
    # greet()

    # def AddNum(n1, n2):
    #     sum = n1 + n2
    #     return sum
    # x = AddNum(3, 5)
    # print(x)
    #
    # def CalcInterest (amount, days, interest  = 5):
    #     i = amount * (days / 365) * (interest / 100)
    #     return i
    #
    # x = CalcInterest(1000, 100)
    # print(x)
    # x = CalcInterest(1000, 100, 4)
    # print(x)
    #
    # x = CalcInterest(days=100, interest=4, amount=1000)
    # print(x)
    # x = CalcInterest(days=100, amount=1000)
    # print(x)
    #
    # def AvgMarks (*marks):
    #     i = 0
    #     n = 0
    #     for m in marks:
    #         n = n + m
    #         i += 1
    #     avg = n / i
    #     return avg
    #
    # x = AvgMarks(21, 51, 25, 32, 26, 30)
    # print(x)

    # x = (lambda amt, days, rate : amt * (days/ 365) * (rate / 100)) (1000, 100, 4)
    # print(x)
    # interest = (lambda amt, days, rate : amt * (days/ 365) * (rate / 100))
    # x = interest(1000, 100, 4)
    # print(x)
    #
    # def div7 (num):
    #     if num % 7 == 0:
    #         return True
    #     else:
    #         return False
    # rng = range(4, 30)
    # x = filter(div7, rng)
    # print(list(x))
    # x1 = filter(lambda y: y % 7 == 0, rng)
    # print(list(x1))

    # def greet(name):
    #     print('welcome', name)
    #
    # greet('Pasha')
    #
    # def fact(num):
    #     if num < 0:
    #         return 'Only positive integers'
    #     elif num == 1:
    #         return 1
    #     else:
    #         return num * fact(num-1)
    #
    # x = fact(6)
    # print(x)

    # x = 5
    # print(x)
    #
    # def TestVar():
    #     x = 10
    #     print('values of x inside the function = ', x)
    #
    # TestVar()
    #
    # def TestVar():
    #     x = 10
    #     y = 7
    #     print('value of x inside the function', x)
    #     print('value of x inside the function', y)
    #
    # TestVar()
    # # print('value of x inside the function', y)
    # a = 8
    # def TestVar():
    #     print('value of a inside the function', a)
    #
    # TestVar()
    #
    # def TestVar():
    #     print('value of a expression involving variable a = ', a + 4)
    #
    # TestVar()
    #
    # def TestVar():
    #     a = a + 4
    #     print('value of a expression involving variable a = ', a)
    #
    # TestVar()

    # a = 8

    # def TestVar():
    #
    #     x = area.AreaOfCircle(10)
    #     print(x)
    #
    #     x1 = area.AreaOfRectangle(10, 20)
    #     print(x1)
    #
    #     x2 = area.AreaOfTriangele(10, 5)
    #     print(x2)
    #
    #     x3 = circle(15)
    #     print(x3)
    #     print(AreaOfCircle(27))
    #
    # TestVar()
    # def nestedFunct(user):
    #     def inner ():
    #         print('Hello! ' + user)
    #     inner()
    #
    # nestedFunct('User')
    #
    # def GetValue(n):
    #     print('value of n in outer func = ', n)
    #     def ChangeValue():
    #         nonlocal n
    #         n = n + 5
    #         print('value of n after change in inner function = ', n)
    #     ChangeValue()
    #
    # GetValue(12)

    # def Closures(num1, num2):
    #     return num1+num2
    #
    # #print(Closures)
    # x = Closures(10, 20)
    # print(x)
    # x = Closures
    # print(x(10, 20))
    #
    # def expon(exp):
    #     def power(base):
    #         result = base ** exp
    #         return result
    #     return power
    # square = expon(2)
    # cube = expon(3)
    # SquareRoot = expon(1/2)
    # CubeRoot  = expon(1/3)
    # print(square(5), cube(5))

    # def IncNum(x):
    #     return x + 1
    # def DecNum(x):
    #     return x - 1
    #
    # def TweakNum(func, x):
    #     result = func(x)
    #     return result
    #
    # print(TweakNum(IncNum, 10))
    # print(TweakNum(DecNum, 10))

    # def AddNumbers(a, b):
    #     return a + b
    # print('the name of module running = ', __name__)
    # x = int(input('first num = '))
    # y = int(input('second num = '))
    # z = AddNumbers(x, y)
    # print('the sum of numbers is', z)

    # Definition of function SalCalc with call to AddNumbers





# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
