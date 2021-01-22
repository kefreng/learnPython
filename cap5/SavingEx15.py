def gcd(a, b):
    """Calculate the Greatest Common Dividor of (a,b) """
    while b != 0:
        a, b = b, a % b
    return a

