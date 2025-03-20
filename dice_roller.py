def main():
	"""Demonstrating the methods made in dice_roller"""
	die=roller_class(6)
	print(f"Single roll: {die.roll()}")
	print(f"10 roll sum: {die.roll_multiple(10)}")
	print(f"Probability of rolling 3: {die.probability_of_num(3)}")
	print("log 10 rolls: ")
	die.log_rolls(10)
if __name__ == "__main__":
	from random import randint
	from dice_class import roller_class
	main()
