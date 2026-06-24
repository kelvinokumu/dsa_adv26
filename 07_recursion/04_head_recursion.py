def head_recursion(n):
    """Recursive call happens BEFORE processing"""
    if n == 0:
        return
    head_recursion(n - 1)
    print("Head:", n)

head_recursion(5)