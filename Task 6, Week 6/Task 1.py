file = open("text1.txt", "r")
while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line, end="")
file.close()
