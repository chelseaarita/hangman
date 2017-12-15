# asks user name what their name is and will capitalize it if it isn't
user_name = raw_input("Hey, what's your name? ")
user_name = user_name.capitalize()

# while loop starts
playing = True

# the word the user has to guess
word = "orange"
# the list of underscores that will be printed to the console
underscores = ["_", "_", "_", "_", "_", "_"]

# prints out underscores to console
print underscores

# keeping track of how many correct guesses they have.
correct = 0

# choosing a while loop because we want to make sure it repeats until the condition is met
while playing:
    
    # asking the user to guess a letter
    guess_letter = raw_input("Guess a letter: ")
    
    # conditional starts
    # when the user types in any of the letters the guessed word is
    if guess_letter in word:
        # if user guesses the letter 'o' which is correct
        if guess_letter == "o":
            # this will change the first index of the list of underscores
            underscores[0] = "o"
            # this will print out the underscores
            print underscores
            # keeping track of the score
            correct = correct + 1
        elif guess_letter == "r":
            underscores[1] = "r"
            print underscores
            correct = correct + 1
        elif guess_letter == "a":
            underscores[2] = "a"
            print underscores
            correct = correct + 1
        elif guess_letter == "n":
            underscores[3] = "n"
            print underscores
            correct = correct + 1
        elif guess_letter == "g":
            underscores[4] = "g"
            print underscores
            correct = correct + 1
        elif guess_letter == "e":
            underscores[5] = "e"
            print underscores
            correct = correct + 1
    else:
        print "That's incorrect. Keep guessing!"

    if correct == 6:
        print "Congratulations" + " " + user_name + "!" + " " + "You won!"
        break
    
# we should keep track of the letters the user is typing in and make sure they only type it in once
# otherwise, you can just press 'o' six times and it'll congratulate you.
# how do we keep track of that? empty string? empty list? 
# my head hurts.

# loop for hangman

# When someone guesses a letter wrong, a body part is drawn. In this case we'll ask the user to keep guessing.
# print "Keep guessing!"

# When someone guesses a letter correctly, place that letter on the correct underscore. 
# replaces underscore with correct letter

# Keep track of the errors and the correct letters
# correct = 0
# incorrect = 0

# When the player guesses the word, congratulate them for winning
# print congratulations (user_name)! Well done!

# When the player guesses a wrong letter, encourage them to keep guessing/trying.
# print "keep guessing!"