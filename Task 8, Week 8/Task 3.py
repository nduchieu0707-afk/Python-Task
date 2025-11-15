def read(readfile):
    numbers = []
    with open(readfile, 'r') as file:
        for line in file:
            content = line.strip()
            if content:
                numbers.append(float(content))
    return numbers

def calculator(numbers):
    length = len(numbers)
    sum_num = sum(numbers)
    average = sum_num / length
    return length, sum_num, average

def main():
    while True:
        print("1 - Read values")
        print("2 - Amount of values")
        print("3 - Calculate sum of values")
        print("4 - Calculate average of values")
        print("0 - Exit")

        choices = int(input("Your choice: "))
        if choices == 1:
            readfile = input("file: ")
            numbers = read(readfile)
            length, sum_num, average = calculator(numbers)
            print(f"{length}, {sum_num}, {average}")
        elif choices == 2:
            print(f"length {length}")
        elif choices == 3:
            print(f"sum {sum_num}")
        elif choices == 4:
            print(f"average {average}")
        elif choices == 0:
            break
if __name__ == "__main__":
    main()