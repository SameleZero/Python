# Q086
# Created by JKChang
# 09/05/2017, 15:37
# Tag: 
# Description: By using list comprehension, please write a program to print the list after removing delete numbers
#              which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

li = [12, 24, 35, 70, 88, 120, 155]
l = [x for x in li if x % 5 != 0 and x % 7 != 0]
print l
