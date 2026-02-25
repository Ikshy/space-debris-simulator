

from sgp4.api import Satrec, jday
import numpy as np
from datetime import datetime, timedelta
import csv

def tle_to_satellite_positions(tle_file, duration_hours=6, step_minutes=10):
    """
    Load TLE file and return satellite positions over time
    Safe parsing using csv module to avoid float conversion issues.
    """
    positions = {}
    times = [datetime.utcnow() + timedelta(minutes=i*step_minutes) for i in range(int(duration_hours*60/step_minutes))]

    # Read TLE file using csv module
    with open(tle_file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if len(row) < 3:
                continue  # skip invalid lines
            name = row[0].strip()
            line1 = row[1].strip()
            line2 = row[2].strip()

            # Create satellite object
            sat = Satrec.twoline2rv(line1, line2)

            # Compute positions over time
            pos_list = []
            for t in times:
                jd, fr = jday(t.year, t.month, t.day, t.hour, t.minute, t.second)
                e, r, v = sat.sgp4(jd, fr)
                if e == 0:
                    pos_list.append(r)  # km
                else:
                    pos_list.append([np.nan, np.nan, np.nan])
            positions[name] = np.array(pos_list)

    return positions, times