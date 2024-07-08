[n, m, k] = [int(x) for x in input().split(' ')]
p = []

for i in range(0, m):
    p.append(int(input()))

f = int(input())

count = 0

for x in p:
    diff = 0
    enemy = False
    o = x ^ f

    while o:
        o &= o - 1
        diff += 1
        if diff > k:
            enemy = True
            break
    
    if not enemy:
        count += 1

print(count)
