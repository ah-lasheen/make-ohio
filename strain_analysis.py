import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load pre-formed and post-formed images
pre_image = cv2.imread("before.png", cv2.IMREAD_GRAYSCALE)
post_image = cv2.imread("after.png", cv2.IMREAD_GRAYSCALE)

# Detect fiducial points (dots) using simple thresholding or feature detection
_, pre_thresh = cv2.threshold(pre_image, 127, 255, cv2.THRESH_BINARY)
_, post_thresh = cv2.threshold(post_image, 127, 255, cv2.THRESH_BINARY)

# Find contours or points on the pre-formed and post-formed images
pre_contours, _ = cv2.findContours(pre_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
post_contours, _ = cv2.findContours(post_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assuming fiducial points are detected and we are interested in the centroid of each contour
pre_points = [np.mean(c, axis=0).flatten() for c in pre_contours]
post_points = [np.mean(c, axis=0).flatten() for c in post_contours]

# Calculate displacement (change in position) for each fiducial point
displacements = []
for pre_point, post_point in zip(pre_points, post_points):
    displacement_x = post_point[0] - pre_point[0]  # Change in X
    displacement_y = post_point[1] - pre_point[1]  # Change in Y
    displacements.append((displacement_x, displacement_y))

# Calculate strain for each fiducial point
strain_values = []
for displacement_x, displacement_y in displacements:
    strain_x = displacement_x / pre_points[0][0]  # Using initial position for strain calculation
    strain_y = displacement_y / pre_points[0][1]
    strain_values.append((strain_x, strain_y))

# Print the strain values
for idx, (strain_x, strain_y) in enumerate(strain_values):
    print(f"Fiducial point {idx}: Strain X = {strain_x:.4f}, Strain Y = {strain_y:.4f}")

# Optional: visualize the displacement (for debugging/visualization purposes)
for pre_point, post_point in zip(pre_points, post_points):
    cv2.circle(pre_image, tuple(pre_point.astype(int)), 5, (0, 0, 255), -1)  # Red circle for pre-formed points
    cv2.circle(post_image, tuple(post_point.astype(int)), 5, (0, 255, 0), -1)  # Green circle for post-formed points

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(pre_image, cmap='gray')
plt.title("Pre-formed Image")

plt.subplot(1, 2, 2)
plt.imshow(post_image, cmap='gray')
plt.title("Post-formed Image")

plt.show()
