"""
Python Comprehensions
=====================
Learn: List, dict, and set comprehensions for concise data transformations.

Your task: Implement each function using ONLY comprehensions (no loops).
"""

from typing import Dict, List, Set

# =============================================================================
# LIST COMPREHENSIONS
# =============================================================================


def squares(n: int) -> List[int]:
    """
    Return squares of numbers 1 to n.

    Example:
        squares(5) -> [1, 4, 9, 16, 25]
    """

    return [i**2 for i in range(1, n + 1)]


def even_squares(n: int) -> List[int]:
    """
    Return squares of even numbers from 1 to n.

    Example:
        even_squares(10) -> [4, 16, 36, 64, 100]
    """
    print(n)
    return [i**2 for i in range(1, n + 1) if i % 2 == 0]


def flatten(nested: List[List[int]]) -> List[int]:
    """
    Flatten a 2D list into 1D.

    Example:
        flatten([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]
    """
    return [item for sublist in nested for item in sublist]


def words_longer_than(sentences: List[str], min_length: int) -> List[str]:
    """
    Extract words longer than min_length from sentences.

    Example:
        words_longer_than(["hello world", "python is great"], 4)
        -> ["hello", "world", "python", "great"]
    """
    return [
        word
        for sentence in sentences
        for word in sentence.split()
        if len(word) > min_length
    ]


# =============================================================================
# DICT COMPREHENSIONS
# =============================================================================


def square_dict(n: int) -> Dict[int, int]:
    """
    Create dict mapping numbers to their squares.

    Example:
        square_dict(5) -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """
    return {i: i**2 for i in range(1, n + 1)}


def invert_dict(d: Dict[str, int]) -> Dict[int, str]:
    """
    Swap keys and values in a dictionary.

    Example:
        invert_dict({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    """
    return {v: k for k, v in d.items()}
    pass


def word_lengths(words: List[str]) -> Dict[str, int]:
    """
    Map each word to its length.

    Example:
        word_lengths(["cat", "elephant", "dog"]) -> {"cat": 3, "elephant": 8, "dog": 3}
    """
    return {word: len(word) for word in words}
    pass


def filter_dict(d: Dict[str, int], min_value: int) -> Dict[str, int]:
    """
    Keep only entries where value >= min_value.

    Example:
        filter_dict({"a": 1, "b": 5, "c": 3}, 3) -> {"b": 5, "c": 3}
    """
    return {k: v for k, v in d.items() if v >= min_value}


# =============================================================================
# SET COMPREHENSIONS
# =============================================================================


def unique_lengths(words: List[str]) -> Set[int]:
    """
    Return set of unique word lengths.

    Example:
        unique_lengths(["cat", "dog", "elephant", "rat"]) -> {3, 8}
    """
    return set(len(x) for x in words)
    pass


def common_elements(list1: List[int], list2: List[int]) -> Set[int]:
    """
    Find elements present in both lists.

    Example:
        common_elements([1, 2, 3, 4], [3, 4, 5, 6]) -> {3, 4}
    """
    return set(x for x in list1 if x in list2)
    pass


# =============================================================================
# ADVANCED: NESTED & CONDITIONAL
# =============================================================================


def matrix_transpose(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transpose a matrix using comprehension.

    Example:
        matrix_transpose([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
    """

    return [list(row) for row in zip(*matrix)]
    # Hint: [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    # Or simpler: [list(row) for row in zip(*matrix)]
    pass


def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    """
    Group words by their length.

    Example:
        group_by_length(["cat", "dog", "elephant", "rat", "bird"])
        -> {3: ["cat", "dog", "rat"], 8: ["elephant"], 4: ["bird"]}

    Note: This is tricky with pure comprehensions.
          You may need to get unique lengths first.
    """
    return {
        length: [w for w in words if len(w) == length]
        for length in set(map(len, words))
    }
    # Hint: {length: [w for w in words if len(w) == length] for length in set(map(len, words))}
    pass


# =============================================================================
# TEST DATA
# =============================================================================

SAMPLE_SENTENCES = [
    "the quick brown fox",
    "jumps over the lazy dog",
    "python programming is fun",
]

SAMPLE_MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

SAMPLE_WORDS = ["apple", "bat", "cat", "dolphin", "elephant", "fox", "go"]


# =============================================================================
# TESTS
# =============================================================================


def test_squares():
    assert squares(5) == [1, 4, 9, 16, 25], f"Got {squares(5)}"
    assert squares(1) == [1], f"Got {squares(1)}"
    assert squares(0) == [], f"Got {squares(0)}"
    print("[PASS] test_squares")


def test_even_squares():
    assert even_squares(10) == [4, 16, 36, 64, 100], f"Got {even_squares(10)}"
    assert even_squares(5) == [4, 16], f"Got {even_squares(5)}"
    print("[PASS] test_even_squares")


def test_flatten():
    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([[1], [2], [3]]) == [1, 2, 3]
    assert flatten([[], [1], []]) == [1]
    print("[PASS] test_flatten")


def test_words_longer_than():
    result = words_longer_than(["hello world", "hi"], 3)
    assert result == ["hello", "world"], f"Got {result}"
    print("[PASS] test_words_longer_than")


def test_square_dict():
    assert square_dict(3) == {1: 1, 2: 4, 3: 9}
    assert square_dict(0) == {}
    print("[PASS] test_square_dict")


def test_invert_dict():
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({}) == {}
    print("[PASS] test_invert_dict")


def test_word_lengths():
    result = word_lengths(["cat", "elephant"])
    assert result == {"cat": 3, "elephant": 8}, f"Got {result}"
    print("[PASS] test_word_lengths")


def test_filter_dict():
    result = filter_dict({"a": 1, "b": 5, "c": 3}, 3)
    assert result == {"b": 5, "c": 3}, f"Got {result}"
    print("[PASS] test_filter_dict")


def test_unique_lengths():
    result = unique_lengths(["cat", "dog", "elephant", "rat"])
    assert result == {3, 8}, f"Got {result}"
    print("[PASS] test_unique_lengths")


def test_common_elements():
    result = common_elements([1, 2, 3, 4], [3, 4, 5, 6])
    assert result == {3, 4}, f"Got {result}"
    print("[PASS] test_common_elements")


def test_matrix_transpose():
    result = matrix_transpose([[1, 2, 3], [4, 5, 6]])
    assert result == [[1, 4], [2, 5], [3, 6]], f"Got {result}"
    print("[PASS] test_matrix_transpose")


def test_group_by_length():
    result = group_by_length(["cat", "dog", "elephant", "rat", "bird"])
    expected = {3: ["cat", "dog", "rat"], 8: ["elephant"], 4: ["bird"]}
    assert result == expected, f"Got {result}"
    print("[PASS] test_group_by_length")


def run_tests():
    print("=" * 60)
    print("COMPREHENSIONS TESTS")
    print("=" * 60)

    tests = [
        test_squares,
        test_even_squares,
        test_flatten,
        test_words_longer_than,
        test_square_dict,
        test_invert_dict,
        test_word_lengths,
        test_filter_dict,
        test_unique_lengths,
        test_common_elements,
        test_matrix_transpose,
        test_group_by_length,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except (AssertionError, TypeError, Exception) as e:
            print(f"[FAIL] {test.__name__}: {e}")
            failed += 1

    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
