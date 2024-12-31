import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
def perceptron(X, y, learning_rate, epochs):
    weights = np.zeros(X.shape[1])
    bias = 0
    for epoch in range(epochs):
        for i in range(len(X)):
            linear_output = np.dot(X[i], weights) + bias
            prediction = 1 if linear_output >= 0 else 0
            error = y[i] - prediction
            weights += learning_rate * error * X[i]
            bias += learning_rate * error
    
    return weights, bias
def plot_perceptron_boundary(X, y, weights, bias):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = np.dot(np.c_[xx.ravel(), yy.ravel()], weights) + bias
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, levels=[-1, 0, 1], cmap='coolwarm', alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k', marker='o')
    plt.title("Perceptron Decision Boundary")
    plt.show()
X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  
y_xor = np.array([0, 1, 1, 0])  
def train_xor_nn(X, y):
    model = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', max_iter=10000)
    model.fit(X, y)
    return model
def visualize_xor_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k', marker='o')
    plt.title("XOR Neural Network Decision Boundary")
    plt.show()
def main():
   
    perceptron_weights, perceptron_bias = perceptron(X_xor, y_xor, learning_rate=0.1, epochs=100)
    plot_perceptron_boundary(X_xor, y_xor, perceptron_weights, perceptron_bias)
    xor_model = train_xor_nn(X_xor, y_xor)
    visualize_xor_boundary(xor_model, X_xor, y_xor)

if __name__ == "__main__":
    main()
