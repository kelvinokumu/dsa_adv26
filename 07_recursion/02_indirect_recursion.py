def function_a(n):
    """Function A calls Function B"""
    if n <= 0:
        return
    print("A:", n)
    function_b(n - 1)

def function_b(n):
    """Function B calls Function A"""
    if n <= 0:
        return
    print("B:", n)
    function_a(n - 1)

function_a(5)