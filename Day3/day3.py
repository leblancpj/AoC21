import math
import numpy as np
from numpy.core.fromnumeric import prod
import pandas as pd
from collections import Counter


def most_common(pos_list=None):
    most_common = Counter(pos_list).most_common()
    # check for equivalence
    if most_common[0][1] == most_common[1][1]:
        return '1'
    else:
        return most_common[0][0]

def least_common(pos_list=None):
    most_common = Counter(pos_list).most_common()
    # check for equivalence
    if most_common[0][1] == most_common[1][1]:
        return '0'
    else:
        return most_common[1][0]

def oxy_gen_rating(report=[]):
    df = pd.DataFrame(report)
    for idx in range(df.columns.size):
        # Get most common
        common_bit = most_common(df[idx])
        # Filter df    
        df = df[df[idx] == common_bit]
        if df.shape[0] == 1:
            break
    rating = df.values.squeeze()
    return int(''.join(rating),2)

def co2_scrubber_rating(report=[]):
    df = pd.DataFrame(report)
    for idx in range(df.columns.size):
        # Get least common
        common_bit = least_common(df[idx])
        # Filter df    
        df = df[df[idx] == common_bit]
        if df.shape[0] == 1:
            break
    rating = df.values.squeeze()
    return int(''.join(rating),2)

# Part 1.
# Get input data
#filepath = ".\Day3\sample.txt"
filepath = ".\Day3\input.txt"
report = open(filepath).read().split("\n")
linelist = [list(line) for line in report]
# This line is zipping the line list with itself
# The * forces a continued repeat of the linelist 
# It's equivalent to:
# If linelist = [['1','2','3'],['4','5','6'],['7,'8','9']]
# zip(*linelist) = zip(['1','2','3'],['4','5','6'],['7,'8','9']) = [['1','4','7'],['2','5','8'],['3','6','9']]
# The rest is converting to list of list instead of tuples.
# See: https://stackoverflow.com/questions/6473679/transpose-list-of-lists
report_pos = list(map(list,zip(*linelist)))
# This might be confusing so I will try to explain:
# Foreach position list, find the most common element using Counter object,
# Take the first one for gamme (last one for epsilon),
# Counter returns the values and the counts of those values. Since I'm asking for the most common,
# I don't care about actual count of 1 or 0.  I just need whether it is the 1 or 0.
# At this point it returns a list of string 0 or 1, which I join together in a single string
# using join.  Then I convert the whole thing into a number using int.
# The parameter 2 specifies the base of the number I'm passing in, which is binary.
gamma = "".join([most_common(x) for x in report_pos])
epsilon = "".join([least_common(x) for x in report_pos])
print("part 1 answer: ", int(gamma,2)*int(epsilon,2))


# Part 2
# I have to rescan for most common after each removal.
# Oxygen Generator Rating
oxy_gen = oxy_gen_rating(linelist)
co2_scrubber = co2_scrubber_rating(linelist)
print("part 2 answer: ",oxy_gen*co2_scrubber)