import time
import copy
from typing import Callable

def bubbleSort(Nums: list[int]) -> list[int]:
    n = len(Nums)
    for i in range(n):
        for j in range(n - i - 1):
            if Nums[j] > Nums[j + 1]:
                Nums[j], Nums[j + 1] = Nums[j + 1], Nums[j]
    return Nums

def quickSort(Nums: list[int]) -> list[int]:
    if len(Nums) <= 1:
        return Nums
    pivot = Nums[len(Nums) // 2]
    left = [x for x in Nums if x < pivot]
    middle = [x for x in Nums if x == pivot]
    right = [x for x in Nums if x > pivot]
    return quickSort(left) + middle + quickSort(right)

def readValues(Values: list[int]) -> None:
    Values.clear()
    filename = input("Insert dataset filename: ")
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                Values.append(int(line))
    print()

def measureSortingTime(SortingAlgorithm: Callable, Arr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    SortingAlgorithm(copy.deepcopy(Arr))
    EndTime = time.perf_counter_ns()
    return EndTime - StartTime

def main() -> None:
    Values: list[int] = []
    current_dataset = ""
    
    print("Program starting.")
    
    while True:
        print("Options:")
        print("1 - Read dataset values")
        print("2 - Measure speeds") 
        print("3 - Save results")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            readValues(Values)
            current_dataset = "dataset"
            
        elif choice == "2":
            if not Values:
                print("No dataset loaded. Please read dataset first.\n")
                continue
                
            print(f"Measured speeds for dataset '{current_dataset}':")
            
            builtin_time = measureSortingTime(sorted, Values)
            bubble_time = measureSortingTime(bubbleSort, Values) 
            quick_time = measureSortingTime(quickSort, Values)
            
            print(f" - Built-in sorted {builtin_time} ns")
            print(f" - Bubble sort {bubble_time} ns")
            print(f" - Quick sort {quick_time} ns")
            print()
            
        elif choice == "3":
            if not Values:
                print("No results to save. Please measure speeds first.\n")
                continue
                
            filename = input("Insert results filename: ")
            with open(filename, 'w') as f:
                f.write(f"Measured speeds for dataset '{current_dataset}':\n")
                f.write(f" - Built-in sorted {measureSortingTime(sorted, Values)} ns\n")
                f.write(f" - Bubble sort {measureSortingTime(bubbleSort, Values)} ns\n")
                f.write(f" - Quick sort {measureSortingTime(quickSort, Values)} ns\n")
            print()
            
        elif choice == "0":
            print("Exiting program.\n")
            break
            
        else:
            print("Invalid choice. Please try again.\n")
    
    print("Program ending.")

if __name__ == "__main__":
    main()