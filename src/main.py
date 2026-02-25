# main.py
from orbit_simulator import tle_to_satellite_positions
from visualizer import plot_orbits
from collision import simple_collision_probability

# Load positions from TLE
positions, times = tle_to_satellite_positions('data/tle_sample.txt')

# Plot satellite orbits
plot_orbits(positions, times)

# Calculate collision probability between first two satellites
names = list(positions.keys())
if len(names) >= 2:
    prob = simple_collision_probability(positions[names[0]], positions[names[1]])
    print(f"Estimated collision probability between {names[0]} and {names[1]}: {prob*100:.2f}%")