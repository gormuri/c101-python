#!/opt/python3/bin/python3
# -*- coding: utf-8 -*-
import math

# ported my php basic prime number function
def is_prime(number):
        # we need to try divide every number from 2 up to square root of the number we are testing
        # to make sure that we have a prime number
        for n in range(2,int(math.sqrt(number))):
                # found a way to include the modulus YAY !
                # if we don't have a remander we dont have a prime number
                if number % n == 0:
                        return False
                        break
        # if we don't find a divider we have a prime *YAY*
        return True

# on to opening file and doing some math stuff ...
#open a file in reading mode
number_file_pointer = open('14-1.txt', 'r')

#read from the file in to a list by spliting the numbers usint the commas
numbers = number_file_pointer.read().split(',')

#some vars used for the output at the end.
sum = 0
max = 0
min = int(numbers[0]) #setting this to the first value just to set it to some value in the list

#lets itterate throug the list and do some magic !
for num in numbers:
        #don't want to to int(num) every time :D
        num = int(num)

        # the easy stuff .. lets do some adding :D
        sum += num

        # next up lets find the smalles number in the list
        if num < min :
                min = num

        # lets find the largest number
        if max < num:
                max = num

        # lets see if the number is a prime number !
        if is_prime(num):
                print(num , ' is a prime number')

# and then just print out the results note I use print() becouse I'm using python3  but should run fine in python 2
print('the sum of all the numbers in our file is: ' , sum)
print('the largest number in our file is: ' , max)
print('the smalest number in our file is: ' , min)

#close your file ! recomended when you are done allso if writing to files
# you need to do this so your data is written ?
number_file_pointer.close()
