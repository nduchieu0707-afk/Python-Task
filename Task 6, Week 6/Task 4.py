def readfile(filename):
    numbers_print = []
    with open(filename, 'r') as file:
        for line in file:
            numbers_print.append(str(line.strip()))
    return numbers_print

def analysis(numbers_print):
    total = len(numbers_print)
    length = [len(name) for name in numbers_print]
    shortest = min(length) if length else 0
    greatest = max(length) if length else 0
    summum = sum(length)
    average = summum / total if length else 0
    return total, length, shortest, greatest, summum, average

def main():
    filename = input("Insert filename: ")
    numbers_print = readfile(filename)
    total, length, shortest, greatest, summum, average = analysis(numbers_print)
    print(f"Count: {total}")
    print(f"Shortest: {shortest}")
    print(f"Greatest: {greatest}")
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()
