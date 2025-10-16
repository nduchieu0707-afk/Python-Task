def readValues(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

def analyseValues(numbers):
    total = sum(numbers)
    count = len(numbers)
    greatest = max(numbers)
    average = total / count if count > 0 else 0
    
    result = f"Count;Sum;Greatest;Average\n{count};{total};{greatest};{average:.2f}\n"
    return result

def main():
    filename = input("Enter filename: ")
    numbers = readValues(filename)
    result = analyseValues(numbers)
    print(result)

if __name__ == "__main__":
    main()