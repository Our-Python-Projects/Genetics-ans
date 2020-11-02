#part f of project-1(time)
import BCIproject1d as pd
import BCIproject1c as pc
import BCIproject1e as pe
import BCIproject1b as pb
numOfExecutions = 10

if __name__=="__main__": 
    # first we measure running time of each algorithm
    analytical_times = pd.analytic_timer()
    backtracking_times = pc.backtrack_timer()
    genetic_times = pb.genetic_timer()
    #we output our timings
    print('Analytical algorithm times in a tuple : {}'.format(analytical_times))
    print()
    print('Backtracking algorithm times in a tuple : {}'.format(backtracking_times))
    print()
    print('Genetic algorithm times in a tuple : {}'.format(genetic_times))
    #in the following, we use 'plotter' function(from another python code) to sketch the bar chart   
    pe.plotter(numOfExecutions,backtracking_times,"Backtrack",analytical_times,"Analytical",genetic_times,"Genetic")