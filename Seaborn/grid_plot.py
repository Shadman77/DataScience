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

def pairGrid(iris):
    g = sns.PairGrid(iris)
    g.map(plt.scatter)
    plt.show()
    g = sns.PairGrid(iris)
    g.map_diag(sns.distplot)
    g.map_upper(plt.scatter)
    g.map_lower(sns.kdeplot)
    plt.show()

def facetGrid(tips):
    g = sns.FacetGrid(data=tips, col='time', row='smoker')
    g.map(sns.distplot, 'total_bill')
    plt.show()
    g = sns.FacetGrid(data=tips, col='time', row='smoker')
    g.map(plt.scatter, 'total_bill', 'tip')
    plt.show()

def main():
    #Use Seaboarn built-in dataset and BDHousing dataset
    incrementIter('Use Seaboarn built-in dataset')
    iris = sns.load_dataset('iris')
    print(iris.head())
    tips = sns.load_dataset('tips')
    print(tips.head())

    #Pair Grid
    incrementIter('Pair Grid')
    #pairGrid(iris)

    #Facet Grid
    incrementIter('Facet Grid')
    facetGrid(tips)

if __name__ == "__main__":
    main()