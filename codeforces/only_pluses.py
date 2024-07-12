import functools
import operator

t = int(input())

nums = []
for x in range(t):
    nums.append([int(y) for y in input().split(' ')])

for n in nums:
    for i in range(5):
        m = n.index(min(n))
        n[m] += 1
    print(functools.reduce(operator.mul, n))