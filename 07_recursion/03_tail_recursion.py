def tail_recursion(n, result=0):
    """
    Recursive call is the LAST operation
    """
    if n == 0:
        return result
    return tail_recursion(n - 1, result + n)

res = tail_recursion(10)
print(res)
