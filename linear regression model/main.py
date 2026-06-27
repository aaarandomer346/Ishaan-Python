# yep this is what im working on, home hand baked linear regression model. yes im jobless. yes im mentally insane. maybe i understand how this works

# numpy import
# matplotlib import

# y = wx + b (y = weight * x + bias)
# loss is the difference between prediction and actual result, where each difference is squared and then averaged

# then find the gradient of the loss function for both bias and weight find the partial direvative:
# partial direvative of the Loss / partial direvative of the weight ---> for the weight
# partial direvative of the Loss / partial direvative of the bias ---> for the bias

# then take the negative of the 2 values of the weight and bias, multiply by a small step (small float)
# take the change in bias/weight (negative of the partial direvations * a small step) and subtract from the original