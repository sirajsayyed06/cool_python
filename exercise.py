import os

# Exercise 1: Calculate the multiplication and sum of two numbers
def addition():
    x = int(input("Enter the number: "))
    y = int(input("Enter the number: "))
    if (x*y>1000):
        print("The result is", x+y)
    else:
        print("The result is", x*y)

# Exercise 2: Print the Sum of a Current Number and a Previous number
def sumOfnum():
    a = 0
    b = 0
    for i in range(11):
        b = a + i
        print(f"Current Number {i} Previous Number  {a}  Sum:  {b}")
        a = i

# Exercise 3: Print characters present at an even index number
def printChar():
    str = input("Enter the String: ")
    for i in range(len(str)):
        if (i%2==0):
            print(str[i])

# Exercise 4: Remove first n characters from a string
def removeChar(str, no):
    print(str[no:])

# Exercise 5: Check if the first and last numbers of a list are the same
def checkElements(list):
    if (list[0] == list[-1]):
        return True
    else:
        return False

# Exercise 6: Display numbers divisible by 5
def divisibleBy5(list):
    for i in list:
        if (i%5==0):
            print(i)

# Exercise 7: Find the number of occurrences of a substring in a string
def countChar(str, word):
    print(str.count(word))

# countChar("Emma is good developer. Emma is a writer", "is")

# Exercise 8: Print the following pattern
def pattern():
    for i in range(6):
        for j in range(i):
            print(i, end=" ")
        print(" ")

# Exercise 9: Check Palindrome Number
def checkPalindrome(num):
    print("original number", num)
    onum = num
    reverse_num = 0
    while num > 0:
        reminder = num % 10
        reverse_num = (reverse_num * 10) + reminder
        num = num // 10

    if onum == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

# Exercise 10: Merge two lists using the following condition
def mergeList(list1, list2):
    list = []
    for i in list1:
        if (i%2!=0):
            list.append(i)

    for i in list2:
        if (i%2==0):
            list.append(i)

    print(list)

# Exercise 11: Get each digit from a number in the reverse order.
def reverseOrder(num):
    while num > 0:
        print(num % 10, end=" ")
        num = num // 10

# Exercise 12: Calculate income tax

# Exercise 13: Print multiplication table from 1 to 10
def table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i*j, end=" ")
        print()

# Exercise 14: Print a downward half-pyramid pattern of stars
def patternDown():
    for i in range(6, 0, -1):
        for j in range(i-1):
            print("*", end=" ")
        print()

# Exercise 15: Get an int value of base raises to the power of exponent
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)


# Python Input and Output Exercise
# Exercise 1: Accept numbers from a user
def mul():
    n1 = int(input("Enter the number: "))
    n2 = int(input("Enter the number: "))
    print(n1*n2)

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# print('Name', 'Is', 'James', sep="**")

# Exercise 3: Convert Decimal number to octal using print() output formatting
# num = 8
# print("%o"% num)

# Exercise 4: Display float number with 2 decimal places using
# num1 = 458.541315
# print("%.2f"% num1)

# Exercise 5: Accept a list of 5 float numbers as an input from the user
def createList():
    numbers = []
    for i in range(5):
        num = float(input("Enter the number: "))
        numbers.append(num)
    print(numbers)

# Exercise 6: Write all content of a given file into a new file by skipping line number 5

# Exercise 7: Accept any three string from one input() call
def acceptName():
    name = input("Enter the full name: ")
    for i in name.split(" "):
        print("Name = ", i)

# Exercise 8: Format variables using a string.format() method
def stringFormat():
    totalMoney = 1000
    quantity = 3
    price = 450
    print(f"I have {totalMoney} dollars so I can buy 3{quantity} football for {float(price)} dollars.")

# Exercise 9: Check file is empty or not
def checkFile():
    size = os.stat("test.txt").st_size
    if size == 0:
        print('file is empty')

# Exercise 10: Read line number 4 from the following file
def checkLine():
    with open('test.txt', 'r') as fp:
        lines = fp.readlines()
        print(lines[3])

# Python Loop Exercises
# Exercise 1: Print first 10 natural numbers using while loop
# for i in range(1, 11):
#     print(i)

# Exercise 3: Calculate sum of all numbers from 1 to a given number
# num = 0
# for i in range(1, 11):
#     num += i
# print(num)

# Exercise 4: Print multiplication table of a given number
# num = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(num*i)

# Exercise 5: Display numbers from a list using a loop

# Exercise 6: Count the total number of digits in a number
num = 75869
count = 0
while num > 0:
    num = num // 10
    count +=1
print(count)
