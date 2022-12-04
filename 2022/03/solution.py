import re, time, hashlib

inputFile = open('input.txt', 'r')
inputStr = inputFile.readlines()

letterArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

priorityArray = []

#TASK 1
for string in range(len(inputStr)):
	eleString = inputStr[string]
	
	firstHalf = eleString[:(len(eleString) //2 )]
	secondHalf = eleString[(len(eleString) //2 ):]

	tempArray = list(set(firstHalf) & set(secondHalf))
	for i in range(len(tempArray)):
		priorityArray.append(tempArray[i])
	
#TASK 2
for string in range(0, len(inputStr), 3):
	firstStr = inputStr[string].replace('\n', '')
	secondStr = inputStr[string+1].replace('\n', '')
	thirdStr = inputStr[string+2].replace('\n', '')

	tempArray = list(set(firstStr) & set(secondStr) & set(thirdStr))
	for i in range(len(tempArray)):
		priorityArray.append(tempArray[i])
	
counter = 0

for i in range(len(priorityArray)):
	counter += (letterArray.index(priorityArray[i])) + 1

print(counter)
