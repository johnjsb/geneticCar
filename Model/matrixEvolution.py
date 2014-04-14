"""
Genetic Matrix evolution

@author: Paul Titchener

@teamName: Track Bot Driver (TBD)
"""

import random 
import copy

def formMatrix(x,y):
	"""Forms a random matrix of size x,y. The output is a nested list 
	in with the outer list being the x coordinate and the inner lists being the y coordinate"""
	L =[]
	for i in range(x):
		Lint = []
		for j in range(y):
			Lint.append(random.random())
		L.append(Lint)

	return L

def mixMatrix(M1,M2):
	"""Checks if two matricies are of equal size and then mixes them randomly."""
	if len(M1) != len(M2): #checks if the x coordinates are equal
		raise Exception("Matricies must be equal size")

	for i in range(len(M1)-1): #checks if the y coordinates are equal
		if len(M1[i]) != len(M2[i]):
			raise Exception("Matricies must be equal size")
	MOut = []
	for i in range(len(M1)): #iterates through x coordinates to mix
		Lint = []
		for j in range(len(M1[0])): #iterates through y coordinates
			mutationType = random.random() #randomly decides if it will use the value from M1, M2, or average them randint is not used so the probability distribution can be changed
			if mutationType<1.0/3:
				Lint.append(M1[i][j])
			elif mutationType <2.0/3:
				Lint.append(M2[i][j])
			else:
				Lint.append((M2[i][j] + M1[i][j])/2)
		MOut.append(Lint)
	return MOut

def mutateMatrix(M,r,rangeMutate):
	"""Takes a matrix that has been mixed and then randomly changes values to simulate mutation
	Three types of mutation:
	1) Switch Values: Switches two values in the matrix
	2) Change value within a range: Adds or subtracts a random, small value to the parameter
	3) Completely change value

	Inputs:
	M: Matrix to mutate
	r: mutation rate. Within the mutation rate, the different mutations will happen equally probably
	rangeMutate: the range in which mutation type 2 will occur in
	"""
	MOut = copy.deepcopy(M)
	for i in range(len(M)):
		for j in range(len(M[i])):
			mutate = random.random()
			if mutate < (1-r):
				pass
			elif mutate < (1-r) + (r/3.0): #switch values with a randomly determined other member of the matrix
				switchIndexX = random.randint(0,len(M)-1)
				switchIndexY = random.randint(0,len(M[switchIndexX]) -1)
				MOut[i][j] = M[switchIndexX][switchIndexY]  
				MOut[switchIndexX][switchIndexY] = M[i][j]
				#print "switch"
			elif mutate < (1-r) + (2*r/3.0): #Change value within a range
				diff = random.random()*rangeMutate
				MOut[i][j] = M[i][j] + (diff - diff/2.0) #uses a symetrical range
				if MOut[i][j] >1: #clips MOut at 1
					MOut[i][j] = 1 
				#print "range"
			else:
				MOut[i][j] = random.random()
				#print "random"
	return MOut

def matrixScale(M,S):
	"""Takes a matrix with values from zero to 1 and returns a matrix with values centered around zero scaled by value S"""
	Mout = []
	for i in range(len(M)):
		Mout.append([])
		for j in range(len(M[i])):
			Mout[i].append((M[i][j] -.5)*S)

	return Mout

if __name__ == '__main__':
	a= formMatrix(4,2)
	b = formMatrix(4,2)
	M = mixMatrix(a,b)
	print M
	print mutateMatrix(M,.2,.2)
	print matrixScale(M,20)
