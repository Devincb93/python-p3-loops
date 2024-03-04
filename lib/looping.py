#!/usr/bin/env python3

def happy_new_year():
   i = 11
   while i > 0:
    i -= 1
    print(f'{i}')
    print ("Happy New Year!")
    

   
    pass

def square_integers(int_list):
    squared_integers = []
    for integer in int_list:
       squared_integer = integer ** 2
       squared_integers.append(squared_integer)
    return squared_integers
    

def fizzbuzz():
    i = 0
    while i < 100:
       i += 1
       
       if (i % 3 == 0 and i % 5 == 0):
          print ("FizzBuzz")
       elif (i % 5 == 0):
          print ("Buzz")
       elif (i % 3 == 0):
          print("Fizz")
       else:
          print(f'{i}')
       
   
