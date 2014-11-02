import random

word = ""
let = ""
a = []


def difficulty():
	dif = raw_input("Select Difficulty: 1    2    3\n")
	if dif == "1":
		lives = 10
		print "You have selected difficulty 1 (10 lives)\n"
	elif dif == "2":
		lives = 7
		print "You have selected difficulty 2 (7 lives\n"
	elif dif == "3":
		lives = 3
		print "WATCH OUT, WE'VE GOT A BOSS OVER HERE!! (3 lives)\n"
	else:
		print "Please type only 1 number between 1 and 3\n"
	return lives


def random_word():
	words = ["wind", "victory", "journalism", "movie", "comma", "defenestrate"]
	ranword = words[random.randint(0, 5)]
	word = ranword
	return word

def guess():
	letter = raw_input("Guess a letter\n")
	return letter


def word_slots(word):
	for l in word:
		slots.append("_ ")
	print slots


def replace(word, letter, answer):
	for l in range(len(word)):
		if letter.lower() == word[l].lower():
			answer[l] = letter
	return word

def get_slots(word):
	a = list(word)
	print a
	for l in range(len(a)):
		a[l] = "_ "
	print a
	return a


#does this work?


print "HANGMAN"
word = random_word()
print word
a = get_slots(word)
life = difficulty()
print life
while True:
	let = guess()
	if let in word:
		replace(word, let, a)
		print a
	else:
		if life > 0:
			life -= 1
			print "You have %n lives left" % life
		else:
			print "You lose! :C"
			break


