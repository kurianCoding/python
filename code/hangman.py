## this program promts the player with a question.
## each player is to enter the answer with a single word. If he cannot
## the bot will give a clue about the word. Depending on the difficulty
## level of the bot the player will have 10 to 20 attempts at the word.
## if the player answers correctly points will be rewarded along with name
##  going on the score board. the player will then attempt the next word

## reads a json file and updates the words and their hints in an array
## it also inits a user object which identifies user either by a userna
## me or by random number.
def init()

## this function reads user in put from terminal
## it displays a string which is the user name and uses this as prompt
def getUserInput()

## this function takes a string as the input  and either
## 1. calls the score function to display the score board
## 2. calls the tryAnswer function
## 3. calls updateUser function
def switchFunction(command)

## this function takes. As an input, if this string matches the answer
## it calls the score board function. If it doesn't match the answer it
## prints the next clue. If there are no mor clues to print then it returns false
def tryAnswer(word)

## updates the score and the current score. It prints score and user na
## me 
def scoreBoard(score,user)


## takes in user class object instances. It takes in current user and
## next user. It returns a string which is the username of the new user
def updateUser(current_user,next_user)
