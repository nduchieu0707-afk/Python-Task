import sys

def merge(Left: list[int], Right: list[int], Merge: list[int], Asc: bool = True) -> None:
    i = j = 0
    while i < len(Left) and j < len(Right):
        if (Asc and Left[i] <= Right[j]) or (not Asc and Left[i] >= Right[j]):
            Merge.append(Left[i])
            i += 1
        else:
            Merge.append(Right[j])
            j += 1
    Merge.extend(Left[i:])
    Merge.extend(Right[j:])

def mergeSort(Values: list[int], PAsc: bool = True) -> None:
    if len(Values) <= 1:
        return
    
    mid = len(Values) // 2
    left = Values[:mid]
    right = Values[mid:]
    
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    
    Values.clear()
    merge(left, right, Values, PAsc)

def main():
    print("Program starting.")
    filename = sys.argv[1] if len(sys.argv) == 2 else input("Insert filename: ")
    
    with open(filename) as f:
        numbers = [int(line.strip()) for line in f if line.strip()]
    
    original = numbers.copy()
    print(f"Raw '{filename}' -> {', '.join(map(str, original))}")
    
    asc_numbers = original.copy()
    mergeSort(asc_numbers, True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc_numbers))}")
    
    desc_numbers = original.copy()
    mergeSort(desc_numbers, False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc_numbers))}")
    
    print("Program ending.")

if __name__ == "__main__":
    main()