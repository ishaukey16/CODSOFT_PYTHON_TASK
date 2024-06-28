import random

user_wins = 0
computer_wins = 0
total_games = 0

user_name = input("What's your name? ")
print(f"Welcome, {user_name}, to the Rock-Paper-Scissors game!")
print("Please enter 'rock', 'paper', or 'scissors' to make a choice.")

# Game rules
rules = {
    'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
    'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
    'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'}
}

while True:
    user_choice = input("Enter your choice: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice: ").lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    result = rules[user_choice][computer_choice]
    if result == 'win':
        print("You win!")
        user_wins += 1
    elif result == 'lose':
        print("Computer wins!")
        computer_wins += 1
    else:
        print("It's a tie!")

    total_games += 1
    print(f"Score - You: {user_wins}, Computer: {computer_wins}, Total Games: {total_games}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
