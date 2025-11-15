def add(cal1, cal2):
    plus = cal1 + cal2
    print(f"{cal1} + {cal2} = {plus}")

def add2(cal1, cal2):
    minus = cal1 - cal2
    print(f"{cal1} - {cal2} = {minus}")

def add3(cal1, cal2):
    area = cal1 * cal2
    print(f"{cal1} * {cal2} = {area}")

def add4(cal1, cal2):
    area = cal1 / cal2
    print(f"{cal1} / {cal2} = {area}")

def main():
    while True:
        Choice = int(input("Your choice: "))
        if Choice == 1:
            cal1 = float(input("num1: "))
            cal2 = float(input("num2: "))
            add(cal1, cal2)
        elif Choice == 2:
            cal1 = float(input("num1: "))
            cal2 = float(input("num2: "))
            add2(cal1, cal2)
        elif Choice == 3:
            cal1 = float(input("num1: "))
            cal2 = float(input("num2: "))
            add3(cal1, cal2)
        elif Choice == 4:
            cal1 = float(input("num1: "))
            cal2 = float(input("num2: "))
            add4(cal1, cal2)
        elif Choice == 0:
            break
if __name__ == "__main__":
    main()