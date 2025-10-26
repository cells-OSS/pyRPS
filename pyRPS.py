import random
import sys
import os

CHOICES = ("r", "p", "s")

if os.name == "nt":
    config_dir = os.path.join(os.getenv("APPDATA"), "pyndcrypt")
else:
    config_dir = os.path.expanduser("~/.config/pyndcrypt")

os.makedirs(config_dir, exist_ok=True)

rigging_config_path = os.path.join(config_dir, "rigging.conf")

def get_computer_choice():
    return random.choice(CHOICES)


def get_player_choice():
    while True:
        playerChoice = input("Choose rock/paper/scissors(r/p/s): ")
        if playerChoice in CHOICES:
            return playerChoice
        if playerChoice.lower() == "finish":
            return None
        print("Invalid choice. Try again.")
        input("Press Enter to continue...")
        os.execv(sys.executable, [sys.executable] + sys.argv)


def decide_winner(player, comp):
    if player == comp:
        return "tie"
    wins = {
        ("r", "s"),
        ("s", "p"),
        ("p", "r"),
    }
    return "player" if (player, comp) in wins else "computer"


def main():
    print("rock paper scissors")
    score_p = score_c = 0
    while True:
        player = get_player_choice()
        if player is None:
            break
        comp = get_computer_choice()
        print(f"You: {player}  |  Computer: {comp}")
        result = decide_winner(player, comp)
        if result == "tie":
            print("It's a tie.")
        elif result == "player":
            score_p += 1
            print("You win this round.")
        else:
            score_c += 1
            print("Computer wins this round.")
        print(f"Score — You: {score_p}  Computer: {score_c}\n")
    print("Thanks for playing. Final score:", score_p, "-", score_c)
    input("Press any key to exit...")
    sys.exit()


if __name__ == "__main__":

    welcomeMessage = """============Welcome to PyRPS - Rock Paper Scissors!============
1 = Play
2 = Settings
TIP: Type 'finish' at any time to end the game.
    """
    print(welcomeMessage)

    chooseOption = input("Which option would you like to choose(1/2)?: ")
    
    if chooseOption == '1':
        main()

    if chooseOption == '2':
        settingsMenu = """
==================SETTINGS==================
1 = Rigging
2 = Change welcome message (Coming Soon...)
3 = Reset welcome message (Comming Soon...)
4 = Figlet welcome message (Comming Soon...)
"""
print(settingsMenu)

settingsOption = input("Which Setting would you like to change(1/2/3/4)?: ")

if settingsOption == '1':
    riggingMenu = """
==================RIGGING==================
1 = Make the bot win
2 = Make the user win
"""
    print(riggingMenu)

    riggingOption = input("Who do you want to win(1/2)?: ")

    if riggingOption == '1':
        config_path = os.path.join(config_dir, "rigging.conf")

        with open(config_path, "wb") as f:
            f.write("True".encode())
        print("Rigging has been done!")
        input("Press Enter to continue...")
        os.execv(sys.executable, [sys.executable] + sys.argv)