import sys

def bubbleSort(Values: list[int], Asc: bool = True) -> None:
    num = len(Values)
    for i in range(num):
        for j in range(num - i - 1):
            if (Asc and Values[j] > Values[j + 1]) or (not Asc and Values[j] < Values[j + 1]):
                Values[j], Values[j + 1] = Values[j + 1], Values[j]

def main():
    print("Program starting.")
    filename = sys.argv[1] if len(sys.argv) == 2 else input("Insert filename: ")
    
    with open(filename) as f:
        numbers = [int(line.strip()) for line in f if line.strip()]
    
    original = numbers.copy()
    print(f"Raw '{filename}' -> {', '.join(map(str, original))}")
    
    bubbleSort(numbers, True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, numbers))}")
    
    bubbleSort(numbers, False)
    print(f"Descending '{filename}' -> {', '.join(map(str, numbers))}")
    
    print("Program ending.")

if __name__ == "__main__":
    main()