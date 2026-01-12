"""
Fibonacci Generator
====================
Learn: How generators yield values lazily (on-demand) instead of storing all in memory.

Your task: Implement generators that yield Fibonacci numbers.
"""

from typing import Generator


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """
    Generate first n Fibonacci numbers.

    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)

    Args:
        n: Number of Fibonacci numbers to generate

    Yields:
        Next Fibonacci number in sequence

    Example:
        list(fibonacci_generator(7)) -> [0, 1, 1, 2, 3, 5, 8]
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci_infinite() -> Generator[int, None, None]:
    """
    Generate infinite Fibonacci sequence.

    This generator never stops - use with islice or break!

    Example:
        from itertools import islice
        list(islice(fibonacci_infinite(), 10)) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_range(min_val: int, max_val: int) -> Generator[int, None, None]:
    """
    Generate Fibonacci numbers within a range [min_val, max_val].

    Args:
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)

    Yields:
        Fibonacci numbers where min_val <= fib <= max_val

    Example:
        list(fibonacci_range(5, 50)) -> [5, 8, 13, 21, 34]
    """
    a, b = 0, 1
    while a <= max_val:
        if a >= min_val:
            yield a
        a, b = b, a + b


# =============================================================================
# BONUS: Generator with send()
# =============================================================================


def fibonacci_resettable() -> Generator[int, bool, None]:
    """
    BONUS: Fibonacci generator that can be reset via send().

    Calling gen.send(True) resets the sequence to start.

    Example:
        gen = fibonacci_resettable()
        next(gen)  # 0
        next(gen)  # 1
        next(gen)  # 1
        gen.send(True)  # Reset! Returns 0
        next(gen)  # 1
    """
    a, b = 0, 1
    while True:
        value = a
        a, b = b, a + b
        reset = yield value
        if reset:
            a, b = 0, 1


# =============================================================================
# TESTS
# =============================================================================


def test_fibonacci_generator_basic():
    """Test basic Fibonacci sequence generation."""
    result = list(fibonacci_generator(7))
    expected = [0, 1, 1, 2, 3, 5, 8]
    assert result == expected, f"Expected {expected}, got {result}"
    print("[PASS] test_fibonacci_generator_basic")


def test_fibonacci_generator_zero():
    """Test with n=0 returns empty."""
    result = list(fibonacci_generator(0))
    assert result == [], f"Expected [], got {result}"
    print("[PASS] test_fibonacci_generator_zero")


def test_fibonacci_generator_one():
    """Test with n=1 returns [0]."""
    result = list(fibonacci_generator(1))
    assert result == [0], f"Expected [0], got {result}"
    print("[PASS] test_fibonacci_generator_one")


def test_fibonacci_generator_two():
    """Test with n=2 returns [0, 1]."""
    result = list(fibonacci_generator(2))
    assert result == [0, 1], f"Expected [0, 1], got {result}"
    print("[PASS] test_fibonacci_generator_two")


def test_fibonacci_generator_large():
    """Test larger sequence."""
    result = list(fibonacci_generator(15))
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    assert result == expected, f"Expected {expected}, got {result}"
    print("[PASS] test_fibonacci_generator_large")


def test_fibonacci_infinite():
    """Test infinite generator with islice."""
    from itertools import islice

    result = list(islice(fibonacci_infinite(), 10))
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert result == expected, f"Expected {expected}, got {result}"
    print("[PASS] test_fibonacci_infinite")


def test_fibonacci_range():
    """Test range-limited Fibonacci."""
    result = list(fibonacci_range(5, 50))
    expected = [5, 8, 13, 21, 34]
    assert result == expected, f"Expected {expected}, got {result}"
    print("[PASS] test_fibonacci_range")


def test_fibonacci_range_from_zero():
    """Test range starting from 0."""
    result = list(fibonacci_range(0, 10))
    expected = [0, 1, 1, 2, 3, 5, 8]
    assert result == expected, f"Expected {expected}, got {result}"
    print("[PASS] test_fibonacci_range_from_zero")


def test_is_generator():
    """Test that functions return generators, not lists."""
    gen = fibonacci_generator(5)
    assert hasattr(gen, "__iter__"), "Should be iterable"
    assert hasattr(gen, "__next__"), "Should be a generator"
    print("[PASS] test_is_generator")


def test_generator_is_lazy():
    """Test that generator doesn't compute all values upfront."""
    gen = fibonacci_generator(1000000)  # Would be huge list
    first = next(gen)
    second = next(gen)
    assert first == 0 and second == 1, "Generator should yield values lazily"
    print("[PASS] test_generator_is_lazy")


def run_tests():
    print("=" * 60)
    print("FIBONACCI GENERATOR TESTS")
    print("=" * 60)

    tests = [
        test_fibonacci_generator_basic,
        test_fibonacci_generator_zero,
        test_fibonacci_generator_one,
        test_fibonacci_generator_two,
        test_fibonacci_generator_large,
        test_fibonacci_infinite,
        test_fibonacci_range,
        test_fibonacci_range_from_zero,
        test_is_generator,
        test_generator_is_lazy,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except (AssertionError, StopIteration, TypeError, Exception) as e:
            print(f"[FAIL] {test.__name__}: {e}")
            failed += 1

    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
