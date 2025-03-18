from random import randint
def roll():
        """Generates a random number from 1-6"""
        return randint(1,6)
def main():
	"""Runs "roll()" a user specified ammount of times, printing each result and the average at the end"""
	total=0
	print("How many dice would you like to roll?")
	repeat=0
	while (not (isinstance(repeat,int)) or (repeat <=0)):
		try:
			repeat=int(input())
		except ValueError:
			print("Please enter an integer.")
		else:
			print("Please enter a positive number.")
	for i in range(repeat):
		Roll=roll()
		print (f"Dice {i+1}: {Roll}")
		total+=Roll
	print(f"You rolled an average of {total/repeat:.3f} in {repeat} rolls!")
if __name__ == "__main__":
	main()
