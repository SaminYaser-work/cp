t = int(input())
p = []
for i in range(0, t):
    p.append(int(input()))

for x in p:
    count = x
    while x:
        x &= x - 1
        count -= 1
    print(count)