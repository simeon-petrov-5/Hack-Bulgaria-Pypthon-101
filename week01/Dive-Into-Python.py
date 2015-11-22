#Is Number Balanced?
def is_number_balanced(n):
    if n <10 and n >= 0:
        return True
    n = str(n)
    n = list(n)
    middle = int(len(n) / 2)
    total1 = 0
    total2 = 0
    back = n[::-1]
    for num in range(0, middle):
        total1 += int(n[num])
        total2 += int(back[num])
    if total1 == total2:
        return True
    else:
        return False



#Increasing sequnce?
def is_increasing(n):
    lenght = len(n) - 1
    total = 0
    for i in range(0, lenght):
        if n[i] < n[i+1]:
            total += 1
    if total == lenght:
        return True
    else:
        return False



#Descreasing sequence?
def is_decreasing(n):
    lenght = len(n) - 1
    total = 0
    for i in range(0, lenght):
        if n[i] > n[i+1]:
            total += 1
    return total == lenght



#Largest Palindrome
def palindrome(n):
    return n == int(str(n)[::-1])
def get_largest_palindrome(n):
    new = n - 1
    while palindrome(new) is False:
        new -= 1
    return new



#Prime Numbers / Sieve of Eratosthenes
def prime_numbers(n):
    primes = []
    for k in range(2, n+1):
        primes.append(k)
    p = 2
    while p < n:
        for i in range(p, n+1):
            if p*i in primes:
                primes.remove(p*i)
        p += 1
    return primes



#Anagrams
def is_anagram(a, b):
    a, b = a.lower(), b.lower()
    a, b = list(a), list(b)
    total = len(a)
    total2 = len(b)
    score = 0
    if total == total2:
        for char in a:
            for char2 in b:
                if char == char2:
                    score += 1
    return total == score



#Birthday Ranges
def birthday_ranges(birthdays, ranges):
    result = []
    for rang in ranges:
        counter = 0

        for day in birthdays:
            if day in range(rang[0], rang[1] + 1):
                counter += 1
        result.append(counter)
    return result



#Sum Numbers in Matrix
def sum_matrix(m):
    total = 0
    for i in m:
        for num in i:
            total += int(num)
    return total



#Matrix Bombing
m = {(0, 0): 42,
 (0, 1): 36,
 (0, 2): 37,
 (1, 0): 30,
 (1, 1): 15,
 (1, 2): 23,
 (2, 0): 29,
 (2, 1): 15,
 (2, 2): 26}

def printing(m):
    print(m[0, 0], m[0, 1], m[0, 2])
    print(m[1, 0], m[1, 1], m[1, 2])
    print(m[2, 0], m[2, 1], m[2, 2])

def set_zero(m):
    for i in m:
        if m[i] < 0:
            m[i] = 0

def matrix_bombing_plan(m):
    new = m
    x = int(input("enter number of row: "))
    y = int(input("enter number of column: "))
    #Corners
    if x == 0 and y == 0:
        new[0, 1] = new[0, 1] - new[0, 0]
        new[1, 1] = new[1, 1] - new[0, 0]
        new[1, 0] = new[1, 0] - new[0, 0]
        set_zero(new)
        return printing(new)
    if x == 0 and y == 2:
        new[0, 1] = new[0, 1] - new[0, 2]
        new[1, 1] = new[1, 1] - new[0, 2]
        new[1, 2] = new[1, 2] - new[0, 2]
        set_zero(new)
        return printing(new)
    if x == 2 and y == 0:
        new[2, 1] = new[2, 1] - new[2, 0]
        new[1, 1] = new[1, 1] - new[2, 0]
        new[1, 0] = new[1, 0] - new[2, 0]
        set_zero(new)
        return printing(new)
    if x == 2 and y == 2:
        new[2, 1] = new[2, 1] - new[2, 2]
        new[1, 1] = new[1, 1] - new[2, 2]
        new[1, 2] = new[1, 2] - new[2, 2]
        set_zero(new)
        return printing(new)

    #middles
    if x == 0 and y == 1:
        new[0, 0] = new[0, 0] - new[0, 1]
        new[1, 0] = new[1, 0] - new[0, 1]
        new[0, 2] = new[0, 2] - new[0, 1]
        new[1, 1] = new[1, 1] - new[0, 1]
        new[1, 2] = new[1, 2] - new[0, 1]
        set_zero(new)
        return printing(new)
    if x == 2 and y == 1:
        new[2, 0] = new[2, 0] - new[2, 1]
        new[2, 2] = new[2, 2] - new[2, 1]
        new[1, 0] = new[1, 0] - new[2, 1]
        new[1, 1] = new[1, 1] - new[2, 1]
        new[1, 2] = new[1, 2] - new[2, 1]
        set_zero(new)
        return printing(new)
    if x == 1 and y == 0:
        new[0, 0] = new[0, 0] - new[1, 0]
        new[2, 0] = new[2, 0] - new[1, 0]
        new[0, 1] = new[0, 1] - new[1, 0]
        new[1, 1] = new[1, 1] - new[1, 0]
        new[2, 1] = new[2, 1] - new[1, 0]
        set_zero(new)
        return printing(new)
    if x == 1 and y == 2:
        new[0, 1] = new[0, 1] - new[1, 2]
        new[2, 1] = new[2, 1] - new[1, 2]
        new[0, 2] = new[0, 2] - new[1, 2]
        new[1, 1] = new[1, 1] - new[1, 2]
        new[2, 2] = new[2, 2] - new[1, 2]
        set_zero(new)
        return printing(new)

    #THE Middle one
    if x == 1 and y == 1:
        new[0, 0] = new[0, 0] - new[1, 1]
        new[0, 1] = new[0, 1] - new[1, 1]
        new[0, 2] = new[0, 2] - new[1, 1]
        new[1, 0] = new[1, 0] - new[1, 1]
        new[1, 2] = new[1, 2] - new[1, 1]
        new[2, 0] = new[2, 0] - new[1, 1]
        new[2, 1] = new[2, 1] - new[1, 1]
        new[2, 2] = new[2, 2] - new[1, 1]
        set_zero(new)
        return printing(new)
    else:
        print("Error. Wrong numbers.")


# Is Transversal
def is_transversal(transversal, family):

    if len(transversal) != len(family):
        return False

    for sett in family:

        for t in transversal:
            for s in sett:
                if t == s:
                    return True

        temp = ["chek"]
        for t in transversal:
            temp.append(t)
            for i in range(0, len(family)):
                for s in sett:
                    for l in temp:
                        if l == s:
                            temp.remove(l)
        if not temp:
            return True
        else:
            return False
