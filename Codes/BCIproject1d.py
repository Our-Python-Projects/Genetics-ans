#part d of project-1
import numpy as np
import timeit
n = 12
numOfExecutions = 10
# the following function initializes answer data structure and then gets the anser from another function
def analyticalAnswer():
    ans = np.zeros((n,), dtype=np.int)
    ans = analyticalConstructor(ans,n)
    return ans
# the following function set the queens in the chess board according to the analytical algorithm(which is mentioned in the slide and ook)
def analyticalConstructor(ans, n):
    if n<3:
        return ans
    if n%2 is 1:
        ans[n-1] = n-1
        analyticalConstructor(ans,n-1)
    elif n%6 != 0:
        for i in range(int(n/2)):
            ans[i] = (int(n/2)+2*i-1)%n
        for i in range(int(n/2),n):
            ans[i] = (int(n/2)+2*i+2)%n
    else:
        for i in range(int(n/2)):
            ans[i] = (2*i+1)
        for i in range(int(n/2),n):
            ans[i] = (2*i)%n
    return ans
#this function runs the analytical algorithm with different sizes of input(from n=1 to n=numOfExecutions)
def analytic_timer():
        analytic_times =(0,0,0)
        for i in range(4,numOfExecutions+1):
            global n
            n = i
            #we use timeit to measure time of algorithm(it operates algorithm 200 times and then we divide the overall time by 200 to find average time)
            analytic_times =  analytic_times + (np.sqrt(np.sqrt(np.sqrt(timeit.timeit(analyticalAnswer, number=200)/200))),) 
        return analytic_times    
        
if __name__=="__main__": 
    print(analytic_timer())