import matplotlib
matplotlib.use('TkAgg')#to run using tkinter

import matplotlib.pyplot as plt
import numpy as np

def incrementIter(param):
    incrementIter.i += 1
    print()
    print(str(incrementIter.i) + ' -------- ' + str(param) + ' -------- ')


incrementIter.i = 0


#Bacis Example
incrementIter('Bacis Example')
x = np.linspace(0,5,11)
y = x ** 2
print(x)
print(y)
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
#plt.show()


#Multi-Plot
incrementIter('Multi-Plot')
plt.subplot(1,2,1)#1 row two column and plot number 1
plt.plot(x,y,'r')#x-axis,y-axis,color
plt.subplot(1,2,2)#1 row two column and plot number 2
plt.plot(y,x,'b')#x-axis,y-axis,color
#plt.show()

#Object Oriented
incrementIter('Object Oriented')
fig = plt.figure()
#adding axes, takes in list, left, bottom, width, height as percentage
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')
#plt.show()

#Object Oriented Multi-Plot
incrementIter('Object Oriented Multi-Plot')
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes2.plot(y,x,'r')
axes1.set_title('larger Plot')
axes2.set_title('Smaller Plot')
#plt.show()

#Object Oriented Sub-Plot
incrementIter('Object Oriented Sub-Plot')
fig,axes = plt.subplots(nrows = 1, ncols = 2)#axes is a array of axes objects
plt.tight_layout()
for current_ax in axes:
    current_ax.plot(x,y)
axes[1].plot(y,x,'r')
axes[0].set_title('First Plot')
axes[1].set_title('Second Plot')#allows multiple line
#plt.show()

#Figure Size & DPI
incrementIter('Figure Size & DPI')
#figsize -> width and height in inches, 
fig,axes = plt.subplots(nrows = 2, ncols = 1,figsize=(8,2), dpi=100)
axes[0].plot(x,y)
axes[1].plot(y,x,'r')
plt.tight_layout()
#plt.show()

#Save Figure
incrementIter('Save Figure')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x ** 2, label = 'X Squared')
ax.plot(x,x ** 3,'r', label = 'X Cubed')
ax.legend(loc = 0)#best location for the legend
fig.savefig('my_picture.png', dpi=300)
#plt.show()

#Appearance
incrementIter('Appearance')
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.9,0.9])
ax.plot(x,y, color='#FF8C00', linewidth=3, alpha=0.8, linestyle = '--', marker = '+', markersize = 20, markerfacecolor='yellow',
 markeredgewidth=2, markeredgecolor='green')
ax.set_xlim([0,1])#limit of the x-axis
ax.set_ylim([0,2])#limit of the y-axis
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Set Title')


#show all plots
plt.show()