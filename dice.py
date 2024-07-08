import numbers
from random import randint
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
j = 0
k = 0
l = 0

fig = plt.figure(tight_layout=True)
ax = fig.add_subplot(2, 2, 1) # using a different approach to arrange plots

arr = np.array([[0,0]])
for i in range(100):
    first_dice = randint(1,6)
    second_dice = randint(1,6)
    add = first_dice + second_dice
    arr = np.append(arr, [[i+1, add]], axis = 0)

arr = np.delete(arr, 0,0)

x, y = arr.T
ax.scatter(x, y, s=1.5, color='lightgreen')
ax.set_title("Scatter")
ax.set_xlabel('trial')
ax.set_ylabel('sum')

ax = fig.add_subplot(2, 2, 2)
plt.plot(x,y, color='palevioletred')
ax.set_title("Line")
ax.set_xlabel('trial')
ax.set_ylabel('sum')

ax = fig.add_subplot(2, 2, 3)
plt.hist(y, color = 'thistle')
plt.xticks(range(2,13))
ax.set_title("Histogram")
ax.set_xlabel('sum')
ax.set_ylabel('amount of times')

ax = fig.add_subplot(2, 2, 4)

for i in np.nditer(y):
        if i == 2:
            a = a +1
        elif i == 3:
            b = b + 1
        elif i == 4:
            c = c + 1
        elif i == 5:
            d = d + 1
        elif i == 6:
            e = e + 1
        elif i == 7:
            f = f + 1
        elif i == 8:
            g = g +1
        elif i == 9:
            h = h +1
        elif i == 10:
            j = j+1
        elif i == 11:
            k = k + 1
        elif i == 12:
            l = l +1

arr1 = np.array([])
arr1 = np.append(arr1, a)
arr1 = np.append(arr1, b)
arr1 = np.append(arr1, c)
arr1 = np.append(arr1, d)
arr1 = np.append(arr1, e)
arr1 = np.append(arr1, f)
arr1 = np.append(arr1, g)
arr1 = np.append(arr1, h)
arr1 = np.append(arr1, j)
arr1 = np.append(arr1, k)
arr1 = np.append(arr1, l)


numbers_for_pie = ['2', '3' , '4' , '5', '6', '7', '8', '9', '10' , '11', '12']
ax.set_title("Pie Plot")
ax.pie(arr1, labels = numbers_for_pie, autopct='%1.0f%%')
plt.show()