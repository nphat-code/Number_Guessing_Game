import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

choice = int(input("Enter your choice: "))

difficulty = {
    1: "Easy",
    2: "Medium",
    3: "Hard"
}

num_of_chances = {
    1: 10,
    2: 5,
    3: 3
}

print(f"Great! You have selected the {difficulty[choice]} difficulty level.")
print("Let's start the game!")

num = random.randint(1, 100)
cnt = 0
while True:
    if cnt == num_of_chances[choice]:
        print("You lose!")
        break
    else:
        guess = int(input("Enter your guess: "))
        if guess > num:
            print(f"Incorrect! The number is less than {guess}.")
        elif guess < num:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Congratulations! You guessed the correct number in {cnt} attempts.")
            break
        cnt += 1
        