"""
Python Decorators - Complete Guide with Timing Example

WHAT ARE DECORATORS?
- Functions that modify the behavior of other functions
- Wrapper pattern: decorator wraps another function
- Syntax: @decorator_name above function definition

SYNTAX EQUIVALENCE:
    @decorator
    def function():
        pass

    # Is exactly the same as:
    function = decorator(function)

COMMON USE CASES:
- Logging function calls
- Timing function execution
- Access control / authentication
- Caching results (memoization)
- Input validation

TODAY'S GOAL: Implement 5 different decorators to understand the pattern
"""

import functools
import time
from typing import Callable

# =============================================================================
# DECORATOR 1: Simple Decorator (Warmup)
# =============================================================================


def simple_decorator(func: Callable) -> Callable:
    """
    Basic decorator that prints before and after function execution.

    HINT FOR IMPLEMENTATION:
    1. Define an inner function called 'wrapper' that takes *args, **kwargs
    2. Print "Before calling [function name]"
    3. Call the original function: result = func(*args, **kwargs)
    4. Print "After calling [function name]"
    5. Return the result
    6. Return the wrapper function

    Example usage:
        @simple_decorator
        def greet(name):
            print(f"Hello, {name}!")

        greet("Alice")
        # Output:
        # [Before calling greet]
        # Hello, Alice!
        # [After calling greet]
    """

    def wrapper(*args, **kwargs):
        print(f"before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"after calling {func.__name__}")
        return result

    return wrapper


# =============================================================================
# DECORATOR 2: Timing Decorator (Main Example)
# =============================================================================


def timing_decorator(func: Callable) -> Callable:
    """
    Decorator to measure function execution time.

    HINT FOR IMPLEMENTATION:
    1. Use @functools.wraps(func) to preserve function metadata
    2. Define wrapper(*args, **kwargs)
    3. Record start time: start_time = time.perf_counter()
    4. Call function and get result
    5. Record end time: end_time = time.perf_counter()
    6. Calculate elapsed: elapsed_time = end_time - start_time
    7. Print: f"{func.__name__} took {elapsed_time:.4f} seconds"
    8. Return result

    Why use @functools.wraps(func)?
    - Preserves original function's name, docstring, etc.
    - Without it, wrapper function loses the original function metadata

    Example usage:
        @timing_decorator
        def slow_function():
            time.sleep(1)
            return "Done"

        slow_function()  # Will print execution time
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.4f} seconds")
        return res

    return wrapper


# =============================================================================
# DECORATOR 3: Decorator with Arguments
# =============================================================================


def repeat(times: int):
    """
    Decorator that repeats function execution N times.

    HINT FOR IMPLEMENTATION (3 levels of functions!):
    1. Outer function: def repeat(times: int)
    2. Middle function: def decorator(func: Callable)
    3. Inner function: def wrapper(*args, **kwargs)
    4. In wrapper: Use a for loop to call func 'times' times
    5. Store results in a list and return it

    This is a DECORATOR FACTORY - it creates decorators!

    Example usage:
        @repeat(3)
        def greet():
            print("Hello!")

        greet()  # Prints "Hello!" 3 times
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = []
            for _ in range(times):
                res.append(func(*args, **kwargs))
            return res

        return wrapper

    return decorator


# =============================================================================
# DECORATOR 4: Memoization Decorator (Caching)
# =============================================================================


def memoize(func: Callable) -> Callable:
    """
    Caches function results for given arguments.

    HINT FOR IMPLEMENTATION:
    1. Create empty dictionary: cache = {}
    2. In wrapper, check if args are in cache
    3. If in cache: return cached result
    4. If not in cache: call function, save to cache, return result

    Why memoization?
    - Avoid recomputing expensive recursive functions
    - Example: fibonacci(30) without cache = slow
    - With cache: instant on second call!

    Example usage:
        @memoize
        def fibonacci(n):
            if n <= 1:
                return n
            return fibonacci(n-1) + fibonacci(n-2)

        # First call: slow
        # Second call with same n: instant!
    """
    cache = {}  # Dictionary to store cached results

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            res = func(*args)
            cache[args] = res
            return res

    return wrapper


# =============================================================================
# DECORATOR 5: Class-Based Decorator (Advanced)
# =============================================================================


class CountCalls:
    """
    Decorator as a class - counts function calls.

    HINT FOR IMPLEMENTATION:
    1. __init__(self, func): Store the function and initialize count = 0
    2. __call__(self, *args, **kwargs): This makes the instance callable
       - Increment self.count
       - Print call number
       - Call the original function
       - Return result

    Why use a class?
    - Can store state (like call count)
    - More readable for complex decorators

    Example usage:
        @CountCalls
        def greet():
            print("Hello")

        greet()  # Call #1 to greet
        greet()  # Call #2 to greet
    """

    def __init__(self, func: Callable):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        res = self.func(*args, **kwargs)
        return res


# =============================================================================
# PRACTICAL EXAMPLES - Test Your Decorators Here!
# =============================================================================


@timing_decorator
def calculate_sum_slow(n: int) -> int:
    """Calculate sum 1 to n using loop (slower)"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


@timing_decorator
def calculate_sum_fast(n: int) -> int:
    """Calculate sum 1 to n using formula (faster)"""
    return n * (n + 1) // 2


@memoize
@timing_decorator
def fibonacci_optimized(n: int) -> int:
    """
    Fibonacci with memoization.
    NOTE: Multiple decorators stack (bottom executes first)
    Order: @memoize wraps @timing_decorator wraps fibonacci_optimized
    """
    if n <= 1:
        return n
    return fibonacci_optimized(n - 1) + fibonacci_optimized(n - 2)


@repeat(3)
def roll_dice() -> int:
    """Simulates rolling a dice"""
    import random

    result = random.randint(1, 6)
    print(f"Rolled: {result}")
    return result


@CountCalls
def process_data():
    """Function with call counting"""
    return "Processing..."


# =============================================================================
# DEMONSTRATION - Run this to test your implementations
# =============================================================================


def main():
    print("=" * 60)
    print("PYTHON DECORATORS - TEST YOUR IMPLEMENTATION")
    print("=" * 60)

    # Test 1: Simple Decorator
    print("\n[TEST 1] Simple Decorator:")

    @simple_decorator
    def say_hello():
        print("Hello, World!")

    say_hello()

    # Test 2: Timing Decorator
    print("\n[TEST 2] Timing Decorator - Compare slow vs fast:")
    n = 1_000_000
    result1 = calculate_sum_slow(n)
    result2 = calculate_sum_fast(n)
    print(f"Results match: {result1 == result2}")

    # Test 3: Repeat Decorator
    print("\n[TEST 3] Repeat Decorator - Roll dice 3 times:")
    rolls = roll_dice()
    print(f"All rolls: {rolls}")

    # Test 4: Memoization Decorator
    print("\n[TEST 4] Memoization - Notice speedup on 2nd call:")
    print("First call:")
    fib_result = fibonacci_optimized(30)
    print(f"Result: {fib_result}")
    print("\nSecond call (should be instant - cached!):")
    fib_result2 = fibonacci_optimized(30)
    print(f"Result: {fib_result2}")

    # Test 5: Class-Based Decorator
    print("\n[TEST 5] CountCalls - Track function calls:")
    process_data()
    process_data()
    process_data()

    print("\n" + "=" * 60)
    print("All tests complete! Check if your decorators work correctly.")
    print("=" * 60)


if __name__ == "__main__":
    main()
