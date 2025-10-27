WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')
    PRows.clear()
    with open(PFilename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            if line.strip():
                PRows.append(line.strip())
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    counts = [0] * 7
    for row in PRows:
        for i, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                counts[i] += 1
                break
    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {counts[i]} stamps")
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for result in PResults:
        print(result)
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    print("Program starting.")
    rows = []
    results = []
    filename = input("Insert filename: ")
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    rows.clear()
    results.clear()
    print("Program ending.")
    return None

main()