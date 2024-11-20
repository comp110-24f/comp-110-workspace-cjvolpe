def factorial(n: int) -> int:
    """Compute factorial of n."""
    # Base case n == 0 or n == 1
    if n == 1 or n == 0:
        return 1
    # Recursive case: n * recursive call with n-1 as argument
    return n * factorial(n - 1)
