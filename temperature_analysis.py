import numpy as np
import time

temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32
avg_fahrenheit = round(temps_fahrenheit.mean(), 1)

print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
print("Average Fahrenheit:", avg_fahrenheit)

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Shape:", scores.shape)
print("Total elements:", scores.size)
print("Highest score:", scores.max())
print("Lowest score:", scores.min())
print("Range:", scores.max() - scores.min())

numpy_array = np.arange(1, 50001)
python_list = list(range(1, 50001))

t0 = time.time()
numpy_sum = np.sum(numpy_array)
t1 = time.time()
numpy_time = t1 - t0

t0 = time.time()
python_sum = sum(python_list)
t1 = time.time()
python_time = t1 - t0

print("NumPy sum:", numpy_sum)
print("Python sum:", python_sum)
print("NumPy time:", f"{numpy_time:.4f}", "seconds")
print("Python time:", f"{python_time:.4f}", "seconds")
print("NumPy is", f"{(python_time / numpy_time):.1f}", "x faster")
