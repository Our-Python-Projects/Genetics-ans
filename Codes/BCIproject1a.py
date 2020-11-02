#part a of project-1
import numpy as np
class chrom:
    def __init__(self, chrome, conflicts):
        self.chrome = chrome
        self.conflicts = conflicts
       

#indicates chromosome size
nx = 8
#the following function counts number of total conflicts of a given answer(coded in the chromosome 'x')
def conflictCounter(x,size): #x is a chromosome
    conflicts = 0
    for i in range(size):
        for j in range(size):
                if(i!=j):
                    #we check diagonal conflicts
                    if(abs(i-j)==abs(x[i]-x[j])):
                        conflicts = conflicts + 1
    return conflicts 
   
if __name__=="__main__":     
    ch = [1,1,3,0,6,4,2,5]
    ch = np.arange(nx)
    np.random.shuffle(ch)
    print("part1 of project")
    print(ch)
    print(conflictCounter(ch,nx))
    print("time cmplexity = O(nx^2)")
    print("space comlexity = O(nx)")