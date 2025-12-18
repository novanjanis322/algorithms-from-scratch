"""
Binary Search Algorithm - Implementation from Scratch

Algorithm Overview:
Binary search is an efficient algorithm for finding a target value within
a sorted array. It works by repeatedly dividing the search interval in half.

Time Complexity: O(log n) - each iteration cuts search space in half
Space Complexity: O(1) for iterative, O(log n) for recursive (call stack)

HINTS:
- Start with left=0, right=len(arr)-1
- Calculate mid = left + (right - left) // 2  (avoids overflow)
- If arr[mid] == target: found it!
- If arr[mid] < target: search right half (left = mid + 1)
- If arr[mid] > target: search left half (right = mid - 1)
- Stop when left > right (not found)
"""

from typing import List, Optional


def binary_search_iterative(arr: List[int], target: int) -> int:
    """
    Iterative implementation of binary search.

    HINT: Use a while loop with left <= right condition

    Args:
        arr: Sorted list of integers
        target: Value to search for

    Returns:
        Index of target if found, -1 otherwise

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(
    arr: List[int], target: int, left: int = 0, right: Optional[int] = None
) -> int:
    """
    Recursive implementation of binary search.

    HINT:
    - Base case: if left > right, return -1
    - Recursive case: call yourself with updated left or right

    Args:
        arr: Sorted list of integers
        target: Value to search for
        left: Left boundary (default 0)
        right: Right boundary (default len(arr) - 1)

    Returns:
        Index of target if found, -1 otherwise

    Time Complexity: O(log n)
    Space Complexity: O(log n) - recursive call stack
    """
    left = 0 if left is None else left
    right = len(arr) - 1 if right is None else right
    if not arr:
        return -1
    if left > right:
        return -1
    mid = left + (right -left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def find_first_occurrence(arr: List[int], target: int) -> int:
    """
    Find the FIRST occurrence of target in sorted array with duplicates.

    HINT:
    - Similar to regular binary search
    - When you find target, save the index BUT continue searching LEFT
    - Set right = mid - 1 to keep searching for earlier occurrence

    Args:
        arr: Sorted list (may contain duplicates)
        target: Value to search for

    Returns:
        Index of first occurrence, -1 if not found

    Example:
        [1, 2, 2, 2, 3, 4] target=2 -> should return 1 (first 2)
    """
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1
    first_index = -1
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == target:
            first_index = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_index


def find_last_occurrence(arr: List[int], target: int) -> int:
    """
    Find the LAST occurrence of target in sorted array with duplicates.

    HINT:
    - Similar to find_first_occurrence but opposite
    - When you find target, continue searching RIGHT
    - Set left = mid + 1 to keep searching for later occurrence

    Args:
        arr: Sorted list (may contain duplicates)
        target: Value to search for

    Returns:
        Index of last occurrence, -1 if not found

    Example:
        [1, 2, 2, 2, 3, 4] target=2 -> should return 3 (last 2)
    """
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1
    last_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            last_index = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_index


def find_insertion_position(arr: List[int], target: int) -> int:
    """
    Find the position where target should be inserted to maintain sorted order.

    HINT:
    - Similar to binary search but no exact match needed
    - When arr[mid] < target: go right (left = mid + 1)
    - When arr[mid] >= target: go left (right = mid - 1)
    - Return 'left' at the end (it will be the insertion position)

    Args:
        arr: Sorted list of integers
        target: Value to insert

    Returns:
        Index where target should be inserted

    Example:
        [1, 3, 5, 7] target=4 -> should return 2 (insert between 3 and 5)
    """
    left = 0 
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left



if __name__ == "__main__":
    print("=" * 60)
    print("BINARY SEARCH - TEST YOUR IMPLEMENTATION")
    print("=" * 60)

    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"\nArray: {arr}")

    # Test 1: Iterative Binary Search
    print("\n1️⃣ Testing Iterative Binary Search:")
    print(f"   Search 7: {binary_search_iterative(arr, 7)} (expected: 3)")
    print(f"   Search 10: {binary_search_iterative(arr, 10)} (expected: -1)")
    print(f"   Search 1: {binary_search_iterative(arr, 1)} (expected: 0)")
    print(f"   Search 15: {binary_search_iterative(arr, 15)} (expected: 7)")

    # Test 2: Recursive Binary Search
    print("\n2️⃣ Testing Recursive Binary Search:")
    print(f"   Search 13: {binary_search_recursive(arr, 13)} (expected: 6)")
    print(f"   Search 2: {binary_search_recursive(arr, 2)} (expected: -1)")

    # Test 3: Find first/last occurrence
    arr_dup = [1, 2, 2, 2, 3, 4, 5]
    print(f"\n3️⃣ Testing with duplicates: {arr_dup}")
    print(
        f"   First occurrence of 2: {find_first_occurrence(arr_dup, 2)} (expected: 1)"
    )
    print(f"   Last occurrence of 2: {find_last_occurrence(arr_dup, 2)} (expected: 3)")
    print(
        f"   First occurrence of 5: {find_first_occurrence(arr_dup, 5)} (expected: 6)"
    )
    print(f"   Last occurrence of 1: {find_last_occurrence(arr_dup, 1)} (expected: 0)")

    # Test 4: Insertion position
    print("\n4️⃣ Testing Insertion Position:")
    print(f"   Insert 4 in {arr}: {find_insertion_position(arr, 4)} (expected: 2)")
    print(f"   Insert 0 in {arr}: {find_insertion_position(arr, 0)} (expected: 0)")
    print(f"   Insert 20 in {arr}: {find_insertion_position(arr, 20)} (expected: 8)")
    print(f"   Insert 7 in {arr}: {find_insertion_position(arr, 7)} (expected: 3)")

    print("\n" + "=" * 60)
