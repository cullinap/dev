import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(0,10,0.5)
y = range(10)

fig = plt.figure()
ax = plt.axes(xlim = (-1,1), ylim=(-1,15))
line, = ax.plot([], [], lw=2)

def initFn():
    line.set_data([], [])
    return line,

def animateFn(i):
    x = xVal[i]
    y = yVal[i]
    line.set_data(x,y)
    return line,

animate_object = FuncAnimation(fig,
                               animateFn,
                               init_func=initFn,
                               frames=100,
                               interval=30,
                               blit=True
                )

plt.show()


