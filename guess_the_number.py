import random

random_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        attempts += 1
        print(f"\nAttempt : {attempts}")
        guess = int(input("Guess the number (1 - 100) : "))

        if guess > random_number:
            print("Number is higher! Guess a lower number.")
        elif guess < random_number:
            print("Number is lower! Guess a higher number.")
        elif guess == random_number:
            print(f"Hurray!! You guessed it right in {attempts} attempts.")
            break

    except TypeError:
        print("Enter a valid number!")

if attempts == max_attempts:
    print("\nOops!! Out of attempts!! Better luck next time!!")
