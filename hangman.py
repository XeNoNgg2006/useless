import random


print("Choose the language of the words: (DE/ENG)")
lang_word = input()
lang_word.lower #makes lang choice to lower case 


if lang_word == "de":
    from words import  words_DE #import from words.py and words_DE is a variable in the file
    hidden_word = random.choice(words_DE)
    print("Random word:", hidden_word)
elif lang_word == "eng":
    from words import words_ENG #import from words.py and words_ENG is a variable in the file
    hidden_word = random.choice(words_ENG)
    print("Random word:", hidden_word)
else:
    print("Wrong Input")

print("WELCOME TO HANGMAN")
print("Your word length is", len(hidden_word) , "letters\n") #Intro

hidden_word = hidden_word.upper() #makes the hidden word UPCASE for safety 
array_hidden_word = list(" ".join(hidden_word)) #makes the hidden word into an Array ["H"," ","E"," ","L"," ","L"," ","O"," "], " " for spaces between letters

misses = 0
list_misses = "_ _ _ _ _ _ _ _ _ _ "
array_misses = list(list_misses)
index_misses = 0
def print_hangman(misses):
    list_misses
    hangman_stages = ["                \n"
                      "                \n"
                      "                             MISSES:              \n"
                      "                             " + list_misses + "\n" +
                      "                \n"
                      "                \n"
                      "                \n"
                      "                \n",  
                      "                \n"
                      "                \n"
                      "                             MISSES:              \n"
                      "                             " + list_misses + "\n" +
                      "                \n"
                      "                \n"
                      "                \n"
                      "_________________\n",  
                      "             |\n"
                      "             |               MISSES:              \n"
                      "             |               " + list_misses + "\n" +
                      "             |\n"
                      "             |\n"
                      "             |\n"
                      "             |\n"
                      "_____________|___\n",
                      "   ___________\n"
                      "             |\n"
                      "             |               MISSES:              \n"
                      "             |               " + list_misses + "\n" +
                      "             |\n"
                      "             |\n"
                      "             |\n"
                      "             |\n"
                      "_____________|___\n",
                      "   ___________\n"
                      "      |      |\n"
                      "             |               MISSES:              \n"
                      "             |               " + list_misses + "\n" +
                      "             |\n"
                      "             |\n"
                      "             |\n"
                      "             |\n"
                      "_____________|___\n",
                    "   ___________\n"
                      "      |      |\n"
                      "     (_)     |\n"
                      "             |               MISSES:              \n"
                      "             |               " + list_misses + "\n" +
                      "             |\n"
                      "             |\n"
                      "             |\n"
                      "_____________|___\n",
                      "   ___________\n"
                      "      |      |\n"
                      "     (_)     |               MISSES:              \n"
                      "      |      |               " + list_misses + "\n" +
                      "      |      |\n"
                      "      |      |\n"
                      "             |\n"
                      "             |\n"
                      "_____________|___\n",
                      "   ___________\n"
                      "      |      |\n"
                      "     (_)     |               MISSES:              \n"
                      "      |      |               " + list_misses + "\n" +
                      "      |      |\n"
                      "      |      |\n"
                     r"     /       |"+"\n" +
                      "             |\n"
                      "_____________|___\n",
                      "   ___________\n"
                      "      |      |\n"
                      "     (_)     |               MISSES:              \n"
                      "      |      |               " + list_misses + "\n" +
                      "      |      |\n"
                      "      |      |\n"
                     r"     / \     |"+"\n" +
                      "             |\n"
                      "_____________|___\n",
                      "   ___________\n"
                      "      |      |\n"
                      "     (_)     |               MISSES:              \n"
                     r"     \|      |               " + list_misses + "\n" +
                      "      |      |\n"
                      "      |      |\n"
                     r"     / \     |"+"\n"+
                      "             |\n"
                      "_____________|___\n",
                      "   ___________\n"
                      "      |      |\n"
                      "     (_)     |               MISSES:              \n"
                     r"     \|/     |               " + list_misses + "\n" +
                      "      |      |\n"
                      "      |      |\n"
                     r"     / \     |"+"\n" +
                      "             |\n"
                      "_____________|___\n\n"
                      "You have lost. The word was "+ hidden_word+"."
    ]
    
    if misses <= 10:
        print(hangman_stages[misses])


def startGame():
    while misses <= 10 and "_" in current_line: #while loop until there are no more lives left and there are "_" still in the word meaning you lost
            
            print("\033[4m        HANGMAN        \033[0m\n")
            print_hangman(misses)
            print(current_line,"\n")
            
            if misses < 10:
                print("Write a letter:")
                letter = input()
                check_letter(letter)

            if "_" not in current_line:
                print("\033[4m        HANGMAN       \033[0m\n")
                print_hangman(misses)
                print(current_line,"\n")
                print("You have won. The Word is", hidden_word)
                break

            if misses == 10:
                print("\033[4m        HANGMAN        \033[0m\n")
                print_hangman(10)

                print(current_line,"\n")
                break


def word_length():
    global var_underscore
    array_underscore = []
    length_Array= "_ " * len(hidden_word)
    array_underscore.append(length_Array)
    var_underscore = "".join(array_underscore)

word_length() #plays the function

current_line = var_underscore

def check_letter(letter):
    global current_line, misses, array_misses,index_misses,list_misses
    found = False
    index_letter = 0
    letter = letter.upper()

    for x in array_hidden_word:
        index_letter += 1
        if x == letter:
            array_line = list(current_line)
            array_line[index_letter - 1] = letter
            current_line = "".join(array_line)
            found = True
    
    if letter.isalpha() == False:
        print("Not from Alphabet")
    elif len(letter) > 1:
        print("to long")
    elif letter in array_misses:
        print("already used")
    elif not found:
        misses += 1 
        array_misses = list(array_misses)
        array_misses.pop(index_misses)
        array_misses.insert(index_misses, letter)
        index_misses += 1
        array_misses.pop(index_misses)
        array_misses.insert(index_misses, " ")
        index_misses += 1
        list_misses = "".join(array_misses)
        return list_misses
        


startGame()

 