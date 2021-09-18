import os

file = open("C:/Users/faiqa/OneDrive/Desktop/Python/readline.txt", 'r')
# print(file.readlines())
# looping
for line in file:
    print(file.readline())
file.close()
