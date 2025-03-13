from random import randint
total=0
print("How many dice would you like to roll?")
repeat=int(input())
def Roll():
	return randint(1,6)
for i in range(repeat):
	roll=Roll()
	print ("Dice ",i+1,": ",roll)
	total+=roll
print("You rolled an average of ",total/repeat,"in ",repeat," rolls!")
