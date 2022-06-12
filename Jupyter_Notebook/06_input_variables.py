# CHAPTER 06 - INPUT VARIABLES

import msilib


fruit_basket = "Mangoes"
print(fruit_basket)

# Input function simple

fruit_basket = input("Which is your favorite fruit?")
print(fruit_basket)

# Input function of second stage

name = input("What is your name? ")
greetings = "Hello"
print(greetings, name)

# Another way of second stage input function

name = input("What is your name? ")
print("Hello", name)

# Third stage input function

name = input("What is your name? ")
age = input("How old are you? " )
greetings = "Hello"
print(greetings, name, ", You are still young!")