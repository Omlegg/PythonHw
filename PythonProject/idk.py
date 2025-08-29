import math
import random
import calendar

# #1
# name = input("Enter your name: ")
# age = input("Enter your age: ")
#
# print(f"Hello {name}! You will be {age+1} years old next year. ")
#
# #2
# num = int(input("Enter a number: "))
#
# if num%2:
#     print("The number is even")
# else:
#     print("The number is odd")
#
# #3
# num = int(input("Enter a number: "))
# fin_num = num
#
# for i in range(num):
#     fin_num = fin_num*i
#
# print(f"Factorial of that number is {fin_num}")

# #4
# for i in range(20):
#     if(math.sqrt(i) % 1 == 0):
#         print(i)
#
# #5
# word= input("Enter a word: ")
# fin_word = ""
# for letter in word:
#     fin_word = letter+fin_word
#
# if(fin_word == word):
#     print("This word is a palindrome")
# else:
#     print("This word is not a palindrome")
#6
# word= input("Enter a word: ")
# fin = dict()
# for letter in word:
#     if letter not in fin:
#         fin[letter] = 1
#     else:
#         fin[letter] += 1
# print(fin)
#7
# word_arr = []
# for i in range(5):
#     word_arr.append(input("Enter a word: "))
#
# word_arr.sort()
# print(word_arr)
#7.5
# word_arr = []
# for i in range(5):
#     word_arr.append(input("Enter a word: "))
#
# for i in range(len(word_arr)):
#     for j in range(len(word_arr)):
#         if word_arr[i] < word_arr[j]:
#             word_arr[i], word_arr[j] = word_arr[j], word_arr[i]
#
# print(word_arr)
#8
# symbol_arr=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","_","&","$","(",")"]
# password=""
# n_length= int(input("Enter length of password: "))
# for i in range(n_length):
#     password = password + symbol_arr[random.randint(0,len(symbol_arr)-1)]
# print(password)
#9
# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr2 = [11, 2, 13, 14, 5, 16, 17, 18, 19]
# fin_arr = arr1.copy()
# for i in range(0, len(arr2)):
#     if arr2[i] not in fin_arr:
#         fin_arr.append(arr2[i])
# print(fin_arr)
#10
# with open('input.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#
# lines = text.splitlines()
# num_lines = len(lines)
#
# words = text.split()
# num_words = len(words)
#
# num_chars = len(text)
#
# print(f'Строк: {num_lines}')
# print(f'Слов: {num_words}')
# print(f'Символов: {num_chars}')
#11
# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max_v = arr1[0]
# for i in range(0, len(arr1)):
#     if arr1[i] > max_v:
#         max_v = arr1[i]
# print(max_v)
#12
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#
#     result = num1 / num2
#
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Please enter valid numbers.")
# else:
#     print(f"Result of division: {result}")
#13
# numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 != 0]
# print(numbers)
#14
import calendar

try:
    # User input
    year = int(input("Enter the year (e.g., 2025): "))
    month = int(input("Enter the month (1-12): "))

    # Validate month
    if 1 <= month <= 12:
        # Print the calendar for the specified month and year
        print("\n" + calendar.month(year, month))
    else:
        print("Error: Month must be between 1 and 12.")

except ValueError:
    print("Error: Please enter valid integers for year and month.")