import matplotlib
matplotlib.use('TkAgg')#to run using tkinter

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def incrementIter(param):
    incrementIter.i += 1
    print()
    print(str(incrementIter.i) + ' -------- ' + str(param) + ' -------- ')

incrementIter.i = 0

def barPlot(tips):
    sns.barplot(x='sex',y='total_bill',data=tips)
    plt.show()
    sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)
    plt.show()

def countPlot(tips):
    sns.countplot(x='sex', data = tips)
    plt.show()

def boxPlot(tips):
    sns.boxplot(x='day',y='total_bill',data=tips)
    plt.show()
    sns.boxplot(x='day',y='total_bill',data=tips, hue='smoker')
    plt.show()

def violinPlot(tips):
    sns.violinplot(x='day', y='total_bill', data=tips)
    plt.show()
    sns.violinplot(x='day', y='total_bill', data=tips, hue='sex')
    plt.show()
    sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker', split=True)
    plt.show()

def stripPlot(tips):
    sns.stripplot(x='day', y='total_bill', data=tips, jitter=False)
    plt.show()
    sns.stripplot(x='day', y='total_bill', data=tips)
    plt.show()
    sns.stripplot(x='day', y='total_bill', data=tips, hue='sex', dodge=True)
    plt.show()

def swarmPlot(tips):
    sns.swarmplot(x='day', y='total_bill', data=tips)
    plt.show()
    sns.violinplot(x='day', y='total_bill', data=tips)
    sns.swarmplot(x='day', y='total_bill', data=tips, color='black')
    plt.show()


def factorPlot(tips):
    sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')
    plt.show()
    sns.factorplot(x='day', y='total_bill', data=tips, kind='box')
    plt.show()


def main():
    #Use Seaboarn built-in dataset and BDHousing dataset
    incrementIter('Use Seaboarn built-in dataset')
    tips = sns.load_dataset('tips')
    print(tips.head())

    #Barplot
    incrementIter('Barplot')
    #barPlot(tips)

    #Count Plot
    incrementIter('Count Plot')
    #countPlot(tips)

    #Box Plot
    # Recommended for presentation since easier to understand for executives
    incrementIter('Box Plot')
    #boxPlot(tips)

    #Violin Plot
    incrementIter('Violin Plot')
    #violinPlot(tips)

    #Strip Plot
    incrementIter('Strip Plot')
    #stripPlot(tips)

    #Swarm Plot
    incrementIter('Swarm Plot')
    #swarmPlot(tips)

    #Factor Plot
    incrementIter('Factor Plot')
    factorPlot(tips)

if __name__ == "__main__":
    main()