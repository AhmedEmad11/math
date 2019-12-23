# Ahmed Emad Section 1
import numpy as np 
import matplotlib.pyplot as plt

n = int(input('enter the number of points of the given data set '))

x = np.ones( (n,2) )
for i in range(n):
    print('enter x of the point number %d'%(i+1))
    x[i][0] = float(input())

y = np.zeros( (n,1) )
for i in range(n):
    print('enter y of the point number %d'%(i+1))
    y[i] = float(input())
# the solution matrix that contains a and b
solution = np.linalg.inv(np.transpose(x).dot(x)).dot(np.transpose(x).dot(y))
# creating one dimension arrays for plotting 
x_plot = [x[0][0]]
y_plot = np.zeros( (n,1))
for i in range(1, n):
    x_plot.append(x[i][0])
for i in range(n):
    y_plot[i] = (solution[1]*x[i][0] + solution[0])

print("the least squre fit is given by the function y = {0} + {1}x".format(solution[1], solution[0]))
plt.plot(x_plot, y, 'r.',x_plot , y_plot)
plt.xlabel('x') 
plt.ylabel('y') 
plt.suptitle('Least Square Fit')
plt.show()
