fp = open("open.txt", "a")
print(fp)
line = input("Give some text, don't be shy ")
fp.write(line)
fp.write("\n")
fp.close()
