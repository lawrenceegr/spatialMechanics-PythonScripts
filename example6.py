import numpy as np

# Coordinates of point Q with respect to the base reference frame
Q_base = np.array([4, 2*np.sqrt(3), 5])

# Angle of rotation in degrees
theta_deg = 60

# Convert angle to radians
theta_rad = np.deg2rad(theta_deg)

# Rotation matrix about the x-axis
R_x = np.array([[1, 0, 0],
                [0, np.cos(theta_rad), -np.sin(theta_rad)],
                [0, np.sin(theta_rad), np.cos(theta_rad)]])

# Calculate new coordinates after rotation
Q_rotated = np.dot(R_x, Q_base)

print("Coordinates of point Q with respect to the rotated frame:", Q_rotated)
