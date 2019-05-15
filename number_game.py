#Number guessing

import logging

#logging.basicConfig(filename= 'logfile.log', level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('handler.log')
fh.setLevel(logging.CRITICAL)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

#Comment out these two lines to turn off the logger
logger.addHandler(fh)
logger.addHandler(sh) #specifically comment out this line to stop logging to the console

import random

def greet():
	"""Greets the user and give them the instructions"""
	logger.debug("greet() entered")
	print("Hello! This game is simple. Just pick a number and I will tell you if you are too low or too high until you have guessed the correct number.")
	print("If you get it on the first guess, you get 5 points. If you get it on the second guess, you get 4 points and so on.")

def generateRandomNumber(low, high):
	"""Generates a number between low and high inclusively"""
	logger.debug("generate RandomNumber(low,high) entered with " +str(low) + " " + str(high))
	randomNum = random.randint(low,high)
	return randomNum
	
def promptForGuess():
	"""Prompts for the user to guess a number"""
	logger.debug("promptForGuess() entered")
	while True:
		try:
			guess = int(input("Pick a number between 1 and 10\n"))
			if(guess >= 1 and guess <= 10):
				return guess
			logger.critical(str(guess) + " was entered, it is not between 1 and 10 inclusively")
		except ValueError:
			print("That is not a number.")
			logger.critical(str(guess) + " was entered, it is not an integer")
	
def checkGuess(guess, randomNum):
	"""Checks if the user's guess is less than, more than, or equal to the random number"""
	logger.debug("checkGuess(guess,randomNum) entered with " +str(guess) + " " + str(randomNum))
	if(guess == randomNum):
		print("You got it!")
		return True
		
	elif(guess > randomNum):
		print("Too high")
		return False
		
	elif(guess < randomNum):
		print("Too low")
		return False


def playAgain():
	"""Asks the user if they want to play again"""
	logger.debug("playAgain() entered")
	while True:
		answer = str(input("Would you like to play again? Yes or No\n"))
		logger.debug("answer = " + str(answer))
		if(answer.lower() == "y" or answer.lower() == "yes"):
			return True
		
		elif(answer.lower() == "n" or answer.lower() == "no"):
			return False
		logger.critical(str(answer) + " does not equal y, n, yes, or no")

def goodbye(score):
	"""Thanks the user for playing and gives them their final score"""
	logger.debug("goodbye(score) entered with " + str(score))
	print("Thank you for playing! Your final score was " + str(score) + ".")

def play():
	"""Runs the game"""
	logger.debug("play() entered")
	score = 0
	
	#Greets the user
	greet()
	logger.debug("greet exited")
	
	#Loop for the whole program, user exits if they say no to playing again
	while True:
		#Generates the random number
		randomNum = generateRandomNumber(1,10)
		logger.debug("generateRandomNumber(low,high) exited, returning randomNum = " + str(randomNum))
		#Number to be added to the score if they guess correctly
		scoreAddition = 5
		
		#Loop for a single game, user exits once they guess the correct number
		while True:
			#Asks the user to guess
			guess = promptForGuess()
			logger.debug("promptForGuess() exited, returning guess = " + str(guess))
			#Checks the user's guess
			result = checkGuess(guess,randomNum)
			logger.debug("checkGuess(guess,randomNum) exited, returning result = " + str(result))
			if(result == True):
				score = score + scoreAddition
				print(str(scoreAddition) + " points have been added to your score.")
				print("Your current score is " + str(score))
				break
				
			#If they got it wrong, the number that will be added to their total score is decremented by 1. It cannot go below 1.
			logger.debug("scoreAddition = " + str(scoreAddition))
			if(scoreAddition != 1):
				scoreAddition -= 1
		
		#Asks the user if they want to play again
		response = playAgain()
		logger.debug("playAgain() exited, returning response = " + str(response))
		if(playAgain() == False):
			break
			
	#Thanks the user for playing and gives them their final score
	goodbye(score)
	logger.debug("goodbye(score) exited")
	
play()
