print("Program starting.")
print("Options:")
print("1 - Show count")
print("2 - Increase count")
print("3 - Reset count")
print("0 - Exit")
count = 0

running = True
while running: 
    def choice():
        global count, running
        Yourchoice = input("Your choice: ")
        if Yourchoice == "1":
            print(f"Current count - {count}")
        elif Yourchoice == "2":
            count += 1
            print("Count increased!")
        elif Yourchoice == "3":
            count = 0
            print("Cleared count!")
        elif Yourchoice == "0":
            running = False
            print("Exiting program.")
        else:
            print("Unknown option!")
        return None

    choice()

# or
# def main():
#     numbers = 0
#     while True:
#         choices = int(input("your choices: "))
#         if choices == 1:
#             print(f"{numbers}")
#         elif choices == 2:
#             numbers += 1
#             print("Increase")
#         elif choices == 3:
#             numbers = 0
#             print("Clear")
#         elif choices == 0:
#             break
# main()
