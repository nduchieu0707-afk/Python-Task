def main():
    print("Program starting.")
    print("This program can copy a file.")
    
    source = input("Insert source filename: ")
    destination = input("Insert destination filename: ")
    
    print(f"Reading file '{source}' content.")
    with open(source, 'r') as source_file:
        content = source_file.read()
    
    print("File content ready in memory.")
    print(f"Writing content into file '{destination}'.")
    
    with open(destination, 'w') as dest_file:
        dest_file.write(content)
    
    print("Copying operation complete.")
    print("Program ending.")

if __name__ == "__main__":
    main()