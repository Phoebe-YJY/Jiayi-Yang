# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 00:50:20 2021

@author: Phoebe Yang
"""

# PPHA 30535
# Spring 2021
# Homework 1

# Jiayi Yang
# Phoebe-YJY

# Due date: Sunday April 11th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.
my_list = [1, 2, 3, 4, 5, 6]
for i in my_list:
    print( "The value at position", my_list.index(i), "is", i)
#Inspiration from CSDN https://blog.csdn.net/lachesis999/article/details/53185299



# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results.
my_list = ["radar", "A man, a plan, a canal, Panama!", "Apple and the phrase", "This isn't a palindrome"]
for string in my_list:
    if string == string[::-1]:
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")



# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')
while choice not in available_vegetables:
    choice = input("You made an invalid choice, please pick again: ")
else:
    print("You can have the vegetable.")



# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".
my_list = ["aPPle", "banana", "PEAR", "COCONUT"]
my_newlist = []
for i in my_list:
    if i[0] in ["a", "b"]:
        my_newlist.append(i.lower()) #Inspiration from cnblogs https://www.cnblogs.com/xiaoit/p/4040568.html
print(my_newlist)



# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]
end_list = [i*2 for i in start_list[::-1]]
print(end_list)


# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']
new_dict = dict(zip(short_names, long_names))
print(new_dict)
#Inspiration from CSDN https://blog.csdn.net/sunmingyang1987/article/details/105456275



























