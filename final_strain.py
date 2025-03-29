import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load pre-formed and post-formed images
pre_image = cv2.imread("before.png", cv2.IMREAD_GRAYSCALE)
post_image = cv2.imread("after.png", cv2.IMREAD_GRAYSCALE)

# Resize post_image to match the dimensions of pre_image if they differ
if pre_image.shape != post_image.shape:
    post_image = cv2.resize(post_image, (pre_image.shape[1], pre_image.shape[0]))

# Compute the absolute difference between pre-formed and post-formed images
difference = cv2.absdiff(pre_image, post_image)

# Apply a threshold to highlight the areas with significant change (strain)
_, difference_thresh = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)

# Detect fiducial points (dots) using thresholding or feature detection on both pre and post images
_, pre_thresh = cv2.threshold(pre_image, 127, 255, cv2.THRESH_BINARY)
_, post_thresh = cv2.threshold(post_image, 127, 255, cv2.THRESH_BINARY)

# Find contours or points on the pre-formed and post-formed images
pre_contours, _ = cv2.findContours(pre_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
post_contours, _ = cv2.findContours(post_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assuming fiducial points are detected and we are interested in the centroid of each contour
pre_points = [np.mean(c, axis=0).flatten() for c in pre_contours]
post_points = [np.mean(c, axis=0).flatten() for c in post_contours]

# Create a colored image to show the difference and marked points
colored_post_image = cv2.cvtColor(post_image, cv2.COLOR_GRAY2BGR)

# Mark only the points that show the changes (displacement) in the post-formed image
for pre_point, post_point in zip(pre_points, post_points):
    displacement_x = post_point[0] - pre_point[0]
    displacement_y = post_point[1] - pre_point[1]
    
    # Only mark points that have moved (threshold displacement to avoid marking small changes)
    if abs(displacement_x) > 0.5 or abs(displacement_y) > 0.5:  # Threshold for movement
        cv2.circle(colored_post_image, tuple(post_point.astype(int)), 5, (0, 0, 255), -1)  # Red for changes

# Visualize the difference and marked post-formed image
plt.figure(figsize=(12, 8))

# Plot the difference image (highlighting the changes)
plt.subplot(2, 2, 1)
plt.imshow(difference_thresh, cmap='gray')
plt.title("Difference Image (Changes Highlighted)")

# Plot the post-formed image with marked changes
plt.subplot(2, 2, 2)
plt.imshow(colored_post_image)
plt.title("Post-formed Image with Changes Marked")

# Plot the pre-formed image
plt.subplot(2, 2, 3)
plt.imshow(pre_image, cmap='gray')
plt.title("Pre-formed Image")

# Plot the post-formed image
plt.subplot(2, 2, 4)
plt.imshow(post_image, cmap='gray')
plt.title("Post-formed Image")

plt.tight_layout()
plt.show()
