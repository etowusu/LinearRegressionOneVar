def gradientDescent(X, y, theta, alpha, iterations):
    for _ in range(iterations):
        temp = np.dot(X, theta) - y
        temp = np.dot(X.T, temp)              #the hypothesis 
        theta = theta - (alpha/m) * temp
    return theta
