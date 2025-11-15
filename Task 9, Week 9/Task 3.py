def main():
    filename = input("file: ")
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"Couldn't read file {filename}")
if __name__ == "__main__":
    main()