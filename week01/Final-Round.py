#Count words
def count_words(arr):
    count = 0
    dict = {}
    for i in arr:
        for k in arr:
            if i == k:
                count += 1
        dict[i] = count
        count = 0
    return dict



#NaN Expand
def nan_expands(n):
    printed = ""
    if n == 0:
        return "''"
    i = 0
    while i < n:
        printed += "Not a "
        i += 1
    printed = printed + "NaN"
    return printed



# Iterations of NaN Expand
def iterations_of_nan_expand(m):
    
    if m == "":
        return 0
    m = m.split()
    
    total = 0
    
    for char in m:
        if char == "Not":
            total += 1
    
    if total != 0:
        return total
    else:
        return False


#The group function
def group(m):
    new =[]
    small_list = []
    small_list.append(m[0])
    for i in range(1, len(m)):
        if m[i] == m[i-1]:
            small_list.append(m[i])
            if i == len(m)-1:
                new.append(small_list)
        else:
            new.append(small_list)
            small_list = []
            small_list.append(m[i])
    return new



# Longest subsequence of equal consecutive elements
def max_consecutive(m):
    new =[]
    total = []
    small_list = []
    small_list.append(m[0])
    for i in range(1, len(m)):
        if m[i] == m[i-1]:
            small_list.append(m[i])
            if i == len(m)-1:
                new.append(small_list)
        else:
            new.append(small_list)
            small_list = []
            small_list.append(m[i])
    for n in new:
        total.append(len(n))
    return max(total)


#Gas Stations
def gas_stations(distance, tank_size, stations):
    stations.append(distance)
    list_stations = [0]
    for i in range(1, len(stations)):
        first = tank_size - stations[i-1] + list_stations[-1]
        second = stations[i] - stations[i-1]
        if second > first:
            list_stations.append(stations[i-1])
    list_stations.remove(0)
    return list_stations



#Sum all numbers in a given string
def sum_of_numbers(m):
    new_list = []
    middle = []
    m = list(m)
    total = 0
    for i in range(0, len(m)):
        if m[i].isdigit():
            middle.append(m[i])
            if i == len(m) -1:
                if middle != []:
                    new_list.append(middle)
        else:
            if middle != []:
                new_list.append(middle)
                middle = []
    for k in new_list:
        new = map(str, k)
        new="".join(new)
        total += int(new)
    return total



#100 SMS
#numbersToMessage(pressedSequence)
def group(m):
    new =[]
    small_list = []
    small_list.append(m[0])
    for i in range(1, len(m)):
        if m[i] == m[i-1]:
            small_list.append(m[i])
            if i == len(m)-1:
                new.append(small_list)
        else:
            new.append(small_list)
            small_list = []
            small_list.append(m[i])
            if i == len(m)-1:
                new.append(small_list)
    return new


def cap(m):
    new =[]
    small_list = []
    small_list.append(m[0])
    for i in range(1, len(m)):
        if m[i] != "cap":
            small_list.append(m[i])
            if i == len(m)-1:
                if "cap" in small_list:
                    small_list.remove("cap")
                new.append(small_list)
        else:
            if "cap" in small_list:
                small_list.remove("cap")
            new.append(small_list)
            small_list = []
    return new


def numbersToMessage(pressedSequence):
    dict={(-1, 1): "",
          (0, 1): " ",
          (0, 2): "  ",
          (1, 1): "cap",
          (2, 1): "a",
          (2, 2): "b",
          (2, 3): "c",
          (3, 1): "d",
          (3, 2): "e",
          (3, 3): "f",
          (4, 1): "g",
          (4, 2): "h",
          (4, 3): "i",
          (5, 1): "j",
          (5, 2): "k",
          (5, 3): "l",
          (6, 1): "m",
          (6, 2): "n",
          (6, 3): "o",
          (7, 1): "p",
          (7, 2): "q",
          (7, 3): "r",
          (7, 4): "s",
          (8, 1): "t",
          (8, 2): "u",
          (8, 3): "v",
          (9, 1): "w",
          (9, 2): "x",
          (9, 3): "y",
          (9, 4): "z"}

    message = []
    pressedSequence = group(pressedSequence)

    for i in pressedSequence:
        index = pressedSequence.index(i)
        lenght = len(i)
        if pressedSequence[index][0] == 7:
            while lenght > 4:
                lenght -= 4
        else:
            while lenght > 3:
                lenght -= 3
        index = pressedSequence.index(i)
        key = [pressedSequence[index][0], lenght]
        key = tuple(key)
        for keys in dict:
            if keys == key:
                message.append(dict[key])
    
    if "cap" in message:
        temp = cap(message)
        message = []
        for i in temp:
            i = "".join(i)
            i = i.capitalize()
            message.append(i)
    
    message = "".join(message)
    return message



#messageToNumbers(messsage)
def one_button(m):
    new = 0
    for i in range(1, len(m)):
        if m[i] == m[i-1]:
            new += 1
            if i == len(m)-1:
                new += 1
    if len(m) == new:
        return True

def messageToNumbers(pressedSequence):
    dict={" ":(0, 1),
          "a":(2, 1),
          "b":(2, 2),
           "c":(2, 3),
          "d":(3, 1),
          "e":(3, 2),
          "f":(3, 3),
          "g":(4, 1),
          "h":(4, 2),
          "i":(4, 3),
          "j":(5, 1),
          "k":(5, 2),
          "l":(5, 3),
          "m":(6, 1),
          "n":(6, 2),
          "o":(6, 3),
          "p":(7, 1),
          "q":(7, 2),
          "r":(7, 3),
          "s":(7, 4),
          "t":(8, 1),
          "u":(8, 2),
          "v":(8, 3),
          "w":(9, 1),
          "x":(9, 2),
          "y":(9, 3),
          "z":(9, 4)}
          
    pressedSequence = list(pressedSequence)
    message = []
    new_message = []

    for char in pressedSequence:
        if char.islower() or char == " ":
            button = dict[char][0]
            times = dict[char][1]
            while times != 0:
                message.append(button)
                times -= 1
        else:
            message.append(1)
            char = char.lower()
            button = dict[char][0]
            times = dict[char][1]
            while times != 0:
                message.append(button)
                times -= 1

    if one_button(message):
        for char in pressedSequence:
            button = dict[char][0]
            times = dict[char][1]
            while times != 0:
                new_message.append(button)
                times -= 1
            new_message.append(-1)
        if new_message[len(new_message)-1] == -1:
            del new_message[len(new_message)-1]
        return new_message
    else:
        return message
