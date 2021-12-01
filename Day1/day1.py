# Given a series of input numbers, count the number of times
# the values increase from one to the next.
import pandas as pd


# Part 1
sample = pd.read_csv(".\Day1\sample.txt", header=None, squeeze=True) 
input = pd.read_csv(".\Day1\input.txt", header=None, squeeze=True)
#print(type(input))
ans = input.diff(1).apply(lambda x: x > 0).sum()
#print(ans)


# Part 2
#print(sample)
rolling = input.rolling(window=3,min_periods=3,center=True)
print(rolling.sum().dropna().diff(1).apply(lambda x: x > 0).sum())
