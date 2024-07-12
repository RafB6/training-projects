import random

#returns a random word from words[]
def getWord():
    words = [
        "Apple", "River", "Mountain", "Computer", "Galaxy",
        "Elephant", "Harmony", "Jazz", "Whisper", "Sunrise",
        "Shadow", "Thunder", "Ocean", "Meadow", "Desert",
        "Forest", "Melody", "Breeze", "Volcano", "Rainbow"
    ]
    words_size = len(words)
    word = words[random.randint(0, words_size - 1)]
    return word

globalWord = getWord()
    
def getGuess():

    #guess counter
    current_guess_counter = 0
    guess = ""
    #Input validation
    while(len(guess) != 1 or guess.isalpha == False):
        if current_guess_counter:
            print("Usage: 1 alphabetical character.")

        guess = input("Guess a letter: ")
        current_guess_counter+=1
    return guess

# list of missed guesses
misses = []
# function checks if guess was hit or missed
# returns value code to handle later and shows list of missed guesses
def checkGuess(guess):
    if guess in globalWord:
        print("HIT!")
        return 10
    else:
        if guess in misses:
            print("You tried this already!")
        else:
            print("MISSED!")
            misses.append(guess)
        
        print("Missed: ", end=" ")
        for i in misses:
            print(i, end=" ")
        print("]")
        return 20

#function checks if the game has ended
#return specified code for each result or if game is continued
def check(game_key, miss_count):
    if str(game_key) == globalWord:
        return 0
    elif miss_count > 12:
        return 1
    else:
        return 2

#actual game function
def game():

    #creates hashed game word
    game_key = ""
    for i in globalWord:
        game_key += "_"

    #miss count
    miss_count = 0


    print("HANGMAN")

    #initializing game_result to 2 so the game will continue
    game_result = 2
    
    #game loop that stops when player won or lost
    while(game_result == 2):
        print(game_key)
        
        curr_guess = getGuess()
        # increments miss_counter if player missed
        if (checkGuess(curr_guess) == 20):
            miss_count+=1
        # reveals guessed letter
        elif (checkGuess(curr_guess) == 10):
            index = globalWord.find(curr_guess)
            print(index)
            game_key = list(game_key)
            game_key[index] = curr_guess
            temp = ""
            for i in game_key:
                temp += i
            game_key = temp
            
        #check game's state
        game_result = check(game_key, miss_count)
    
    #check if player lost or won
    if game_result:
        print("You've exceeded your guess limit, you lose!")
        print("Word: ", globalWord)
    else:
        print("YOU WIN!")


game()


