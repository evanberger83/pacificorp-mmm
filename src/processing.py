import numpy as np

def adstock(x, alpha=0.5):
    result = np.zeros_like(x)
    for i in range(len(x)):
        if i == 0:
            result[i] = x[i]
        else:
            result[i] = x[i] + alpha * result[i-1]
    return result


def saturation(x, alpha=1.5, theta=100):
    return (x ** alpha) / (x ** alpha + theta ** alpha)
