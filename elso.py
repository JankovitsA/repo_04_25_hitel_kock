import numpy as np
import matplotlib.pyplot as plt

def generate_synthetic_data(x, coefficients, seed=4, noise_std=1):
    np.random.seed(seed)
    y = np.polyval(coefficients[::-1], x) + np.random.normal(0, noise_std, len(x))

def visualize_data(x,y):
    plt.scatter(x,y)
    plt.xlabel("Feature (x)")
    plit.title("Synthetic Data")
    plt.show()

def main():
    coefficients = [1, 0.02, -0.002, 0.014]
    x_values = np.linspace(-10,10,100)
    x,y = generate_synthetic_data(x_values,coefficients)
    visualize_data(x,y)