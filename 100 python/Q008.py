# Q008
# Created by JKChang
# 23/02/2017, 14:28
# Description: Write a program that accepts a comma separated sequence of words as input and prints the words in a
#              comma-separated sequence after sorting them alphabetically.
#
# Example: Suppose the following input is supplied to the program:
#          without,hello,bag,world
#          Then, the output should be:
#          bag,hello,without,world

items = [x for x in raw_input().split(',')]
items.sort()
print ','.join(items)