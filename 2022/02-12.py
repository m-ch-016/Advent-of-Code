import re, time, hashlib

inputFile = open('input.txt', 'r')
inputStr = inputFile.readlines()

totalScore = 0

for choice in range(len(inputStr)):
tempScore = 0
	oppChoice = inputStr[choice][0]
	myChoice = inputStr[choice][2]

	# print(oppChoice)
	# print(myChoice)


	if oppChoice == 'A' and myChoice == 'X':
		tempScore += 3
	if oppChoice == 'A' and myChoice == 'Y':
		tempScore += 4
	if oppChoice == 'A' and myChoice == 'Z':
		tempScore += 8 

	if oppChoice == 'B' and myChoice == 'X':
		tempScore += 1
	if oppChoice == 'B' and myChoice == 'Y':
		tempScore += 5
	if oppChoice == 'B' and myChoice == 'Z':
		tempScore += 9

	if oppChoice == 'C' and myChoice == 'X':
		tempScore += 2
	if oppChoice == 'C' and myChoice == 'Y':
		tempScore += 6
	if oppChoice == 'C' and myChoice == 'Z':
		tempScore += 7

	totalScore += tempScore

print(totalScore)
