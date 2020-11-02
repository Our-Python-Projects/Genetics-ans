#part e of project-1(time)
import numpy as np
import matplotlib.pyplot as plt


#the following function plots a bar chart according to its inputs
#inputs are : n(number of bars) and a, b, c are the three types of algorithms datas... 
def plotter(n,a,a_label,b,b_label,c,c_label):

   
    index = np.arange(n)
    bar_width = 0.1
    opacity = 0.81
    rects1 = plt.bar(index, a, bar_width,
                 alpha=opacity,
                 color='b',
                 label=a_label)
 
    rects2 = plt.bar(index + 1*bar_width, b, bar_width,
                 alpha=opacity,
                 color='g',
                 label=b_label)
    rects3 = plt.bar(index + 2*bar_width, c, bar_width,
                 alpha=opacity,
                 color='r',
                 label=c_label)
   
    
    plt.xlabel('N(size of input)')
    plt.ylabel('Time(s)')
    plt.title('Time by size of input')
    plt.xticks(index + bar_width, np.arange(n)+1)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__=="__main__": 
  plotter(4,(-12,2,3,4),'a',(-12222.545,3,2,1),'b',(1,123,87,1),'c')
  print(type((1,2,3,4)))