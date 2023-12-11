#!/usr/bin/python3

"""Minimum Operations - Dynamic programming problem"""

def minOperations(n):
  if n <= 0:
    return 0
  if n == 1:
    return 1
  
  dp = [float('inf')] * (n + 1)
  dp[1] = 0

  for i in range(2, n + 1):
    for j in range(1, i):
      if i % j == 0: 
        dp[i] = min(dp[i], dp[j] + i / j)    
  return int(dp[n])
