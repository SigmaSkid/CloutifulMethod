import matplotlib.pyplot as plt
import numpy as np

def normal_random(mean, stddev):
    U1 = np.random.rand()
    U2 = np.random.rand()
    R = np.sqrt(-2 * np.log(U1))
    Theta = 2 * np.pi * U2
    Z0 = R * np.cos(Theta)
    return mean + Z0 * stddev

def update_plot(event):
    global bell_curve_numbers
    bell_curve_numbers = [normal_random(mean_delay, stddev_delay) for _ in range(num_samples)]
    ax.clear()
    ax.hist(bell_curve_numbers, bins=30, density=True, alpha=0.75, color='b')
    ax.plot(x, p, 'k', linewidth=2)
    ax.set_title('Bell Curve Distribution of Delay Times')
    ax.set_xlabel('Delay Time (milliseconds)')
    ax.set_ylabel('Probability Density')
    ax.grid(True)
    plt.draw()

# Initialize variables
mean_delay = 60
stddev_delay = 5
num_samples = 1000
bell_curve_numbers = [normal_random(mean_delay, stddev_delay) for _ in range(num_samples)]

# Plotting setup
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.2)
plt.hist(bell_curve_numbers, bins=30, density=True, alpha=0.75, color='b')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = np.exp(-(x - mean_delay)**2 / (2 * stddev_delay**2)) / (stddev_delay * np.sqrt(2 * np.pi))
plt.plot(x, p, 'k', linewidth=2)

plt.title('Bell Curve Distribution of Delay Times')
plt.xlabel('Delay Time (milliseconds)')
plt.ylabel('Probability Density')
plt.grid(True)

# Connect the key press event to update plot
fig.canvas.mpl_connect('key_press_event', update_plot)

plt.show()