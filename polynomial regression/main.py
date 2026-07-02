# same as linear regression model
# however, there are multiple variables
# first start with the second degree
# m1x^2 + m2x + b
# m1 and m2 are different values for X
# one key difference is that for every weight, the derivitives will need to be calculated seperately.

import matplotlib.pyplot as plt
import numpy as np
import random

def show_graph():
    plt.show()

def make_graph(x_data, y_data, y, weights, intercept):
    plt.figure(figsize= (10, 5))

    plt.scatter(x_data, y_data, color="Orange")

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.plot(
        x_data, 
        y,
        label=f"Custom Regression: y = {weights} + {intercept}"
    )

    plt.title("Custom linear regression visualisation", fontsize=14, fontweight="bold")
    plt.xlabel("X (iv)", fontsize=12)
    plt.ylabel("Y (dv)", fontsize=12)
    plt.legend(loc="upper left", frameon=True)
    plt.grid(True, linestyle="--", alpha=0.5)

def predict(weights, x, intercept):
    prediction = 0
    for i in range(len(weights)):
        prediction += weights[i] * x ** (len(weights) - i)
    return prediction + intercept

def learn(x, y, weights, intercept, step, learn_amount):
    count = 0
    for a in range(learn_amount):
        count += 1
        # for each weight i need to do the gradient decsent.
        grad_intercept = 0
        weight_slopes = [0] * len(weights)
        # iterate over all values of x
        for i in range(len(x)):
            y_pred = predict(weights, x[i], intercept) # predict
            residual = y_pred - y[i] # find loss
            grad_intercept += 2 * residual # intercept gradient decsent

            for j in range(len(weights)):
                weight_slopes[j] += 2 * (x[i] ** (len(weights) - j)) * residual # gradient descent for all weights in the array
        
        for k in range(len(weights)):
            weight_slopes[k] /= len(x) # average out the gradient descent of all weights
            weights[k] -= weight_slopes[k] * step # adjust all weights

        grad_intercept = grad_intercept / len(x) # average gradient descent for interceopt
        intercept -= step * grad_intercept # adjust intercept

    return weights, intercept

def make_r_square(x_data, weights, intercept, y):
    average = 0
    ssres = 0
    sstot = 0

    for k in y:
        average += k
    average /= len(y)

    for i in range(len(x_data)):
        y_predict = predict(weights, x_data[i], intercept)
        ssres += (y_predict - y[i]) ** 2
        sstot += (y[i] - average) ** 2
    
    return 1 - (ssres / sstot)

nth = input("ending degree: ")
nth_start = input("starting degree:  ")

results = []

for i in range(int(nth) - int(nth_start) + 1):
    results.append([None, None, None, None])
# [[degree of polynomial, r^2], [degree of polynomial, r^2]]

y = np.array([    3.1,     3.2,     6.3,    15.8,    38.4,    86.9,   175.2,
               317.1,   528.7,   840.1,  1281.3,  1859.8,  2636.4,  3609.2,
              4861.7,  6392.0,  8244.5, 10523.8, 13198.4, 16401.2, 20089.6])
x = np.array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,
               5. ,  5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5,  9. ,  9.5, 10. ])

x_data = x[:16]
y_data = y[:16]

x_test = x[16:21]
y_test = y[16:21]

x_min, x_max = np.min(x_data), np.max(x_data)
y_min, y_max = np.min(y_data), np.max(y_data)

y_data = (y_data - y_min) / (y_max - y_min)
y_test = (y_test - y_min) / (y_max - y_min)

x_data = (x_data - x_min) / (x_max - x_min)
x_test = (x_test - x_min) / (x_max - x_min)


# print(len(x_test), len(x_data))
#print(len(y_test), len(y_data))

for i in range(int(nth_start), int(nth) + 1):
    weights = []
    for j in range(i):
        weights.append(random.uniform(0, 0.1))
    # weights = [0.5, 2, 1]
    intercept = random.uniform(0, 0.1)
    # intercept = 5

    step = 0.0001 # * (0.001 ** (i - 2))
    learn_amount = 400000

    weights, intercept = learn(x_data, y_data, weights, intercept, step, learn_amount)
    r_squared = make_r_square(x_test, weights, intercept, y_test)

    results[i - int(nth_start)][0] = i
    results[i - int(nth_start)][1] = r_squared
    results[i - int(nth_start)][2] = weights
    results[i - int(nth_start)][3] = intercept

    plt.close('all')

best_polynomial_fit = None
current_r_squared = None
previous_r_squared = 0

for r in results:
    current_r_squared = r[1]
    if current_r_squared > previous_r_squared:
        best_polynomial_fit = r[0]
    previous_r_squared = current_r_squared

print(best_polynomial_fit)

weights = results[best_polynomial_fit - int(nth_start)][2]
intercept = results[best_polynomial_fit - int(nth_start)][3]

make_graph(x_data, y_data, predict(weights, x_data, intercept), weights, intercept)
show_graph()
make_graph(x_test, y_test, predict(weights, x_test, intercept), weights, intercept)
show_graph()