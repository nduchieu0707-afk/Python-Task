import sys
import os

def main():
    print("Program starting.")
    
    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        print("Usage: python A9_T7.py source_file destination_file")
        return
    
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    
    print(f'Source file "{src_file}"')
    print(f'Destination file "{dst_file}"')
    
    if os.path.exists(dst_file):
        overwrite = input("File exists. Overwrite (y/n)?: ")
        if overwrite.lower() != "y":
            print("Copy operation cancelled.")
            return
    
    try:
        with open(src_file, "r") as source:
            content = source.read()
        
        with open(dst_file, "w") as destination:
            destination.write(content)
        
        print(f'Copying file "{src_file}" to "{dst_file}".')
        
    except Exception as e:
        print(f"Error: {e}")
        print("Program ending with exit code -1.")
        sys.exit(-1)
    
    print("Program ending.")
if __name__ == "__main__":
    main()