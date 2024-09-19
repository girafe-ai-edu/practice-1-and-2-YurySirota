# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""

my_digit = str(input("введите четырехзначное число: "))

print( f" Сумма числ равна = { int(my_digit[0]) + int(my_digit[1]) + int(my_digit[2]) + int(my_digit[3])  }  " )


