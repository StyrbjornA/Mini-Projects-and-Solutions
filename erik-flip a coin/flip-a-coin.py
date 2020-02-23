import random
flipcoin = input("Flip a coin? y/n")
if (flipcoin == "y") :
	if (random.choice([0,1]) == 1) :
		print("Heads")
	else :
		print("Tails")
