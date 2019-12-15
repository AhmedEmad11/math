#Ahmed Emad Section 1
import numpy as np 
import matplotlib.pyplot as plt
n = int(input('enter the number of points of the given data set '))
x = np.ones( (n,2) )
for i in range(n):
    print('enter x  NO. {0}', (i+1))
    x[i][0] = float(input())
print(np.transpose(x).dot(x))
y = np.zeros( (n,1) )
for i in range(n):
    print('enter y {0}', (i+1))
    y[i] = float(input())
variables = np.linalg.inv(np.transpose(x).dot(x)).dot(np.transpose(x).dot(y))
print(variables)
x_plot = [x[0][0]]
y_plot = np.zeros( (n,1))
for i in range(1, n):
    x_plot.append(x[i][0])
for i in range(n):
    y_plot[i] = (variables[0]*x[i][0] + variables[1])
plt.plot(x_plot, y, 'r.',x_plot , y_plot)
plt.show()