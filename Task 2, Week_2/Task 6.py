print("Program starting.")
print()

hex_color = input("Insert a hex color: ")

if len(hex_color) == 7 and hex_color[0] == '#':
    red = hex_color[1:3]
    green = hex_color[3:5]
    blue = hex_color[5:7]

    print()
    print("Colors")
    print(f"- Red {red.upper()}")
    print(f"- Green {green.upper()}")
    print(f"- Blue {blue.upper()}")
else:
    print("Please use the format #RRGGBB.")

print()
print("Program ending.")