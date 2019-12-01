from random import randint
import json
import datetime

class Result:
    def __init__(self, first_name = "Name", last_name = "Surname", level = "medium", score=[], datetime=str(datetime.datetime.now())):
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.score = score
        self.datetime = datetime

    def create_dictionary(self):
        return self.__dict__

def hello():
    print("Welcome to the game Guess a secret number!")
    name = input("Please, enter your name: ").strip().lower().title()
    surname = input("and your surname: ").strip().lower().title()
    print("Thank you! Now...")
    return name, surname

def good_bye():
    print("\nThank you for playing with us. Good bye!")

#function, where user selects the level of dificulty
def select_level():
    level = input(f"Please enter the level of difficulty (easy, medium, hard): ").strip().lower()
    max_num = 100
    if level == "easy":
        max_num = 10
    elif level == "hard":
        max_num = 1000
    return max_num, level

#function for one round of the game
def play_round(min_num = 1, max_num = 100):
    secret_number = randint(min_num, max_num)
    print(f"The computer has just generated the secret number, i.e. an integer between {min_num} and {max_num}. "
          f"Try to guess, which one it is.")
    correct = False
    score = []
    while not correct:
        guess = read_number(min_num, max_num) #user inserts one guess
        score.append(guess)
        if guess == secret_number:
            if len(score) == 1:
                print("Congratulations! You have guessed the secret number in the first trial.")
            else:
                print(f"Congratulations! You have guessed the secret number in {len(score)} trials.")
            correct = True
        elif guess > secret_number:
            print("Wrong! Your number is higher than the secret number. Keep on guessing.")
        else:
            print("Wrong! Your number is lower than the secret number. Keep on guessing.")
    return score

#function that reads users guesses
def read_number(min_num, max_num):
    entry = False
    while not entry:
        try:
            guess = int(input("Enter your guess: ").strip())
            if guess > max_num:
                print(f"ERROR: The entered value is grater than the upper limit ({guess} > {max_num}). Please retry!")
            elif guess < min_num:
                print(f"ERROR: The entered value is lower than the lower limit ({guess} < {min_num}). Please retry!")
            else:
                entry = True
        except ValueError:
            print("ERROR: The value you have entered is not an integer. Please retry!")

    return guess

#the main function of the program
def play():
    all_results_game = []

    name, surname = hello() #calls function hello
    replay = True
    level_selection = True
    while replay:
        if level_selection:
            max_num, level = select_level() #asks user to select the level of the game
        score = play_round(max_num = max_num) #calls the function that plays a round of the game
        #score_dictionary[level].append(score)
        answer_play = input("Would you like to play another round (yes/no)? ").strip().lower() #asks user to play another game and select another level
        if answer_play == "no":
            replay = False
        else:
            answer_level = input("Would you like to select another level of difficulty (yes/no)? ").strip().lower()
            level_selection = True
            if answer_level == "no":
                level_selection = False
        #creating an object for each round played
        result = Result()
        result.first_name = str(name)
        result.last_name = str(surname)
        result.level = level
        result.score = score
        result.datetime = str(datetime.datetime.now())

        all_results_game.append(result)
    all_results = write_score_to_file(all_results_game) #reads the score file if it exists and appends the score of this game to the file
    print_score(all_results, all_results_game, name, surname)  # print current and total score
    good_bye() #bids user good bye

#this function reads the score file if it exists and appends the score of this game to the file
def write_score_to_file(all_results_game):
    all_results = []
    try:
        with open("results.txt", "r") as input_file:
            all_results = json.loads(input_file.read())
            for result in all_results_game:
                all_results.append(result.create_dictionary())
    except FileNotFoundError:
        for result in all_results_game:
            all_results.append(result.create_dictionary())
    with open("results.txt", "w") as output_file:
        output_file.write(json.dumps(all_results))

    return all_results

#function calculates current and total score
def print_score(all_results, all_results_game, name, surname):
    dictionary_game = {"easy": [], "medium": [], "hard": []}
    for result in all_results_game:
        level_game = result.level
        dictionary_game[level_game].append(result.score)

    print("\nYour score in this game:")
    for level in dictionary_game:
        print("Level:", level)
        print("    games played:", len(dictionary_game[level]))
        if len(dictionary_game[level]) != 0:
            print("    your best score:", min(len(x) for x in dictionary_game[level]), "guesses")

    dictionary_total = {"easy": [], "medium": [], "hard": []}
    for result in all_results:
        if result["first_name"] != name or result["last_name"] != surname:
            continue
        level_total = result["level"]
        dictionary_total[level_total].append(result["score"])

    print("\nYour total score:")
    for level in dictionary_total:
        print("Level:", level)
        print("    games played:", len(dictionary_total[level]))
        if len(dictionary_total[level]) != 0:
            print("    your best score:", min(len(x) for x in dictionary_total[level]), "guesses")

#starts playing the game
if __name__ == "__main__":
    play()
