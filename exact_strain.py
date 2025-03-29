import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the "before" and "after" images
before_image = cv2.imread("pre.jpg", cv2.IMREAD_GRAYSCALE)
after_image = cv2.imread("post.jpg", cv2.IMREAD_GRAYSCALE)

# Check if images loaded correctly
if before_image is None or after_image is None:
    print("Error: Could not load one of the images.")
else:
    # Use optical flow to track the displacement between images
    # We use Farneback method for dense optical flow
    flow = cv2.calcOpticalFlowFarneback(before_image, after_image, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Calculate displacement (magnitude of flow)
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    # You can also calculate strain by approximating the deformation per region
    strain = magnitude / np.max(magnitude)

    # Plot the displacement magnitude (representing strain)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(before_image, cmap="gray")
    plt.title("Before Forming")

    plt.subplot(1, 2, 2)
    plt.imshow(strain, cmap="hot")
    plt.title("Strain (Deformation)")

    plt.show()
