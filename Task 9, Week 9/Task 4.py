def main():
    Insert = input("Insert Celsius: ")
    try:
        value = float(Insert)
        print(f"You inserted {value}")
    except ValueError:
        print(f"could not convert string to float: {Insert}")
if __name__ == "__main__":
    main()