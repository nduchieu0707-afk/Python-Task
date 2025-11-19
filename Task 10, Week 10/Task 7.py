import random

def layMines(Field: list[list[int]], PMines: int):
    rows = len(Field)
    cols = len(Field[0])
    
    mines_placed = 0
    while mines_placed < PMines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        
        if Field[row][col] != 9:
            Field[row][col] = 9
            mines_placed += 1

def calculateNearbys(Field: list[list[int]]) -> None:
    rows = len(Field)
    cols = len(Field[0])
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    for row in range(rows):
        for col in range(cols):
            if Field[row][col] == 9:
                continue
                
            mine_count = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols:
                    if Field[r][c] == 9:
                        mine_count += 1
            
            Field[row][col] = mine_count

def generateMinefield(MineField: list[list[int]], Rows: int, Cols: int, Mines: int) -> None:
    MineField.clear()
    
    for _ in range(Rows):
        MineField.append([0] * Cols)
    
    layMines(MineField, Mines)
    calculateNearbys(MineField)

def main() -> None:
    minefield = []
    
    print("Program starting.")
    
    while True:
        print("Options:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board") 
        print("3 - Save generated board")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            
            generateMinefield(minefield, rows, cols, mines)
            print()
            
        elif choice == "2":
            if not minefield:
                print("No board generated. Please generate board first.\n")
                continue
                
            for row in minefield:
                print(row)
            print()
            
        elif choice == "3":
            if not minefield:
                print("No board generated. Please generate board first.\n")
                continue
                
            filename = input("Insert filename: ")
            with open(filename, 'w') as f:
                for row in minefield:
                    f.write(','.join(map(str, row)) + '\n')
            print(f"Board saved to {filename}\n")
            
        elif choice == "0":
            print("Exiting program.\n")
            break
            
        else:
            print("Invalid choice. Please try again.\n")
    
    print("Program ending.")

if __name__ == "__main__":
    main()