def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    count = 0
    i = 0

    while True:
        if is_prime(i):
            count += 1

        if count == 10001:
            print(i)
            break
        i += 1

main()