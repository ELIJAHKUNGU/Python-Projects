import time

#Welcome the user
name =input("What is your Name? ")

print("Hello ," +name, "Time to play Hangman !")
print("")

#wait for 1 second
time.sleep(1)
print()
"start guessing ......"
time.sleep(0.5)

#Here we set the secret
word = "Secret"

# create an variable with an empty value
guesses = ''
#determine the number of turns
turns = 10

# Create a while loop
#check if the turns are more than zero

while turns > 0:
    #make a counter that start with zero
    failed = 0
    #for Every character in secret_word
    for char in word:
        #see if the charat=cter is in the players guess
        if char in guesses:
            #print then out the character
            print(char),

        else:
            #if not found print a dash
            #print(" __")
            #and increase the failed counter with one
            failed += 1

            #if failed is equal to zero


    #print You won
    if failed == 0:
        print("You won")

#Exit the script
#break;
print()

#Ask the user go  guess a character
guess =input("guess a character:")

#set the players guess to guesses
guesses += guess

#if the guess is not found in the secret word
if guess not in word:
    #Turns counter decrease wit 1 (now 9)
    turns -= 1


    #Print wrong
    print("Wrong")
print("You have ", +turns , 'More guesses')

#If the turns are equal to zero
if turns == 0:
    #print "You loose dear"
    print('You loose')
