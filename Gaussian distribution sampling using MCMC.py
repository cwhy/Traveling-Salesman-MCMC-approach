# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 12:56:37 2016

@author: Zhongxiang Dai
"""

# use MCMC (Metropolis algorithm) to geenrate a gaussian
# from a random walk Markov Chain

import numpy as np
import matplotlib.pyplot as plt

s = 2.0 # free parameter for uniform sampling for step 1

# Mean and Standard Deviation of the desired distribution
mu = 3
sigma = 0.1

x = 0 # value of initial sample
ITER = 100000
dist = []
dist.append(x)
for i in range(ITER):
    # Step 1
    # Uniform sampling method
#    a = np.random.rand() * s - s / 2
#    y = x + a
    
    # Gaussian sampling method
    mu_1, sigma_1 = x, 1
    y = np.random.normal(mu_1, sigma_1, 1)
    
    # Step 2
    p = min(1, np.exp(-1 * pow((y - mu), 2) / (2.0 * sigma * sigma)) / np.exp(-1 * pow((x - mu), 2) / (2.0 * sigma * sigma)))
    u = np.random.rand()
    if u < p:
        x = y
        dist.append(x)

print "Mean: ", np.mean(dist)
print "STD: ", np.std(dist)
plt.hist(dist, bins=100)
