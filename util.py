# Utility Functions
import numpy as np  # Import NumPy for numerical operations

# Get Angle
# Function to calculate the angle between three points
def get_angle(a, b, c):
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])  # Calculate the angle in radians
    angle = np.abs(np.degrees(radians))  # Convert radians to degrees and take the absolute value
    return angle  # Return the calculated angle

# ### Get Distance
# Function to calculate the distance between two landmarks
def get_distance(landmark_list):
    if len(landmark_list) < 2:  # Check if there are at least two landmarks
        return  # Return None if not enough landmarks

    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]  # Unpack the coordinates of the two landmarks
    L = np.hypot(x2 - x1, y2 - y1)  # Calculate the Euclidean distance
    return np.interp(L, [0, 1], [0, 1000])  # Normalize the distance to a range of 0 to 1000 and return it