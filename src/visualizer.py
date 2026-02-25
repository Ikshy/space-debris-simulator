# visualizer.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_orbits(positions_dict, times):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Earth as sphere
    u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
    R = 6371  # km
    x = R*np.cos(u)*np.sin(v)
    y = R*np.sin(u)*np.sin(v)
    z = R*np.cos(v)
    ax.plot_surface(x, y, z, color='b', alpha=0.3)

    for name, pos in positions_dict.items():
        pos = np.array(pos)
        ax.plot(pos[:,0], pos[:,1], pos[:,2], label=name)

    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title('Satellite Orbits & Earth')
    plt.legend()
    plt.show()