import matplotlib
matplotlib.use('TkAgg')#to run using tkinter

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def incrementIter(param):
    incrementIter.i += 1
    print()
    print(str(incrementIter.i) + ' -------- ' + str(param) + ' -------- ')


incrementIter.i = 0

#dist plot function
def distPlot(tips):
    #apartments = apartments.dropna(subset=['Price'])
    sns.distplot(tips['tip']).set_title('With kernel density plot') #single column distribution plot
    plt.show()
    sns.distplot(tips['tip'], kde=False, bins=200).set_title('Without kernel density plot') #single column distribution plot without kernel density plot
    #bins is kinda like the divition in which the value falls, best option is automatically set by sns
    plt.show()
    sns.rugplot(tips['total_bill'])
    plt.show()
    sns.kdeplot(tips['total_bill'])
    plt.show()

def jointPlot(tips):
    from scipy import stats
    #apartments = apartments.dropna(subset=['Price', 'Size'])
    sns.jointplot(x='total_bill',y='tip', data=tips)
    plt.show()
    sns.jointplot(x='total_bill',y='tip', data=tips, kind='hex')
    plt.show()
    sns.jointplot(x='total_bill',y='tip', data=tips, kind='reg').annotate(stats.pearsonr)
    plt.show()
    sns.jointplot(x='total_bill',y='tip', data=tips, kind='kde')
    plt.show()

def pairPlot(tips):
    sns.pairplot(tips)
    plt.show()
    sns.pairplot(tips, hue='sex')
    plt.show()
    sns.pairplot(tips, hue='sex', palette='coolwarm')
    plt.show()

def main():
    #Use Seaboarn built-in dataset and BDHousing dataset
    incrementIter('Use Seaboarn built-in dataset')
    tips = sns.load_dataset('tips')
    #apartments = pd.read_csv("../data/formattedData.csv") 
    #print(apartments['Price'][apartments['Price'].isnull()])
    #apartments['Price'] = pd.to_numeric(apartments['Price'], errors='coerce')#to change non numerical values to numerical values
    #apartments = apartments.dropna(subset=['Price'])
    #apartments['Price'] = apartments['Price'].fillna(value = 0)
    print(tips.head())
    #print(apartments.head())
    #for col in apartments.columns: 
    #    print(col)

    #Dist Plot
    incrementIter('Dist Plot')
    distPlot(tips)


    #Joint Plot
    incrementIter('Joint Plot')
    #jointPlot(tips)

    #Pair Plot
    incrementIter('Pair Plot')
    #pairPlot(tips)

if __name__ == "__main__":
    main()