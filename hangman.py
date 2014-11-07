#import crap
import random





#hi guys im writing a comment and ya its fun so this is great grammar and ya
#Death to the rebles
#Rawwwwwwwwr
#conflict is good for the soul
#variables
word = ""
let = ""
a = []
go_back = 0
#1 or 2 players?
def selection():
	text = raw_input("1 or 2 Players?\t").lower()
	if text == "1":
		return "one_player"
	elif text == "2":
		return "two_player"
	else:
		print "incorrect"
#if 1 player
def	one_player():
	words = ["wind", "victory", "journalism", "movie", "comma", "defenestration"]
	word = random.choice(words)
	return word
#if 2 player
def	two_player():
	text = raw_input("Pick a Word...").lower()
	return text

#select difficulty/lives
def difficulty():
	dif = raw_input("Select Difficulty: 1    2    3\n")
	if dif == "1":
		lives = 10
		print "You have selected difficulty 1 (10 lives)\n"
		return lives
	elif dif == "2":
		lives = 7
		print "You have selected difficulty 2 (7 lives\n"
		return lives
	elif dif == "3":
		lives = 3
		print "WATCH OUT, WE'VE GOT A BOSS OVER HERE!! (3 lives)\n"
		return lives
	else:
		print "Please type only 1 number between 1 and 3\n"
		exit()

#get a random word
def random_word():
	words = open("dictionary.txt", "r")
	content = [x.strip('\n') for x in words.readlines()]
	ranword = content[random.randint(0, len(content))]
	word = ranword
	return word
#guess a letter
def guess():
	letter = raw_input("Guess a letter\n").lower()
	return letter
#this replaces the _ with the correctly guessed letter
def replace(word, letter, answer):
	for l in range(len(word)):
		if letter.lower() == word[l].lower():
			answer[l] = letter
	return word
#turns word from string into list then back into a string. Why? BECAUSE I SAID SO!
def get_slots(word):
	a = list(word)
	for l in range(len(a)):
		a[l] = '_ '
	print ''.join(a)
	return a

#This is a dead man

#main function
print """   		HANGMAN
           _______
          |/      |
          |      (_)
          |      \|/
          |       |
          |      / |
          |
         _|___"""

while True:
	go_back = 0
	sel = selection()
	if sel == "one_player":
		word = random_word()
		life = difficulty()
		a = get_slots(word)
		print life
		while go_back != 1:
			let = guess()
			if let in word:
				replace(word, let, a)
				print ''.join(a)
				if word == ''.join(a):
					print "Congratulations, you win!"
					go_back = 1
			else:
				if life > 0:
					life -= 1
					print "You have %d lives left" % life
				else:
					print "You lose! :C, the word was %s" % word
					go_back = 1
	elif sel == "two_player":
		word = two_player()
		life = difficulty()
		a = get_slots(word)
		print life
		while go_back != 1:
			let = guess()
			if let in word:
				replace(word, let, a)
				print ''.join(a)
				if word == ''.join(a):
					print "Congratulations, you win!"
					go_back = 1
			else:
				if life > 0:
					life -= 1
					print "You have %d lives left" % life
				else:
					print "You lose! :C"
					go_back = 1
