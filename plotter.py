import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = 'csv/clean_square.csv'  # Update this to your file path
data = np.loadtxt(file_path, delimiter=',')

# Define the range for the shorter sample
start = 0  # Start of the range
end = len(data)  # End of the range

# Select the shorter sample range from the first column
short_sample = data[start:end, 0]

# Plotting the short sample
plt.figure(figsize=(10,6))
plt.plot(short_sample, label='Channel 1 (Short Sample)')
plt.title('Short Sample of ADC Channel 1 Data')
plt.xlabel('Sample Number')
plt.ylabel('ADC Reading')
plt.legend()
plt.grid(True)
plt.show()
