# -*- coding: utf-8 -*-
"""homework0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VAeemU2MBiG358sp54946n7aECcTNw_J

# CIS 5200: Machine Learning
## Homework 0
"""

import os
import sys

# For autograder only, do not modify this cell. 
# True for Google Colab, False for autograder
NOTEBOOK = (os.getenv('IS_AUTOGRADER') is None)
if NOTEBOOK:
    print("[INFO, OK] Google Colab.")
else:
    print("[INFO, OK] Autograder.")
    sys.exit()

"""### Penngrader setup"""

# %%capture
!pip install penngrader-client

# Commented out IPython magic to ensure Python compatibility.
# %%writefile config.yaml
# grader_api_url: 'https://23whrwph9h.execute-api.us-east-1.amazonaws.com/default/Grader23'
# grader_api_key: 'flfkE736fA6Z8GxMDJe2q8Kfk8UDqjsG3GVqOFOa'

from penngrader.grader import PennGrader

# PLEASE ENSURE YOUR PENN-ID IS ENTERED CORRECTLY. IF NOT, THE AUTOGRADER WON'T KNOW WHO 
# TO ASSIGN POINTS TO YOU IN OUR BACKEND
STUDENT_ID = 17125403
SECRET = STUDENT_ID

grader = PennGrader('config.yaml', 'CIS5200_23Sp_HW0', STUDENT_ID, SECRET)

"""# PyTorch

Programming assignments will be primarily done in PyTorch. If you've used NumPy before, then you'll find that PyTorch has many of the same functionalities plus more. 

The base object in PyTorch is the Tensor. See this tutorial for a brief primer on the syntax: https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
"""

import torch

A = torch.randn(5,6)
print(A)

"""
Nearly all low-level functions are already implemented in PyTorch. *Check the documentation before implementing anything yourself*: https://pytorch.org/docs/stable/index.html

Many functions are built-in to the `torch.Tensor` object. For example, instead of calling `torch.sum(X)`, you can call `X.sum()` directly. Some of these functions such as `matmul`, `mm`, or `dot` will be useful for implementing matrix operations. A full list of tensor operations can be found here: https://pytorch.org/docs/stable/tensors.html"""

A = torch.randn(5,6)
B = torch.randn(6,2)
print(A.mm(B))

"""PyTorch has a fairly extensive distributions library, which allows you to generate samples, compute probabilities, and other statistical quantities. In this example we can construct a Bernoulli random variable with parameter $p=0.8$ and calculate the log probability of the following observations `[1,0,0,1,1]`. """

from torch.distributions.bernoulli import Bernoulli

X = Bernoulli(0.8)
print(X.log_prob(torch.Tensor([1,0,0,1,1])))

"""# Matrix operations
Let $X\in \mathbb R^{m\times n}$ be a data matrix of $m$ samples with $n$ features. Implement the batched sample gradient, $\nabla_X f(X)$, for each of the calculus problems from the written homework. The batched sample gradient is the $m\times n$ matrix where the $i$th row is the gradient of $f$ with respect to the $i$th sample. 

Do so using matrix operations without any for loops. As an example, the first one has been done for you. 

Some variables other than $X$ can also be batched, such as sample labels $Y \in \mathbb R^{m}$. For such functions, the $i$th sample gradient of these examples is taken with respect to the sample $x_i$ using the sample label $y_i$: $\nabla_{x_i} f(x_i,y_i)$. 


1. $f(x_i;w) = w^\top x_i$ 
2. $f(x_i) = x_i^\top x_i$ 
3. $f(x_i,y_i;w) = (y_i-w^\top x_i)^2$
4. $f(x_i,y_i;w) = \log(1 + \exp(-y_iw^\top x_i))$
5. $f(x_i;A) = x_i^\top Ax_i$
"""

import torch

def grad1(X, w): 
    # X := Tensor of size (m,n) 
    # w := Tensor of size (n,)
    # Return := Tensor of size (m,n) 
    m = X.size(0)
    return w.repeat(m,1)
    # return torch.zeros(X.size())
    # return X.zero_()

def grad2(X): 
    # X := Tensor of size (m,n) 
    # Return := Tensor of size (m,n) 
    return X.multiply(2)

def grad3(X, y, w): 
    # X := Tensor of size (m,n) 
    # y := Tensor of size (m,)
    # w := Tensor of size (n,)
    # Return := Tensor of size (m,n) 
    m = X.size(0)
    s = w.repeat(m, 1).multiply(-2)
    a = X.multiply(2).multiply(w.dot(w))
    return s.add(a)

