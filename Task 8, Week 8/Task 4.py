from datetime import datetime

MONTHS = ("January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December")

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def read_timestamps(filename, timestamps):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    dt = datetime.strptime(line, "%Y-%m-%dT%H:%M")
                    timestamps.append(dt)
    except FileNotFoundError:
        print(f"Not found {filename}")

def count_years(year, timestamps):
    count = 0
    for ts in timestamps:
        if ts.year == year:
            count += 1
    return count

def count_months(month, timestamps):
    month_index = MONTHS.index(month) + 1
    count = 0
    for ts in timestamps:
        if ts.month == month_index:
            count += 1
    return count

def count_weekdays(weekday, timestamps):
    weekday_index = WEEKDAYS.index(weekday)
    count = 0
    for ts in timestamps:
        if ts.weekday() == weekday_index:
            count += 1
    return count

def main():
    print("Program starting.")
    
    filename = input("Insert filename: ")
    timestamps = []
    read_timestamps(filename, timestamps)
    
    if not timestamps:
        print("No data loaded!")
        return
    
    while True:
        print("\nOptions:")
        print("1 - Calculate amount of timestamps during year")
        print("2 - Calculate amount of timestamps during month") 
        print("3 - Calculate amount of timestamps during weekday")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            year = int(input("Insert year: "))
            count = count_years(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {count}")
            
        elif choice == "2":
            month = input("Insert month: ")
            if month in MONTHS:
                count = count_months(month, timestamps)
                print(f"Amount of timestamps during month '{month}' is {count}")
            else:
                print("Invalid month!")
                
        elif choice == "3":
            weekday = input("Insert weekday: ")
            if weekday in WEEKDAYS:
                count = count_weekdays(weekday, timestamps)
                print(f"Amount of timestamps during weekday '{weekday}' is {count}")
            else:
                print("Invalid weekday!")
                
        elif choice == "0":
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice!")
    
    print("Program ending.")

if __name__ == "__main__":
    main()