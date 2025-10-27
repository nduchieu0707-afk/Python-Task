from dataclasses import dataclass

@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

def readTimestamps(filename: str, timestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{filename}".')
    timestamps.clear()
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            if line.strip():
                columns = line.strip().split(';')
                timestamp = TIMESTAMP(
                    weekday=columns[0],
                    hour=columns[1],
                    consumption=float(columns[2]),
                    price=float(columns[3])
                )
                timestamps.append(timestamp)

def displayTimestamps(timestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for ts in timestamps:
        total = ts.consumption * ts.price
        print(f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, consumption {ts.consumption:.2f} kWh, total {total:.2f} €")

def main() -> None:
    print("Program starting.")
    timestamps = []
    filename = input("Insert filename: ")
    readTimestamps(filename, timestamps)
    displayTimestamps(timestamps)
    print("Program ending.")

if __name__ == "__main__":
    main()