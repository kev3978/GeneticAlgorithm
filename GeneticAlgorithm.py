import numpy
import math
import random

def popGen(popSize,genelength):
	pop = []
	for i in range(0,popSize):
		member = numpy.random.randint(0,2,genelength)
		pop.append(member)
	return pop
	#pop = numpy.zeros(popSize, dtype=float)
	#for member in pop:
	#	pop[member]=numpy.random.randint(0,2,5)

def eval(pop):
	evals = []
	for member in range(0,len(pop)):
		memVal=0
		for i in range(0,len(pop[member])):
			if pop[member][len(pop[member])-i-1]>0:
				val = math.pow(2,i)
				memVal=memVal+val
		evals.append(memVal)
	return evals


def roulette(probs,popSize):
	r=random.random()
	count=0
	tot=0
	for i in range(0,len(probs)):
		tot=tot+probs[i]
		if tot>r:
			return i





def selection(evals,pop,popSize):
	x = sum(evals)
	mean = x/len(evals)
	probs = []
	for each in evals:
		probs.append(each/x)
	parent1 = []
	parent2 = []
	for i in range(0,popSize):
		parent1.append(roulette(probs,popSize))
		parent2.append(roulette(probs,popSize))
	return parent1, parent2

def crossover(population,p1,p2,geneLength):
	crosspoint = numpy.random.randint(1,geneLength,1)
	crosspoint = crosspoint[0]
	p1 = population[p1]
	p2 = population[p2]
	c1 = numpy.zeros(geneLength)
	c2 = numpy.zeros(geneLength)
	for i in range(0,geneLength):
		if i<crosspoint:
			c1[i]=(p1[i])
			c2[i]=(p2[i])
		else:
			c1[i] =(p2[i])
			c2[i] =(p1[i])
	c1.astype(int)
	return c1, c2

	

def process():
	popSize = 10
	geneLength = 5
	mutationRate = 0.1
	population = popGen(popSize,geneLength) 
	print len(population)
	print population[0]
	print population[1]
	print population[2]
	evals = eval(population)
	parent1,parent2 = selection(evals,population,popSize)
	newPopulation = numpy.zeros
	#for i in range(0,popSize):
	child1,child2 = crossover(population,parent1[1],parent2[1],geneLength)


if __name__ == "__main__":
    import numpy
    process()