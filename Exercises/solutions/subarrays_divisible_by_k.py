#You are given an array of positive and/or negative integers and a value K .
# The task is to find count of all sub-arrays whose sum is divisible by K?

#Let there be a subarray (i, j) whose sum is divisible by k
# sum(i, j) = sum(0, j) - sum(0, i-1)
# Sum for any subarray can be written as q*k + rem where q is a quotient and rem is remainderThus,
#       sum(i, j) = (q1 * k + rem1) - (q2 * k + rem2)
#       sum(i, j) = (q1 - q2)k + rem1-rem2
# We see, for sum(i, j) i.e. for sum of any subarray to bedivisible by k,
# the RHS should also be divisible by k.(q1 - q2)k is obviously divisible by k, for (rem1-rem2)
# to follow the same, rem1 = rem2 where
# rem1 = Sum of subarray (0, j) % k
# rem2 = Sum of subarray (0, i-1) % k