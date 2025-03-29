import numpy as np
import matplotlib.pyplot as plt

# Provided strain data for each fiducial point (Strain X, Strain Y)
strain_x = [
    0.1209, -0.4305, -0.0043, 0.0021, 0.0035, 0.0319, 0.0298, 0.1921, -0.0793, 0.0222,
    0.0091, 0.0650, -0.0759, 0.0363, -0.0416, -0.1790, 0.4277, -0.0075, 0.0069, 0.5626,
    -0.6185, -0.0185, -0.0290, -0.5955
]

strain_y = [
    -0.2288, -0.2119, -0.1949, -0.1907, -0.1497, -0.1520, -0.2347, 0.0139, -0.0889, -0.1819,
    -0.2664, -0.2168, -0.2169, -0.1703, -0.2211, -0.0848, -0.0878, -0.2059, -0.2036, -0.2173,
    -0.2235, -0.2056, -0.2054, -0.2171
]

# Calculate the total strain using Pythagorean theorem (sqrt(Strain_X^2 + Strain_Y^2))
total_strain = np.sqrt(np.array(strain_x)**2 + np.array(strain_y)**2)

# Reshape the strain values into a 2D grid (4x6 in this case)
total_strain_2d = total_strain.reshape((4, 6))

# Plot the total strain with a color map
plt.imshow(total_strain_2d, cmap='viridis', interpolation='nearest')
plt.colorbar(label="Total Strain")
plt.title("Total Strain Distribution")
plt.show()

# Optionally, you can plot Strain X and Strain Y as well
# Plot Strain X distribution
plt.imshow(np.array(strain_x).reshape((4, 6)), cmap='coolwarm', interpolation='nearest')
plt.colorbar(label="Strain X")
plt.title("Strain X Distribution")
plt.show()

# Plot Strain Y distribution
plt.imshow(np.array(strain_y).reshape((4, 6)), cmap='coolwarm', interpolation='nearest')
plt.colorbar(label="Strain Y")
plt.title("Strain Y Distribution")
plt.show()
