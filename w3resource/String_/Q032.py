# -*- coding: UTF-8 -*-
# Q032
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python program to print the following floating numbers with no decimal places. 
x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with no decimal places: "+"{:.0f}".format(x))
print("Original Number: ", y)
print("Formatted Number with no decimal places: "+"{:.0f}".format(y))
print()