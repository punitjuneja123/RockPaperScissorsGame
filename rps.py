import random
user_choice=""
computer_choice=""
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'q']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = get_user_choice()
    if user_choice == 'q':
        return False

    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == "draw":
        print("It's a draw!")
    else:
        print(f"{winner.capitalize()} wins!")

    return winner

def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        print("\nRock, Paper, Scissors")
        print("---------------------")

        result = play_round()
        if not result:
            break

        if result == "user":
            user_wins += 1
        elif result == "computer":
            computer_wins += 1
        else:
            draws += 1

        print("\nScore")
        print("-----")
        print(f"You: {user_wins}  Computer: {computer_wins}  Draws: {draws}")

if __name__ == '__main__':
    play_game()
