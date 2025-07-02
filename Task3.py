import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("❌ Invalid input. Please choose rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("--------------------------------------")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"🧑 You chose: {user_choice}")
        print(f"🤖 Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("✅ You win this round!")
            user_score += 1
        elif winner == "computer":
            print("❌ You lose this round.")
            computer_score += 1
        else:
            print("🤝 It's a tie!")

        print(f"📊 Score: You {user_score} - Computer {computer_score}")

        play_again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\n🏁 Game Over!")
            print(f"🎉 Final Score: You {user_score} - Computer {computer_score}")
            break

        round_number += 1

# Start the game
play_game()
