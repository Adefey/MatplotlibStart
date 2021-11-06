import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    plt.style.use('seaborn-whitegrid')

    fig = plt.figure(figsize=(10,6))

    ax = fig.add_subplot(projection='3d')

    x = np.arange(-5, 5, 0.5)
    y = np.sin(x)
    z = np.cos(x)

    ax.set_xticks(np.arange(-5,5,1))
    ax.set_yticks(np.arange(-1,1,0.5))
    ax.set_zticks(np.arange(-1,1,0.5))

    ax.plot(x, y, z, color='purple', linestyle=':', label='Sin(x)')

    ax.scatter(x, y, z, s=500, color='purple', linestyle=':', marker='*', label='Sin(x)', cmap='viridis')

    ax.grid(color = 'blue', alpha = 0.9)

    plt.show()

    #fig.savefig('./sin.png')

if __name__=="__main__":
    main()
