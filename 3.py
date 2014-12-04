#3 in a row
import random
names = []
gameBoard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
def inputNames():
	name1 = raw_input("Enter first player's name here: \t")
	name2 = raw_input("Enter second player's name here: \t")
	return name1, name2

def first(name1, name2):
	num1 = int(raw_input("%s, guess a number between 1 and 10, closest person wins and get to go first!\t" % name1))
	num2 = int(raw_input("%s, pick a number\t" % name2))
	if num2 == num1:
		num2 = int(raw_input("%s, choose a different number" % name2))
	RNG = random.randint(0, 10)
	print ("%d is the number" % RNG)
	if abs(num1 - RNG) > abs (num2 - RNG):
		print "%s goes first" % name2
	else:
		print "%s goes first" % name1

def move(board):
	mov = raw_input("Pick a number between 1 and 9 (that hasn't been picked already)")
	for listt in board:
		for subvalue in range(len(listt)):
			if mov == subvalue:
				listt[subvalue]= "X"
				print board
			






#names = inputNames()
#first(names[0], names[1])
move(gameBoard)


	
