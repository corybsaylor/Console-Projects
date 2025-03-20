from random import randint
class roller_class:
	def __init__(self, n):
		"""Contructor that initialises the number of sides the dice will be simulated with"""
		self.num_sides=n
	def roll(self):
		"""Generates a random number between 1 and num_sides"""
		return randint(1,self.num_sides)
	def roll_multiple(self,num_rolls):
		"""Call roll() num_rolls times and return the sum"""
		total=0
		for i in range(num_rolls):
			total+=self.roll()
		return total
	def probability_of_num(self,num):
		"""Returns the probability of getting a specific number"""
		return(round(1/self.num_sides,5))
	def log_rolls(self,num_rolls):
		"""Call roll() num_rolls times and print the results"""
		total=0
		rolls=[]
		for i in range(num_rolls):
			rolls.append(self.roll())
			print(f"Dice {i+1}: {rolls[len(rolls)-1]}")
		for i in (rolls):
			total+=i
		print(f"Average roll: {total/num_rolls}")
