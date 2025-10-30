value1 = int(input("Insert starting point: ")) 
value2 = int(input("Insert stopping point: ")) 
value3 = int(input("Insert inspection point: "))

running = True
while running:
    if value1 > value3:
        print("Inspection value must be within the range of start and stop.")
    elif value1 == value3:
        print("First loop - inspection with break: ")

        Secound_loop = [str(i) for i in range(value1, value2)]
        print(" ".join(Secound_loop))
    elif value1 == value2:
        print("Starting point value must be less than the stopping point value.")
        print("Inspection value must be within the range of start and stop.")
    else:
        First_loop = [str(i) for i in range(value1, value3)]
        print(" ".join(First_loop))

        Secound_loop = [str(i) for i in range(value1, value2)]
        print(" ".join(Secound_loop))

    break

# or:
# Insert1 = int(input("Insert starting point: "))
# Insert2 = int(input("Insert starting point: "))
# Insert3 = int(input("Insert starting point: "))

# if Insert1 > Insert3:
#     print("Inspection value must be within the range of start and stop. ")
# elif Insert1 == Insert2:
#     print("Starting point value must be less than the stopping point value.")
#     print("Inspection value must be within the range of start and stop.")
# elif Insert1 == Insert3:
#     print("First loop - inspection with break:\n")
#     print("Second loop - inspection with continue: ")
#     for i in range(Insert1, Insert2):
#         if i == Insert3:
#             continue
#         print(i, end=" ")
#     print()
# else:
#     for i in range (Insert1, Insert3):
#         print(i, end=" ")
#     print()
    
#     for i in range(Insert1, Insert2):
#         if i == Insert3:
#             continue
#         print(i, end=" ")
#     print()
