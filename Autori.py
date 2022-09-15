from pickle import TRUE
import sys

str = ""
a = sys.stdin.read()
test = True
for i in a:
    if test == True:
        str += i
        test = False
    if i == '-':
        test = True
    
        
print (str)