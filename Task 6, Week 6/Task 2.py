line1 = str(input("Insert first name: "))
line2 = str(input("Insert last name: "))
filename = input("Insert filename: ")
open(filename, 'a').write(f"{line1}\n{line2}")