import random
import time
import os
import sys

def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def get_player_choice():
    choices = ['rock', 'paper', 'scissors']
    short_choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    numbered_choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    print("Choose one:")
    print("  1) Rock (r)")
    print("  2) Paper (p)")
    print("  3) Scissors (s)")
    print("  4) Exit (e, q, x, 0)")
    while True:
        player = input("Your choice: ").strip().lower()
        if player in ['4', 'e', 'q', 'x', 'exit', 'quit']:
            print("Thanks for playing!")
            return player
        if player in choices:
            return player
        if player in short_choices:
            return short_choices[player]
        if player in numbered_choices:
            return numbered_choices[player]
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    wins = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    if wins[player] == computer:
        return "\033[92m*** YOU WIN! ***\033[0m"
    else:
        return "\033[91m*** COMPUTER WINS! ***\033[0m"

def get_ascii_art(choice):
    art = {
        'rock': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
        'paper': '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
        'scissors': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    }
    return art.get(choice, '')

def print_side_by_side(player, computer, player_choice, computer_choice):
    player_art = get_ascii_art(player_choice).splitlines()
    computer_art = get_ascii_art(computer_choice).splitlines()
    max_lines = max(len(player_art), len(computer_art))
    player_art += [''] * (max_lines - len(player_art))
    computer_art += [''] * (max_lines - len(computer_art))
    print(f"You chose: {player_choice:<10}    VS    Computer chose: {computer_choice:<10}")
    print()
    for l, r in zip(player_art, computer_art):
        print(f"{l:<20}    {r}")

def animate_ascii(player_choice, computer_choice):
    # Animation frames for rock, paper, scissors
    frames = [
        ("    _______        _______\n---'   ____)      ---'   ____)",

         "      (_____)          (_____)",

         "      (_____)          (_____)",

         "      (____)           (____)",

         "---.__(___)      ---.__(___)"),
        ("    _______        _______\n---'   ____)      ---'    ____)____",

         "      (_____)           ______)",

         "      (_____)          _______)",

         "      (____)          _______)",

         "---.__(___)      ---.__________)"),
        ("    _______        _______\n---'   ____)____  ---'   ____)____",

         "          ______)         ______)",

         "       __________)    __________)",

         "      (____)           (____)",

         "---.__(___)      ---.__(___)")
    ]
    # Show 3 quick "1, 2, 3, SHOOT!" frames
    for count in ["Rock...", "Paper...", "Scissors...", "Shoot!"]:
        clear_screen()
        print(f"{count}\n")
        time.sleep(0.4)
    # Show the hands coming together
    for i in range(len(frames)):
        clear_screen()
        for line in frames[i]:
            print(line)
        time.sleep(0.15)
    # Show the final choices side by side
    clear_screen()
    print_side_by_side('player', 'computer', player_choice, computer_choice)

def main():
    print("Welcome to Rock-Paper-Scissors (Rochambeau)!")
    player_score = 0
    computer_score = 0
    ties = 0
    round_num = 1
    while True:
        print("\n==============================")
        print(f"  Round: {round_num}")
        print("==============================")
        print(f"|  You  | Computer |  Ties  |")
        print(f"|  {player_score:^4} |   {computer_score:^7} |  {ties:^5} |")
        print("==============================\n")
        player = get_player_choice()
        if player in ['4', 'e', 'q', 'x', 'exit', 'quit']:
            print("Thanks for playing!")
            return
        computer = get_computer_choice()
        print()
        animate_ascii(player, computer)
        result = determine_winner(player, computer)
        print(result)
        time.sleep(2)
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        else:
            ties += 1
        round_num += 1

if __name__ == "__main__":
    main()
