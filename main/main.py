import sys

sys.stdin = open('./main/input.txt', 'r')
sys.stdout = open('./main/output.txt', 'w')

t = int(input())

for x in range(t):
    total, slices = [int(y) for y in input().split(' ')]
    p = sorted([int(y) for y in input().split(' ')])
    last = p[0:-1]
    a,b=0,0
    for i in p:
        a += i - 1
        b += i
    print(a+b)
