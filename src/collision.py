# collision.py
import numpy as np

def simple_collision_probability(pos1, pos2, threshold_km=10):
    """
    Very basic collision estimate:
    - pos1, pos2: arrays of positions over time
    - threshold_km: minimum distance considered a collision
    """
    collision_count = 0
    for p1, p2 in zip(pos1, pos2):
        distance = np.linalg.norm(p1 - p2)
        if distance < threshold_km:
            collision_count += 1
    return collision_count / len(pos1)