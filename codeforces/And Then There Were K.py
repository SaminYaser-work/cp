# Find the leftmost set bit and construct 2^n
# where n in the position of that bit.
# Then, (2^n) - 1 is the answer because 2^n & (2^n) - 1 is
# always 0

t = int(input())
p = []
for i in range(0, t):
    p.append(int(input()))

for x in p:
    print((1 << (x.bit_length() - 1)) - 1)