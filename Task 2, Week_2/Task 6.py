# Yêu cầu người dùng nhập mã màu HEX
#hex_color = input("Insert a hex color: ")

# Kiểm tra xem mã màu có bắt đầu bằng # và có đủ 7 ký tự không
#if len(hex_color) == 7 and hex_color[0] == '#':
    # Trích xuất các thành phần màu
    #red = hex_color[1:3]
    #green = hex_color[3:5]
    #blue = hex_color[5:7]
    
    # Hiển thị kết quả
    #print("Colors")
    #print(f"- Red {red.upper()}")
    #print(f"- Green {green.upper()}")
    #print(f"- Blue {blue.upper()}")
#else:
    #print("Invalid hex color format! Please use the format #RRGGBB.")

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