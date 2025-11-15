import sys

print("Program starting.")
code = int(input("Insert exit code(0-255): "))

if code == 0:
    print("Clean exit")
else:
    print("Error code")

sys.exit(code)