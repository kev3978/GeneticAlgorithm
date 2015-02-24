import numpy
import math

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

def crossover(evals,pop):
	



def process():
	population = popGen(3,5)
	print len(population)
	print population[0]
	print population[1]
	print population[2]
	evals = eval(population)
	


if __name__ == "__main__":
    import numpy
    process()