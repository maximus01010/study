import numpy as np
import matplotlib.pyplot as plt

# Given dataset
temperature = np.array([18, 22, 26, 30, 34, 38, 40, 44, 48, 50, 54, 58, 60, 64, 68, 70, 74, 78, 80])
voltage = np.array([0.294, 0.366, 0.388, 0.429, 0.47, 0.51, 0.531, 0.581, 0.623, 0.651, 0.687, 0.718, 0.742, 0.79, 0.827, 0.85, 0.885, 0.918, 0.94])

# Perform linear regression
coefficients = np.polyfit(temperature, voltage, 1)
line_fit = np.polyval(coefficients, temperature)

# Calculate deviations
deviations = voltage - line_fit

# Find maximum deviation
max_deviation = np.max(np.abs(deviations))

# Plot the data and the best-fitting line
plt.scatter(temperature, voltage, label='Data')
plt.plot(temperature, line_fit, color='red', label='Best-Fitting Line')
plt.title('Temperature vs Voltage with Best-Fitting Line')
plt.xlabel('Temperature')
plt.ylabel('Voltage')
plt.legend()
plt.show()

# Output the max deviation
print(f'Max Deviation: {max_deviation}')
