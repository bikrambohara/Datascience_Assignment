import random
import numpy as np
random.seed(4090)
data = np.array([ random.randint(30, 100) for i in range(50) ])
mean = np.mean(data)
median = np.median(data)

unique, counts = np.unique(data, return_counts=True)
max = np.argmax(counts)
mode = unique[max]

ranges = np.ptp(data)
q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.50)
q3 = np.quantile(data, 0.75)
iqr = q3 - q1


print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Range: {ranges}")
print(f"Quartile 1: {q1}")
print(f"Quartile 2: {q2}")
print(f"Quartile 3: {q3}")
print(f"Interquartile range: {iqr}")