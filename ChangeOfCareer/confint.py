import math

"""
Written by Idriani Mandal - Univeristy of Rhode Island

Compute the 95% confidence interval for a classification problem.
  acc -- classification accuracy
  n -- number of observations used to computethe accuracy
Returns a tuple (lb, ub)
"""
def classification_confint(acc, n):
  interval = 1.96 * math.sqrt(acc * (1 - acc) / n)
  lb = max(0, acc - interval)
  ub = min(1.0, acc + interval)
  
  return lb, ub

"""
Compute the 95% confidence interval for a regression problem.
  rs_score -- R^2 score
  n -- number of observations used to compute the R^2 score
  k -- number of independent variables in dataset
Returns a tuple (lb, ub)

Reference: https://books.google.com/books?id=gkalyqTMXNEC&pg=PA88#v=onepage&q&f=false
"""
def regression_confint(rs_score, n, k):
  interval = 2 * math.sqrt((4 * rs_score * (1 - rs_score)**2 * (n - k - 1)**2) / ((n**2 - 1) * (n + 3)))
  lb = max(0, rs_score - interval)
  ub = min(1.0, rs_score + interval)
  
  return lb, ub
