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

def heatMap(tc, fp):
    sns.heatmap(tc)
    plt.show()
    sns.heatmap(tc, annot=True, cmap='coolwarm')
    plt.show()
    sns.heatmap(fp, cmap='magma', linecolor='white', linewidth=1)
    plt.show()

def clusterMap(tc, fp):
    #Re-sorts both axes to group by similarity, shows heirechical clusters
    sns.clustermap(fp, cmap='coolwarm')
    plt.show()
    sns.clustermap(fp, cmap='coolwarm', standard_scale=1)#Normalizing
    plt.show()


def main():
    #Use Seaboarn built-in dataset and BDHousing dataset
    incrementIter('Use Seaboarn built-in dataset')
    tips = sns.load_dataset('tips')
    print(tips.head())
    flights = sns.load_dataset('flights')
    print(flights.head())

    #Creating a correlation table of tips so that both axes contains variables i.e. labels
    incrementIter('Creating a correlation table of tips so that both axes contains variables i.e. labels')
    tc = tips.corr()
    print(tc)
    fp = flights.pivot_table(index='month',columns='year',values='passengers')
    print(fp)

    #Heat Map
    incrementIter('Heat Map')
    #heatMap(tc, fp)

    #Cluster Map
    incrementIter('Cluster Map')
    clusterMap(tc, fp)


if __name__ == "__main__":
    main()