import random
import sys
import os

CHOICES = ("rock", "paper", "scissors")


def get_computer_choice():
    return random.choice(CHOICES)


def get_player_choice():
    while True:
        playerChoice = input("Choose rock/paper/scissors: ")
        if playerChoice in CHOICES:
            return playerChoice
        print("Invalid choice. Try again.")
        os.execv(sys.executable, [sys.executable] + sys.argv)


def decide_winner(player, comp):
    if player == comp:
        return "tie"
    wins = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
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


if __name__ == "__main__":
    main()