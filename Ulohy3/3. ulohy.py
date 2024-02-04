def nextPalindrome (n, base):
    valid = False
    if not 2 <= base <= 36:
        return n, int(valid)
    for n in range(n + 1, 2**64):
        number = to_base(n, base)
        if number == number[::-1]:
            valid = True
            break
    
    return n, int(valid)

def to_base(n, base):
    if n == 0:
        return [0]
    result = []
    while n > 0:
        result.insert(0, n % base)
        n = n // base
    return result

print(nextPalindrome(18446744073709551614, 2))