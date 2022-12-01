import sys
import sysconfig

ab = sys.stdin.read().split(" ")
if (int(ab[0]) > int(ab[1])):
    print("1")
else:
    print("0")