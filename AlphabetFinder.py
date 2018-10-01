
# string = 'azcwobobegghakl'  # example
# string = "abcbcd"

# ("z">"a") ->  True
# print(string.find("a")) -> 0

string = input("Introduce a string of characters: ")

result = ''
temp = ''

for pos in range(len(string)):

    prevPos = pos - 1

    if temp is "":
        temp = string[pos]
        continue

    if string[pos] >= string[prevPos]:
        temp += string[pos]
    else:
        temp = string[pos]

    # print(temp, iterator - 1, end=" - ")

    if len(temp) > len(result):
        result = temp

    # print(result)

print("The longest alphabetically ordered string is: ", result)
