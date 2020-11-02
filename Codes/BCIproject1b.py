#part b of project-1
import numpy as np
import BCIproject1a as pa
from timeit import Timer
#indicates population size
ns = 10
#saves the individuals
population = []
#keeps the new population
new_population = []
#saves number of conflicts for each individual
conflicts = []
#indicates chromosome size
nx = 4
#indicates tournament size
nts = 3
#
#indicates index of first best individual of population
bestid = -1
#indicates index of second best individual of population
bestid2 = -1
#
new_generation = np.zeros((ns-2,nx),dtype=np.int)
#
next_generation = np.zeros((ns,nx),dtype=np.int)

numOfExecutions = 10
# =============================================================================
#the following function creates the first generation of population 
# =============================================================================
def firstGenerationProduction():
    population = np.random.randint(nx,size=(ns,nx))
    for i in range(ns):
        #we create random individuals
        population[i] = np.arange(nx)
        np.random.shuffle(population[i])
    return population

# =============================================================================
#the following function counts number of total conflicts of each individual
#(with a function in part a of project) and saves it in 'conflicts' array
# =============================================================================
def conflictComputer(population):
    conflicts = np.zeros((ns,), dtype=np.int)
    for i in range(ns):
      conflicts[i] = pa.conflictCounter(population[i],nx)   
    return conflicts

# =============================================================================
#we find an individual(chromosome) with least conflicts
# =============================================================================
def bestFinder( best,conflicts ) :
    for i in range(ns):
        if best>conflicts[i]:
            best = conflicts[i]
            k = i
            
    return k

# =============================================================================
#we find second best individual 
# =============================================================================
def secondBestFinder( best2,bestid,conflicts) :
     for i in range(ns):
         if i != bestid:
             if best2>conflicts[i]:
                 best2 = conflicts[i]
                 k = i
     return k
# =============================================================================
#this choose two individuals from population without considering their costs(conflicts) 
# =============================================================================
def sampler():
    lst =[]
    while(len(lst)<nts):
        a = np.random.randint(ns)
        if lst.count(a)==0:
            lst.append(a)
    return lst

# =============================================================================
#the following function is used for tournament selection method 
# =============================================================================
def tournament(population, conflicts):
    new_population = []
    for i in range (ns-2):
        lst = sampler()
        minIndex=-1
        if (conflicts[lst[0]] <= conflicts[lst[1]] and conflicts[lst[0]] <= conflicts[lst[2]] ) :
            minIndex=lst[0]
        if (conflicts[lst[1]] <= conflicts[lst[0]] and conflicts[lst[1]] <= conflicts[lst[2]] ) :
            minIndex=lst[1]
        else :
            minIndex=lst[2]
        new_population.append(population[minIndex])
    return new_population

# =============================================================================
#this method is a crossover operator for permutation codings
#pmx stands for partially mapped crossover 
# =============================================================================
def pmx(new_population):
    #cp : crossover probablity
    cp = np.random.uniform(0,1)
    new_generation = np.zeros((ns-2,nx),dtype=np.int)
    remained = np.zeros((ns-2,nx),dtype=np.int) -1
    print("crossover probablity:" , cp)
    if cp < 0.9:
        #e1 and e2 are two random points two make a two point crossover
        e1 = np.random.randint(1,nx)
        e2 = np.random.randint(1,nx)
        while abs(e2-e1)<2:
            e2 = np.random.randint(1,nx)
        if e1>e2 :
            e1,e2 = e2,e1
        print("e1:" , e1)
        print("e2:" , e2)
        i=0
        while i < (ns-3) :
            for j in range (e1 , e2):
                new_generation[i][j]=new_population[i+1][j]
                new_generation[i+1][j]=new_population[i][j]
                
                remained[i][new_population[i+1][j]] = new_population[i][j]
                remained[i+1][new_population[i][j]] = new_population[i+1][j]
            i += 2
        i=0
        while i < (ns-3) :
            for j in range (nx):
                if j<e1 or j>=e2:
                    p1=new_population[i][j]
                    p2=new_population[i+1][j]
                    r1=remained[i][p1]
                    r2=remained[i+1][p2]
                    
                    k=0
                    while r1!=-1 and k<nx:
                        p1=r1
                        r1=remained[i][r1]
                        k += 1
                    k=0
                    while r2!=-1 and k<nx: 
                        p2=r2
                        r2=remained[i+1][r2]
                        k += 1
                        
                    new_generation[i][j]=p1
                    new_generation[i+1][j]=p2
                
            i += 2
    else:
        for i in range (ns-2):
            for j in range (nx):
                new_generation[i][j]=new_population[i][j]
    return new_generation

# =============================================================================
#this function mutate each individual of new_generation with probability of mp
# =============================================================================
def mutation(new_generation):
    for i in range (ns-2):
        #mp : mutation probablity 
        mp = np.random.uniform(0,1)
        print("mutation probablity:" , mp)
        if mp < 0.1:
            index1=np.random.randint(nx)
            index2=np.random.randint(nx)
            print("index1:" , index1)
            print("index2:" , index2)
            new_generation[i][index1] , new_generation[i][index2] =new_generation[i][index2] , new_generation[i][index1]
    return new_generation

# =============================================================================
#this is the main function that runs genetic algorithm until number of conflicts => 0
# =============================================================================
def genetic():
    population = firstGenerationProduction()
    conflicts = conflictComputer(population)
    best = np.Infinity

    print("part 2 of project !!")
    print()
    print("~~primary population~~")
    for i in range(ns):
        print(population[i])
        #print(pa.conflictCounter(population[i],nx))
        #print(conflicts[i])
    #best == an individual with least conflicts (i.e best person in population)  
    bestid = bestFinder(best, conflicts)
    best = conflicts[bestid]
    next_generation = np.zeros((ns,nx),dtype=np.int)

    #while conflicts of best individual > 0
    if best>0:
        while best>0:
            #
            print()
            print("~~Tournament~~")
            new_population = tournament(population, conflicts)
            for i in range (ns-2):
                print(new_population[i])
            #
            print()
            print("~~PMX~~")
            new_generation = pmx(new_population)
            print(new_generation)
            #
            print()
            print("~~Mutation~~")
            new_generation = mutation(new_generation)
            print(new_generation)
            #
            print()
            print("~~Elitism~~")
            for i in range (ns-2):
                next_generation[i] = new_generation[i]
            print("bestid1:" ,bestid)
            next_generation[ns-2]=population[bestid]
            bestid2 = secondBestFinder(np.Infinity,bestid,conflicts)
            print("bestid2:" , bestid2)
            next_generation[ns-1]=population[bestid2]
            print(next_generation)
    
            conflicts = conflictComputer(next_generation)
            bestid = bestFinder(np.Infinity,conflicts)
            best = conflicts[bestid]
            print()
            print("~~best~~")
            print(next_generation[bestid])
            print(conflicts[bestid])
    else:
        print()
        print("~~best~~")
        print(population[bestid])
        print(conflicts[bestid])
    
# =============================================================================
#this function runs the genetic algorithm with different sizes of input
#(from n=1 to n=numOfExecutions)
# =============================================================================       
def genetic_timer():
        #for n=1,2,3 there isn't any feasible solution
        genetic_times =(0,0,0)
        for i in range(4,numOfExecutions+1):
            global nx
            nx = i
            #we use timeit to measure time of algorithm(it operates algorithm 200 times and then we divide the overall time by 200 to find average time)
            t = Timer( genetic)
            genetic_times = genetic_times + (np.sqrt(np.sqrt(t.timeit(number=1))) ,) 
        return genetic_times    
                       
if __name__=="__main__": 
    print(genetic_timer())