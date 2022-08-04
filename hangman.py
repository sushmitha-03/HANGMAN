import random
def hang():
    print("*WELCOME! IN HANGMAN GAME*")
    print("THIS IS WORD GUESSING GAME")
    print("Hangman about guessing letters (A-Z) to form the words")
    print("If the player guesses the right letter that is within the word, the letter appears at its correct position.") 
    print("The user has to guess the correct word until a man is hung, then the game is over.")
    name = input("What is your name? ")
    print("Good Luck ! ", name)
words = ['python', 'variable', 'datatype', 'operator',
 	'loop', 'list', 'function', 'file',
	'json', 'webscrapping', 'request', 'hangman']
word = random.choice(words)
a=set("abcdefghijklmnopqrstuvwxyz")
print("Guess the characters")
guesses = ''
turns = 10
while len(word)!=0:
    main=""
    for char in word:
        if char in guesses:
            main+=char
        else:
            main+="_ "
        if main==word:
            print(main)
            print("You Win")
            break
        print("Guess now:",main)
        guess = input("guess a character:")
        if guess in a:
            guesses+=guess
        else:
            print("Invalid character!")
        if guess not in word:
            turns-=1
            print("You have",turns,"only")
            if (turns == 9):
                print ("|")
                print ("|____")
            elif (turns == 8):
                print ("|")
                print ("|")
                print ("|")
                print ("|")
                print ("|____")
            elif (turns == 7):
                print ("___")
                print ("|	 |")
                print ("|")
                print ("|")
                print ("|")
                print ("|")
                print ("|____")
            elif (turns == 6):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|")
                print ("|")
                print ("|")
                print ("|____")
            elif (turns == 5):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	 |")
                print ("|	")
                print ("|")
                print ("|____")
            elif (turns == 4):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|")
                print ("|	 ")
                print ("|")
                print ("|____")
            elif (turns == 3):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 ")
                print ("|")
                print ("|____")
            elif (turns == 2):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 |")
                print ("|")
                print ("|____")
            elif (turns == 1):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 |")
                print ("|	/ ")
                print ("|____")
            elif (turns == 0):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 |")
                print ("|	/ \ ")
                print ("|____")
                print ("\nYOU LOSE! TRY AGAIN!")
                print ("\nWould you like to play again?")
                again=input("Enter Y or N:")
                if again=="Y":
                    hang()
                else:
                    print("Thanks for playing!!")
                    break
hang()