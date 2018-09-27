
url = "https://raw.githubusercontent.com/itb-ie/contest/master/text.txt"
name = "newcompetition.txt"
from urllib.request import urlretrieve
urlretrieve(url, name)

# count vowels in a line
#

result = " abcdefghijklmnopqrstuvwxyz"
fp = open(name, "r")

for line in fp:
    num = 0
    for char in line:
       #if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
       if char in "aeiou":
           num += 1

    print(result[num], end="")

fp.close()
