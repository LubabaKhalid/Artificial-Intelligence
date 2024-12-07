def calculate_mean(values):
    return sum(values) / len(values)

def calculate_slope(X, Y, mean_X, mean_Y):
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(len(X)))
    return numerator / denominator
def calculate_intercept(mean_X, mean_Y, slope):
    return mean_Y - slope * mean_X
def predict(X, theta_0, theta_1):
    return [theta_0 + theta_1 * x for x in X]
def calculate_mse(Y, Y_pred):
    return sum((Y[i] - Y_pred[i]) ** 2 for i in range(len(Y))) / len(Y)
def fit_linear_regression(X, Y):
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)
    slope = calculate_slope(X, Y, mean_X, mean_Y)
    intercept = calculate_intercept(mean_X, mean_Y, slope)
    
    return intercept, slope
if __name__ == "__main__":
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]
    theta_0, theta_1 = fit_linear_regression(X, Y)
    print(f"Fitted Model: theta_0 (intercept) = {theta_0}, theta_1 (slope) = {theta_1}")
    Y_pred = predict(X, theta_0, theta_1)
    print(f"Predictions: {Y_pred}")
    mse = calculate_mse(Y, Y_pred)
    print(f"Mean Squared Error (MSE): {mse}")
    X_new = [10, 20, 30, 40, 50]
    Y_new = [15, 25, 35, 45, 55]
    
    theta_0_new, theta_1_new = fit_linear_regression(X_new, Y_new)
    print(f"\nNew Dataset Model: theta_0 = {theta_0_new}, theta_1 = {theta_1_new}")
    
    Y_new_pred = predict(X_new, theta_0_new, theta_1_new)
    mse_new = calculate_mse(Y_new, Y_new_pred)
    print(f"New Dataset Predictions: {Y_new_pred}")
    print(f"New Dataset MSE: {mse_new}")
