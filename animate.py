import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.tan(x))


def animate(i):
    line.set_ydata(np.tan(x + i / 20))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=10, blit=True, save_count=50)

plt.show()