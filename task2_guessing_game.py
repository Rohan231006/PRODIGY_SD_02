"""
PRODIGY INFOTECH INTERNSHIP - TASK 2
Guessing Game
Generates a random number and challenges the user to guess it
"""

import random

def get_difficulty():
    print("\n  Select Difficulty:")
    print("  1. Easy   (1 - 50)")
    print("  2. Medium (1 - 100)")
    print("  3. Hard   (1 - 500)")
    while True:
        choice = input("\n  Enter choice (1/2/3): ").strip()
        if choice == '1':
            return 1, 50, "Easy"
        elif choice == '2':
            return 1, 100, "Medium"
        elif choice == '3':
            return 1, 500, "Hard"
        else:
            print("  ❌ Invalid choice. Enter 1, 2, or 3.")

def play_game():
    low, high, difficulty = get_difficulty()
    secret = random.randint(low, high)
    attempts = 0
    max_attempts = {"Easy": 10, "Medium": 7, "Hard": 12}[difficulty]

    print(f"\n  🎮 [{difficulty}] I've picked a number between {low} and {high}.")
    print(f"  You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        guess_input = input(f"  Attempt {attempts+1}/{max_attempts} | Guesses left: {remaining} → ").strip()

        if guess_input.lower() == 'exit':
            print(f"\n  The number was {secret}. Better luck next time!")
            return

        try:
            guess = int(guess_input)
        except ValueError:
            print("  ❌ Please enter a valid integer.")
            continue

        if guess < low or guess > high:
            print(f"  ⚠️  Please guess within range ({low}–{high}).")
            continue

        attempts += 1

        if guess == secret:
            print(f"\n  🎉 CORRECT! The number was {secret}.")
            print(f"  You guessed it in {attempts} attempt(s)!")
            if attempts == 1:
                print("  🏆 WOW — First try! Incredible!")
            elif attempts <= max_attempts // 3:
                print("  ⭐ Excellent performance!")
            elif attempts <= max_attempts // 2:
                print("  👍 Good job!")
            else:
                print("  😅 Made it just in time!")
            return
        elif guess < secret:
            diff = secret - guess
            hint = "🔥 Very close!" if diff <= 5 else ("👆 Go higher!" if diff <= 20 else "⬆️  Way too low!")
            print(f"  {hint}  (Too LOW)")
        else:
            diff = guess - secret
            hint = "🔥 Very close!" if diff <= 5 else ("👇 Go lower!" if diff <= 20 else "⬇️  Way too high!")
            print(f"  {hint}  (Too HIGH)")

    print(f"\n  ❌ Out of attempts! The number was {secret}.")
    print("  Better luck next time! 💪")

def main():
    print("\n" + "="*44)
    print("   🎲  NUMBER GUESSING GAME  🎲")
    print("   Prodigy Infotech Internship - Task 2")
    print("="*44)

    while True:
        play_game()
        again = input("\n  Play again? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("\n  Thanks for playing! 👋\n")
            break

if __name__ == "__main__":
    main()
