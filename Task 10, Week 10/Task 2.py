from math import prod

def read(filename):
    numbers = []
    with open(filename, "r") as file:
        for lines in file:
            if lines.strip():
                numbers.append(int(lines.strip()))
    return numbers

def calculate(numbers):
    sum_num = sum(numbers)
    product = prod(numbers)
    return sum_num, product

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    numbers = read(filename)
    sum_num, product = calculate(numbers)
    
    print("# --- Sum of numbers --- #")
    print(sum_num)
    print("# --- Sum of numbers --- #")
    
    print("# --- Product of numbers --- #")
    print(product)
    print("# --- Product of numbers --- #")
    
    print("Program ending.")

if __name__ == "__main__":
    main()