import sys

# reading the command line arguments
argumentList = sys.argv

f = open(argumentList[1],"r")

print(f.readlines())
print(type(f.readlines()))


