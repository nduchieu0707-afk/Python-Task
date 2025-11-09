Insert = int(input("Insert starting point: "))
Insert2 = int(input("Insert stopping point: "))
Insert3 = int(input("Insert inspection point: "))

if Insert > Insert3:
    print("Inspection value must be within the range of start and stop.")
elif Insert == Insert2:
    print("Starting point value must be less than the stopping point value.")
    print("Inspection value must be within the range of start and stop.")
elif Insert == Insert3:
    print("First loop - inspection with break:")

    print("Second loop - inspection with continue:")
    for i in range(Insert, Insert2):
        if i == Insert3:
            continue
        print(i, end=" ")
else:
    print("First loop - inspection with break:")
    for i in range(Insert, Insert3):
        print(i, end=" ")
    print()

    print("Second loop - inspection with continue:")
    for i in range(Insert, Insert2):
        if i == Insert3:
            continue
        print(i, end=" ")
