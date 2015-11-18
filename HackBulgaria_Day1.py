#Programming101-Python/week01 First Problems

#Sum of all digits of a number
def sum_of_digits(n):
    n = abs(n)
    n = str(n)
    n = list(n)
    result = 0
    for i in range (0, len(n)):
        result += int(n[i])
    return result



#Turn a number into a list of digits
def to_digits(n):
    n = abs(n)
    n = str(n)
    n = list(n)
    return n



#Turn a list of digits into a number
def to_number(n):
    new = map(str, n)
    new = "".join(new)
    new = int(new)
    return new



#Factorial Digits
from math import factorial

def fact_digits(n):
    n = str(n)
    n = list(n)
    total = 0
    
    for num in n:
        num = int(num)
        fac = factorial(num)
        total += fac
    return total



#First nth members of Fibonacci
def fibonacci(n):
    new = []
    a = 1
    b = 1

    for i in range( 0, n):
        new.append(a)
        a, b = b, a+b
    return new



#Fibonacci number
def fib_fibonacci(n):
    new = []
    a = 1
    b = 1

    for i in range( 0, n):
        new.append(a)
        a, b = b, a+b
    num = map(str, new)
    num = "".join(num)
    num = int(num)
    return num



#Palindrome
def palindrome(n):
    n = str(n)
    n = list(n)
    lenght = len(n)
    new = []

    while lenght != 0:
        new.append(n[lenght-1])
        lenght -= 1
    if n == new:
        return True
    elif n != new:
        return False



#Vowels in a string
def count_vowels(str):
    str = str.lower()
    str = list(str)
    total = 0

    for i in str:
        if i == "a":
            total += 1
        elif i == "e":
            total += 1
        elif i == "i":
            total += 1
        elif i == "o":
            total += 1
        elif i == "u":
            total += 1
        elif i == "y":
            total += 1
    return total



#Consonants in a string
def count_consonants(str):
    str = str.lower()
    str = list(str)
    total = 0

    for i in str:
        if i !="a" and i != "e" and i != "i" and i != "y" and i != "o" and i != "u" and i != "!" and i!= " " and i != "," and i != "?" and i != "." and i != "/":
            total += 1
    return total



#Char Histogram
def char_histogram(string):
   string = list(string)
   dict = {}

   for char in string:
       for i in range(0, len(string)):
           occurance = 0
           if char == string[i]:
               occurance += 1
           dict.update({char: occurance})
   return dict






#Additional problems for solving from 
#Programming101-3/week1-Python-Problems/1-Warmups

#Palindrome Score
Score = 1
def str_to_int(n):
    new = map(str, n)
    new = "".join(new)
    new = int(new)
    return new


def p_score(n):
    global Score
    n = str(n)
    n = list(n)
    lenght = len(n)
    new = []

    while lenght != 0:
        new.append(n[lenght-1])
        lenght -= 1

    if n == new:
        newscore = Score
        Score = 1
        return newscore
    else:
        Score += 1
        q = str_to_int(n) + str_to_int(new)
        return p_score(q)



#My first understanding of Palindrome Score - If a number is a polindrome to add 1 to overall score and to add the polindrome to the old number. This cycle will be active until the sum is not a palindrome.
def str_to_int(n):
    new = map(str, n)
    new = "".join(new)
    new = int(new)
    return new

def palindrome(n):
    n = str(n)
    n = list(n)
    lenght = len(n)
    new = []

    while lenght != 0:
        new.append(n[lenght-1])
        lenght -= 1

    if n == new:
        new = str_to_int(new)
        return new
    elif n != new:
        return False


def p_score(n):
    score = 0
    while palindrome(n) is not False:
        n = (n + palindrome(n))
        score += 1
    return score



#Hack Numbers
def palindrome(n):
    n = str(n)
    n = list(n)
    lenght = len(n)
    new = []
    while lenght != 0:
        new.append(n[lenght-1])
        lenght -= 1
    if n == new:
        return True
    elif n != new:
        return False


def int_to_binary(n):
    binary = bin(n)[2:]
    return binary


def odd_check(n):
    n = str(n)
    n = list(n)
    total = 0
    for num in n:
        if num == "1":
            total += 1
    if total % 2 != 0:
        return True
    else:
        return False



def hack(n):
    new = int_to_binary(n)
    if palindrome(new) is True:
        if odd_check(new) is True:
            return True
        else:
            return False
    else:
        return False


def next_hack(n):
    new = n
    end = False
    while end is False:
        if hack(new) is not True:
            new += 1
        else:
            end = True
    return new