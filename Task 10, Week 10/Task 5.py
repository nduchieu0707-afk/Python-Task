def Factorial(Num: int) -> int:
    if Num == 0 or Num == 1:
        return 1
    return Num * Factorial(Num - 1)

def main():
    print("Program starting.")
    num = int(input("Insert factorial: "))
    result = Factorial(num)
    print(f"Factorial {num}!")
    print(f"{num} = {result}")
    print("Program ending.")

if __name__ == "__main__":
    main()