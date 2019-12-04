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

def lmPlot(tips):
    sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o','x'], palette='magma', scatter_kws={'s':50})
    plt.show()
    sns.lmplot(x='total_bill', y='tip', data=tips, col='day', row='time', hue='sex')
    plt.show()
    sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', aspect=0.8, size=8)
    plt.show()
    

def main():
    #Use Seaboarn built-in dataset and BDHousing dataset
    incrementIter('Use Seaboarn built-in dataset')
    iris = sns.load_dataset('iris')
    print(iris.head())
    tips = sns.load_dataset('tips')
    print(tips.head())

    #LM Plot
    incrementIter('LM Plot')
    lmPlot(tips)


if __name__ == "__main__":
    main()