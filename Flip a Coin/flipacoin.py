from random import randint


'''
Flip a coin game
'''

playing = True

while playing:
	print("Welcome to Flip a Coin!")
	
	coin = randint(0,1)

	if coin == 0:
		print("You flipped heads!")
	else:
		print("You flipped tails!")

	if (input("Do you want to play again? y/n: ") != 'y'):
		playing = False



