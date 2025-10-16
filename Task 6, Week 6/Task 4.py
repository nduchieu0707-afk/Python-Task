def readfile(filename):
    numbers_print = []
    with open(filename, 'r') as file:
        for line in file:
            numbers_print.append(int(line.strip()))
    return numbers_print

def analysis(numbers_print):
    count = len(numbers_print)
    total = sum(numbers_print)
    shortest = min(numbers_print)
    greatest = max(numbers_print)
    average = total / count 
    return count, shortest, greatest, average

def main():
    filename = input("Insert filename: ")
    numbers_print = readfile(filename)
    count, shortest, greatest, average = analysis(numbers_print)
    print(f"Count: {count}")
    print(f"Shortest: {shortest}")
    print(f"Greatest: {greatest}")
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()