from dataclasses import dataclass

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

@dataclass
class define():
    days: str
    price: str
    consumption: float
    total: float

@dataclass
class calculator():
    days: str
    daily_sum: float = 0.0
    daily_cost: float = 0.0

def readTimestamps(readfile: str, adds: list[define]):
    print(f'Reading file "{readfile}".')
    adds.clear()
    with open(readfile, 'r') as file:
        next(file)
        for line in file:
            if line.strip():
                columnes = line.strip().split(';')
                add = define(
                    days=columnes[0],
                    price=columnes[1],
                    consumption=float(columnes[2]),
                    total=float(columnes[3])
                )
                adds.append(add)

def analysis(adds: list[define], results: list[str]):
    print("Analysing timestamps.")
    daily_cost_week = [calculator(dayweek) for dayweek in WEEKDAYS]

    for ad in adds:
        for dai in daily_cost_week:
            if ad.days == dai.days:
                dai.daily_sum += ad.consumption
                dai.daily_cost += ad.consumption * ad.total
                break
            
    for dai in daily_cost_week:
        results.append(f" - {dai.days} usage {dai.daily_sum:.2f} kWh, cost {dai.daily_cost:.2f} €")

def displayTimestamps(results: list[str]):
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for result in results:
        print(result)
    print("### Electricity consumption summary ###")

def main():
    print("Program starting.")
    adds = []
    results = []
    readfile = input("Insert filename: ")
    readTimestamps(readfile, adds)
    analysis(adds, results)
    displayTimestamps(results)
    print("Program ending.")

if __name__ == "__main__":
    main()