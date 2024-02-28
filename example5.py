import numpy as np

theta = np.pi / 3  # 60 degrees in radians
R = np.array([[np.cos(theta), 0, -np.sin(theta)],
              [0, 1, 0],
              [np.sin(theta), 0, np.cos(theta)]])

p_oxyz = np.array([2, 3, 6])
q_oxyz = np.array([4, 2, 5])

p_oabc = np.dot(R, p_oxyz)
q_oabc = np.dot(R, q_oxyz)

print("Coordinates of p in OABC frame:", p_oabc)
print("Coordinates of q in OABC frame:", q_oabc)
