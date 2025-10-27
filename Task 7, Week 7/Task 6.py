import random
random.seed(1234)

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = {1: ("Rock", ROCK), 2: ("Paper", PAPER), 3: ("Scissors", SCISSORS)}

def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    name = input("Insert player name: ")
    print(f"Welcome {name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")
    
    wins = losses = draws = 0
    
    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper") 
        print("3 - Scissors")
        print("0 - Quit game")
        
        try:
            choice = int(input("Your choice: "))
        except:
            continue
            
        if choice == 0:
            break
        elif choice not in [1, 2, 3]:
            continue
            
        print("Rock! Paper! Scissors! Shoot!\n")
        
        player_choice, player_art = choices[choice]
        bot_choice_num = random.randint(1, 3)
        bot_choice, bot_art = choices[bot_choice_num]
        
        print("#" * 25)
        print(f"{name} chose {player_choice}.\n{player_art}")
        print("#" * 25)
        print(f"RPS-3PO chose {bot_choice}.\n{bot_art}")
        print("#" * 25)
        
        if player_choice == bot_choice:
            print(f"Draw! Both players chose {player_choice}.")
            draws += 1
        elif (player_choice == "Rock" and bot_choice == "Scissors") or \
             (player_choice == "Paper" and bot_choice == "Rock") or \
             (player_choice == "Scissors" and bot_choice == "Paper"):
            print(f"{name} {player_choice} beats RPS-3PO {bot_choice}.")
            wins += 1
        else:
            print(f"RPS-3PO {bot_choice} beats {name} {player_choice}.")
            losses += 1
            
        print()
    
    print("\nResults:")
    print(f"{name} - wins ({wins}), losses ({losses}), draws ({draws})")
    print(f"RPS-3PO - wins ({losses}), losses ({wins}), draws ({draws})")
    print("Program ending.")

if __name__ == "__main__":
    main()