import numpy
import math
import random

def popGen(popSize,genelength):
	# pop = []
	# for i in range(0,popSize):
	# 	member = numpy.random.randint(0,2,genelength)
	# 	pop.append(member)
	# return pop
	newPopulation = numpy.zeros( shape = (popSize,genelength))
	for i in range(0,popSize):
		newPopulation[i] = numpy.random.randint(0,2,genelength)
	return newPopulation
	#pop = numpy.zeros(popSize, dtype=float)
	#for member in pop:
	#	pop[member]=numpy.random.randint(0,2,5)

def eval(pop):
	evals = []
	for member in range(0,len(pop)):
		memVal=0
		fitness=0
		for i in range(0,len(pop[member])):
			if pop[member][len(pop[member])-i-1]>0:
				val = math.pow(2,i)
				memVal=memVal+val
				fitness=memVal
		evals.append(fitness)
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

def crossover(population,p1,p2,geneLength,mutationRate):
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
	for i in range(0,geneLength):
		r1=random.random()
		if r1<mutationRate:
			if c1[i]==0:
				c1[i]=1
			else:
				c1[i]=0
	for i in range(0,geneLength):
		r2=random.random()
		if r2<mutationRate:
			if c2[i]==0:
				c2[i]=1
			else:
				c2[i]=0

	return c1, c2

def mutation(child):

	return child

	

def process():
	popSize = 10
	geneLength = 5
	mutationRate = 0.1
	population = popGen(popSize,geneLength)
	for x in range(0,50):
		evals = eval(population)
		x = sum(evals)
		best = max(evals)
		if (x%5==0):
			print best
		newPopulation = numpy.zeros( shape = (popSize,geneLength))
		i=0
		while i<popSize:
			parent1,parent2 = selection(evals,population,popSize)
			child1,child2 = crossover(population,parent1[1],parent2[1],geneLength,mutationRate)
			newPopulation[i] = child1
			newPopulation[i+1] = child2
			i+=2
		population = newPopulation






if __name__ == "__main__":
    import numpy
    process()