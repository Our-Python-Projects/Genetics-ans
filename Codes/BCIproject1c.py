#part c of project-1
import numpy as np
import timeit
n = 8
numOfExecutions = 10
#this function checks that it is possible to set the k-th queen in the board(according to our previous decisions)
def isSafe(x,k):
    for i in range(k):
        if(x[i]==x[k] or abs(x[i]-x[k])==abs(i-k)):
            return False
    return True    
#this function is the main part of backtracking 
# places queens on the chess board(if possible) and then does it for next queen until a solution is obtained
def backtrackNQeen(n,x,i):
        if(i==n):
            #we finish the algorithm when one answer is found
            #print(x)
            #print(pa.conflictCounter(x,n))
            return x
        else:
            #try all of possible choices
            for j in range(0,n):
                x[i] = j
                if(isSafe(x,i)):
                 return backtrackNQeen(n,x,i+1)
#the following function initializes answer data structure and starts backtracking                
def launchBacktrack():
       x = np.zeros((n,), dtype=np.int)
       backtrackNQeen(n,x,0)
       
#this function runs the backtracking algorithm with different sizes of input(from n=1 to n=numOfExecutions)       
def backtrack_timer():
        #for n=1,2,3 there isn't any feasible solution
        backtrack_times =(0,0,0)
        for i in range(4,numOfExecutions+1):
            global n
            n = i
            #print(n)
            #we use timeit to measure time of algorithm(it operates algorithm 200 times and then we divide the overall time by 200 to find average time)
            backtrack_times = backtrack_times + (np.sqrt(np.sqrt(np.sqrt(timeit.timeit(launchBacktrack, number=200)/200))),) 
        return backtrack_times    
                
if __name__=="__main__": 
   
   print(backtrack_timer())
   