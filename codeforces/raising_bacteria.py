n = int(input())

def get_days(num):
    count = 0

    while(num > 1):
        if num & 1:
            count += 1
        
        num = num >> 1

    return count + 1


print(get_days(n))