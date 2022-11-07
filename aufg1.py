import sys

print("Input args: ")
print(sys.argv)

allArgs = len(sys.argv)
startindex = allArgs - 2

while startindex < allArgs:
    print(sys.argv[startindex]) 
    startindex = startindex + 1