value1 = int(input("Insert starting value: "))
value2 = int(input("Insert stopping value: "))

if value1 > value2:
    print("Error")
else:
    for i in range(value1, value2+1):
        print(i)