def grad4(X, y, w): 
    # X := Tensor of size (m,n) 
    # w := Tensor of size (n,)
    # Return := Tensor of size (m,n) 
    num = torch.exp(X.mm(w).multiply(-y))
    ones = torch.full((X.size(dim=1), 1), 1)
    den = ones.add(den)
    factor = num.divide(den)
    return factor.mm(w.T).multiply(-y)

def grad5(X, A): 
    # X := Tensor of size (m,n) 
    # w := Tensor of size (n,)
    # Return := Tensor of size (m,n) 
    return A.mm(X).add(A.T.mm(X))

for i in range(1,6): 
    grader.grade(test_case_id = f'grad{i}_test', answer = locals()[f'grad{i}'])

"""# Dataset statistics

Let $X\in \mathbb R^{m\times n}$ be a data matrix of $m$ samples with dimension 
$n$. Implement the following functions to calculate dataset statistics: 

1. Calculate the mean of each feature using the unbiased sample mean
2. Calculate the variance of each feature using the unbiased sample variance
3. Normalize the data matrix to have zero mean and unit variance along each feature. 
"""

import math
def stat1(X): 
    # Calculate the unbiased sample mean for each feature of the data matrix X. 
    # The ith entry in the returned tensor should have the sample mean of the 
    # ith feature. 
    # X := Tensor of size (m,n) 
    # Return := Tensor of size (n,) 
    return torch.mean(X, 0, True)

def stat2(X): 
    # Calculate the unbiased sample variance for each feature of the data 
    # matrix X. The ith entry in the returned tensor should have the unbiased 
    # sample variance of the ith feature
    # X := Tensor of size (m,n) 
    # Return := Tensor of size (n,) 
    return torch.var(X, dim=0, unbiased=True)

def stat3(X): 
    # Normalize the data matrix X. The ijth entry in the returned tensor should 
    # have the normalized entry of X[i,j]. 
    var, mean = torch.var_mean(X, 0, unbiased=True)
    std = torch.sqrt(var)
    return X.divide(std).subtract(mean.divide(std))

for i in range(1,4): 
    grader.grade(test_case_id = f'stat{i}_test', answer = locals()[f'stat{i}'])

"""# Sampling and plotting

Draw samples from a 2D multivariate Gaussian with mean $\mu=[-1,2]$ and covariance matrix $\Sigma=\left[\begin{array}{cc} 1 & 2 \\ 2 & 5\end{array}\right]$. 

Then, plot this data using matplotlib. The plotting is not autograded, but you can compare your result with the image at the end of this notebook. 
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib
# %matplotlib inline
import matplotlib.pyplot as plt
from torch.distributions.multivariate_normal import MultivariateNormal

def sample(n): 
    # Draw samples from a 2D Gaussian with the given parameters. The ith row of 
    # the output should have a drawn sample. 
    # Return := Tensor of size (n,2) 
    mean = torch.tensor([-1.0, 2.0])
    cov = torch.tensor([[1.0, 2.0], [2.0, 5.0]])
    m = MultivariateNormal(mean, cov)
    print(m.sample())
    res = torch.zeros(n, 2)
    for i in range(n):
      res[i, 0], res[i, 1] = m.sample()
    return res

def plot(X): 
    # Plot data from the given matrix. Each row in X is a data point with 2 
    # features to be plotted. 
    # X := Tensor of size (m,2) 
    torch.Tensor.ndim = property(lambda self: len(self.shape))
    x = X[:, 0]
    y = X[:, 1]
    plt.scatter(x, y)
    plt.show()

grader.grade(test_case_id = 'sample_test', answer = sample)

"""Plotting the data sampled from the previous problem should show something like this: 

![image.png](data:image/png;base64,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)

# Submitting to Gradescope
Before submitting to Gradescope, make sure that selecting "Runtime" -> "Restart and run all" completes all cells without errors. 

1. Go to the File menu and choose "Download .ipynb" and also "Download .py". Make sure these files are named homework0.ipynb and homework0.py, respectively
2. Go to GradeScope through the canvas page and ensure your class is "BAN_CIS-5200-001 202310"
3. Select Homework 0
4. Upload both files
5. PLEASE CHECK THE AUTOGRADER OUTPUT TO ENSURE YOUR SUBMISSION IS PROCESSED CORRECTLY!
You should be set! This assignment is autograded to give you feedback, but is not worth any points. However, completion of this assignment is required to pass the course.
"""