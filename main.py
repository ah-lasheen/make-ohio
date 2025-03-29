import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read your before and after forming images (use your image paths)
before_image = cv2.imread("pre.jpg", cv2.IMREAD_GRAYSCALE)
after_image = cv2.imread("post.jpg", cv2.IMREAD_GRAYSCALE)

# Check if images loaded correctly
if before_image is None or after_image is None:
    print("Error: Could not load one of the images.")
else:
    # Pre-process the images (you can tweak the operations as needed)
    before_image = cv2.GaussianBlur(before_image, (5, 5), 0)
    after_image = cv2.GaussianBlur(after_image, (5, 5), 0)

    # Calculate the difference between the images (strain analysis concept)
    strain_image = cv2.absdiff(before_image, after_image)

    # Display the results
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(before_image, cmap="gray")
    plt.title("Before Forming")

    plt.subplot(1, 3, 2)
    plt.imshow(after_image, cmap="gray")
    plt.title("After Forming")

    plt.subplot(1, 3, 3)
    plt.imshow(strain_image, cmap="hot")
    plt.title("Strain (Difference)")

    plt.show()
