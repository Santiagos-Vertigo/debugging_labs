""""
Lab 01 - Assertions

Goal:
- Understand how assertions fail
- Learn traceback output
- Use assertions to protect assumptions
"""

def factorial(n):
    #preconditions
    assert isinstance(n, int), "n must be an integer"
    assert n >= 0, "n must be non integer"

    result = 1
    for i in range(1, n + 1):
        result *= i

    # Postposition
    assert result > 0, "result must be positive"

    return result

def run_tests():
    print("Running assertion tests ...\n")

    # Valid case
    # print("Factorial(5): ", factorial(5))

    # Intentional Failiures  (uncomment one at a time)
    print("factorial(3):", factorial(3))
    # print("factorial(2.5)", factorial(2.5))

if __name__ == "__main__":
    run_tests()