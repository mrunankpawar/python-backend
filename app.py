#  //TODO: Print 

# print("Hello World")
# print("Welcome")

# //TODO: Variables

# name = "Mrunank"
# age = 21

# print(name)
# print(name+ " is a boy")
# print(name, "is", age)
# print(name+ " lives in Pune")

# //TODO: Strings in Python

# name = 'MRUNANK'

# print("Hi.\nHow are you?")

# print(name.upper())
# print(name.lower())
# print(name.isupper())
# print(name.islower())
# print(name.lower().islower()) 
# print(len(name))
# print(name.index('A'))
# print(name.replace("M", "K"))

# //TODO: Numbers in Python

# from math import *

# number = 20
# number2 = str(number)
# print(78)
# print(78 + 54)
# print(78 - 54.34523)
# print(20 / 6)
# print(20 % 6)
# print("The number is : " + number2)
# print(abs(-5))
# print(max(10, 6, -12, 15))
# print(min(10, 6, -12, 15))
# print(round(3.6))
# print(round(3.2)) 
# print(bin(5401))
# print(sqrt(100))

# //TODO: User input

# name = input("What's your name: ")
# age = input("What's your age: ")
# print("My name is", name, "and I'm", age, "years old")

# //TODO: Replace word in a sentence

# sentence = input("Enter your sentence: ")
# print('Your sentence is: ', sentence)
# word1 = input("Enter the word to replace: ")
# word2 = input("Enter the word to replace it with: ")
# print(sentence.replace(word1, word2))

# // TODO: Lists in Python

# countries = ['India', 10, True, 'United States']
# countries2 = list(('India', 10, True, 'United States'))
# countries[0] = "South Africa"
# print(countries[2][:3])
# print(countries[1:])
# print(countries[1:3])
# print(countries)
# print(type(countries))
# print(countries[-1])
# print(len(countries))

# //TODO: List methods 

list1 = [3, 2, 4, 1, 5]
list2 = ['banana', 'apple', 'mango', 'oranges', 'mango']

# list2.append('cherry')
# list2.insert(1, 'cherry')
# list2.remove('banana')
# list2.clear()
# print(list2.index('mango'))
# print(list2.count('mango'))
# list1.sort()
# print(list1)
# list3 = list2.copy()
# list2.reverse()
# list2.pop()
# print(list2)
# list2.pop(2)
# del list2[0]
# print(list3)
# print(list2)


# list1.extend(list2)
# print(list1)

# TODO: Tuples in python

# numbers = (1, 2, 3, 1)
# tuple_contructor = tuple((1, 3, 'hello', False))
# strings = ('home', 'house', 'villa', True, 3)
# print(strings)
# print(type(tuple_contructor))
# three_numbers[1] = 5 [ERROR] 
# print(numbers)
# print(numbers[0])
# print(type(numbers))
# print(len(numbers))
# print(type(strings[3]))

# TODO: Functions in Python

def greetings_function(name, age):
    print("Welcome " + str(name) + '. You are ' + str(age) + ' years old!')

name = input("Enter your name: ")
age = input("Enter your age: ")
greetings_function(name, age)

# def greeting_function(*names):
#     print("Welcome " + names[2])

# greeting_function('Mrunank', 'Vaibhav', 'Piyush')



