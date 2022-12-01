import sys

string = input()
TARGET = 'PER'
counter = 0

for i, char in enumerate(string):
    if char != TARGET[i % 3]:
        counter += 1

print(counter)