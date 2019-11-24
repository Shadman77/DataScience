import matplotlib
matplotlib.use('TkAgg')#to run using tkinter

import matplotlib.pyplot as plt
import seaborn as sns

def incrementIter(param):
    incrementIter.i += 1
    print()
    print(str(incrementIter.i) + ' -------- ' + str(param) + ' -------- ')


incrementIter.i = 0

#dist plot function
def distPlot():
    sns.distplot(tips['total_bill']).set_title('With kernel density plot') #single column distribution plot
    plt.show()
    sns.distplot(tips['total_bill'], kde=False, bins=200).set_title('Without kernel density plot') #single column distribution plot without kernel density plot
    #bins is kinda like the divition in which the value falls, best option is automatically set by sns
    plt.show()

def jointPlot():
    from scipy import stats
    sns.jointplot(x='total_bill',y='tip', data=tips)
    plt.show()
    sns.jointplot(x='total_bill',y='tip', data=tips, kind='hex')
    plt.show()
    sns.jointplot(x='total_bill',y='tip', data=tips, kind='reg').annotate(stats.pearsonr)
    plt.show()


#Use Seaboarn built-in dataset
incrementIter('Use Seaboarn built-in dataset')
tips = sns.load_dataset('tips')
print(tips.head())

#Dist Plot
incrementIter('Dist Plot')
#distPlot()


#Joint Plot
incrementIter('Joint Plot')
jointPlot()