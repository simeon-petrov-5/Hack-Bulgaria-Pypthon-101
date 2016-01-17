# cat
import sys
def main():
    filename = sys.argv[1]
    data = open(filename, 'r')
    print(data.read())
    data.close()

if __name__ == '__main__':
    main()



# #cat2
# import sys
# def main():
#     for filename in sys.argv[1:]:
#         data = open(filename, 'r')
#         print('{} \n'.format(data.read()))
#         data.close()

# if __name__ == '__main__':
#     main()



# #Generate numbers
# import sys
# from random import randint

# def main():
#     filename = sys.argv[1]
#     n = sys.argv[2]
#     n = int(n)
#     data = open(filename, 'w')
#     while n != 0:
#         data.write(str(randint(1, 1000)) + " ")
#         n -= 1
#     data.close()

# if __name__ == '__main__':
#     main()



# #Sum numbers
# import sys

# def main():
#     filename = sys.argv[1]
#     sum_ = 0
#     data = open(filename, 'r')
#     numbers = data.read()
#     numbers = numbers.split(' ')
#     for digit in numbers:
#         if digit.isdigit():
#             sum_ += int(digit)
#     data.close()

#     return sum_

# if __name__ == '__main__':
#     print(main())



# #to du -h command
# import sys
# import os

# def main():
#     path = sys.argv[1]
#     if os.path.exists(path):
#         print(os.path.getsize(path) / 512)

# if __name__ == '__main__':
#     main()