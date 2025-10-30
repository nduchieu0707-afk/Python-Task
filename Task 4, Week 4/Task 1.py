value1 = int(input("Insert starting value: "))
value2 = int(input("Insert stopping value: "))

if value1 > value2:
    print("Error")
else:
    for i in range(value1, value2+1):

        print(i)

# or:
# Insert1 = int(input("Insert: "))
# Insert2 = int(input("Insert: "))
# sequences = int(Insert2)

# while Insert1 <= Insert2:
#     print(Insert1, end=" ")
#     Insert1 += 1
