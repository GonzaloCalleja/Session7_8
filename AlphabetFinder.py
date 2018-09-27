
# string = input("Introduce a string of characters: ")
string = 'azcwobobegghakl'  # example
# string = "abcbcd"

# ("z">"a") ->  True
# print(string.find("a")) -> 0

result = ''
temp = ''
iterator = 0

for c in string:

    prevPos = iterator - 1
    iterator += 1

    if temp is "":
        temp = c
        continue

    if c >= string[prevPos]:
        temp += c
    else:
        temp = c

    print(temp, iterator - 1, end=" - ")

    if len(temp) > len(result):
        result = temp

    print(result)


print("The longest alphabetically ordered string is: ", result)
