import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # in this code it is not required

def cylinder (radius, height):
    ax = plt.axes(projection='3d') 
    z = np.linspace(0, height, 100)  
    theta = np.linspace(0, 2*np.pi, 100) 
    theta1, z1=np.meshgrid(theta, z)  
    x = radius * np.cos(theta1)
    y = radius * np.sin(theta1)        
    ax.contour3D(x, y, z1, 50)
    ax.set_title('Cylinder')
    plt.show()                  

if __name__ == '__main__':
    cylinder(1, 2)
    cylinder(2, 10)