# RecIntMult Algorithm

def karatsuba(x: int, y: int) -> int:
    # Convert to strings to determine number of digits
    x_str = str(x)
    y_str = str(y)

    # Base case: single-digit multiplication
    if len(x_str) == 1 and len(y_str) == 1:
        return x * y

    # Make lengths equal by padding with zeros
    n = max(len(x_str), len(y_str))
    if n % 2 != 0:
        n += 1

    x_str = x_str.zfill(n)
    y_str = y_str.zfill(n)

    # Split x and y into halves
    mid = n // 2
    a = int(x_str[:mid])
    b = int(x_str[mid:])
    c = int(y_str[:mid])
    d = int(y_str[mid:])

    # Compute p = a + b and q = c + d
    p = a + b
    q = c + d

    # Recursive multiplications
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pq = karatsuba(p, q)

    # Compute ad + bc
    adbc = pq - ac - bd

    # Combine results
    return ac * (10 ** n) + adbc * (10 ** (n // 2)) + bd

print(karatsuba(1234, 5678))   # 7006652
print(1234 * 5678)             # verification
