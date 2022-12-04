import re, time, hashlib

inputFile = open('input.txt', 'r')
inputStr = inputFile.readlines()

calArray = []
calCounter = 0

#Task 1
for i in range(len(inputStr)):
	if inputStr[i] != '\n':
		calCounter += int(inputStr[i])
	else:
		calArray.append(calCounter)
		calCounter = 0

print(max(calArray))

#Task 2
for i in range(len(inputStr)):
	if inputStr[i] != '\n':
		calCounter += int(inputStr[i])
	else:
		calArray.append(calCounter)
		calCounter = 0

calCounter = 0 
calArray = sorted(calArray)
calCounter += int(calArray[-1]) + int(calArray[-2]) + int(calArray[-3])

print(calCounter)
