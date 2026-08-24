import random
game_name ="WordRaiderGame"

# read in words per line from words.txt

word_list = []
with open("words.txt") as f:
    for line in f:
        words = line.rstrip().lower()
        word_list.append(words)


# pick a random word from the word list
random_word = random.choice(word_list)

# variables to track game state

misplaced_letters = []
incorrect_letters = []
max_turns = 8
current_nr_turns = 0

print(f"Welcome to {game_name}!")
print(f"The word has 5 letters to guess. \nYou have {max_turns-current_nr_turns} turns left to guess the word.")

## validation logic
while current_nr_turns < max_turns:
    input_val = input("What is your guess?")
    input_val = input_val.lower()
    if len(input_val) != 5 or not input_val.isalpha():
        print("Your input format is wrong. It must be letters only and at most 5 letters long.")
        continue
    else:

        for index, char in enumerate(input_val):
            if char == random_word[index]:
                print(f"{char} is correct")
                if char in misplaced_letters:
                    misplaced_letters.remove(char)

            elif char in random_word:
                print(f"{char} is misplaced")
                if char not in misplaced_letters:
                    misplaced_letters.append(char)
            else:
                print(f"{char} is incorrect")
                if char not in incorrect_letters:
                    incorrect_letters.append(char)

    print(f"Misplaced letters: {misplaced_letters} \nIncorrect letters: {incorrect_letters}")
    current_nr_turns += 1

    if input_val == random_word:
        print("Congratulations! You guessed the word!")
        break

    if current_nr_turns == max_turns:
        print(f"You failed to guess the word in {max_turns} turns. Game over. The word was '{random_word}'.")
    else:
        print(f"You have {max_turns - current_nr_turns} turns left to guess the word.")


# checking for a win or loss

