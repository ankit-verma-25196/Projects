import re

# input str - aahacktractorhacker

pat = r'hack'
st = input()

match = re.findall(pat,st)

print("No. of matches :", len(match))


