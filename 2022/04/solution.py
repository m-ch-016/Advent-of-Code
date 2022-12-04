import re, time, hashlib

inputFile = open('input.txt', 'r')
inputStr = inputFile.readlines()

count = 0

#Task 1
for pairs in inputStr:
	
	firstElf, secondElf = pairs.split(",")
	firstElfLower, firstElfUpper = map(int, firstElf.split("-"))
	secondElfLower, secondElfUpper = map(int, secondElf.split("-"))
	firstElfSet = set(range(firstElfLower, firstElfUpper+1))
	secondElfSet = set(range(secondElfLower, secondElfUpper+1))

	if firstElfSet.issubset(secondElfSet) or secondElfSet.issubset(firstElfSet):
		count += 1

#Task 2 
for pairs in inputStr:
	
	firstElf, secondElf = pairs.split(",")
	firstElfLower, firstElfUpper = map(int, firstElf.split("-"))
	secondElfLower, secondElfUpper = map(int, secondElf.split("-"))
	firstElfSet = set(range(firstElfLower, firstElfUpper+1))
	secondElfSet = set(range(secondElfLower, secondElfUpper+1))

	overlapSet = firstElfSet.intersection(secondElfSet)

	if len(overlapSet) != 0:
		count += 1

print(count)
