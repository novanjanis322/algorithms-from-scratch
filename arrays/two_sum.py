"""
Two Sum Algorithm - Implementation from Scratch

Problem: Given an array of integers and a target sum, find two numbers
such that they add up to the target. Return their indices.

Algorithm Approaches:
1. Brute Force: Check all pairs - O(n^2) time, O(1) space
2. Hash Map: Store complements - O(n) time, O(n) space (optimal)

HINTS:
- Brute force: Use nested loops, outer picks first number, inner picks second
- Hash map: complement = target - current_num
- If complement exists in hash map, we found a pair!
- Store value -> index mapping as you iterate
"""

import time
from typing import List, Optional


def timer_dec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.10f}s to execute")
        return res

    return wrapper


@timer_dec
def two_sum_brute_force(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Brute force approach: Check all pairs.

    HINT:
    - Use nested loops
    - Outer loop: i from 0 to n-1
    - Inner loop: j from i+1 to n
    - Check if nums[i] + nums[j] == target

    Args:
        nums: List of integers
        target: Target sum to find

    Returns:
        List of two indices [i, j] if found, None otherwise

    Time Complexity: O(n^2) - checking all pairs
    Space Complexity: O(1) - no extra space needed

    Example:
        nums = [2, 7, 11, 15], target = 9
        Returns [0, 1] because nums[0] + nums[1] = 2 + 7 = 9
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


@timer_dec
def two_sum_hash_map(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Hash map approach: Store seen numbers and their indices.

    HINT:
    - Create empty dict: seen = {}
    - Loop through nums with index: for i, num in enumerate(nums)
    - Calculate: complement = target - num
    - If complement in seen: return [seen[complement], i]
    - Otherwise: seen[num] = i
    - Return None if no pair found

    Args:
        nums: List of integers
        target: Target sum to find

    Returns:
        List of two indices [i, j] if found, None otherwise

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(n) - hash map stores up to n elements

    Example walkthrough:
        nums = [2, 7, 11, 15], target = 9
        - i=0, num=2: complement=7, not in {}, add {2: 0}
        - i=1, num=7: complement=2, found in {2: 0}! Return [0, 1]
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


if __name__ == "__main__":
    print("=" * 60)
    print("TWO SUM - TEST YOUR IMPLEMENTATION")
    print("=" * 60)

    # Test Case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"\nTest 1: nums={nums1}, target={target1}")
    print(f"  Brute force: {two_sum_brute_force(nums1, target1)} (expected: [0, 1])")
    print(f"  Hash map:    {two_sum_hash_map(nums1, target1)} (expected: [0, 1])")

    # Test Case 2: Target at end
    nums2 = [1, 2, 3, 4, 5]
    target2 = 9
    print(f"\nTest 2: nums={nums2}, target={target2}")
    print(f"  Brute force: {two_sum_brute_force(nums2, target2)} (expected: [3, 4])")
    print(f"  Hash map:    {two_sum_hash_map(nums2, target2)} (expected: [3, 4])")

    # Test Case 3: No solution
    nums3 = [1, 2, 3]
    target3 = 10
    print(f"\nTest 3: nums={nums3}, target={target3}")
    print(f"  Brute force: {two_sum_brute_force(nums3, target3)} (expected: None)")
    print(f"  Hash map:    {two_sum_hash_map(nums3, target3)} (expected: None)")

    # Test Case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    print(f"\nTest 4: nums={nums4}, target={target4}")
    print(f"  Brute force: {two_sum_brute_force(nums4, target4)} (expected: [2, 4])")
    print(f"  Hash map:    {two_sum_hash_map(nums4, target4)} (expected: [2, 4])")

    # Test Case 5: Duplicate values
    nums5 = [3, 3]
    target5 = 6
    print(f"\nTest 5: nums={nums5}, target={target5}")
    print(f"  Brute force: {two_sum_brute_force(nums5, target5)} (expected: [0, 1])")
    print(f"  Hash map:    {two_sum_hash_map(nums5, target5)} (expected: [0, 1])")

    # Test Case 6: Empty array
    nums6 = []
    target6 = 5
    print(f"\nTest 6: nums={nums6}, target={target6}")
    print(f"  Brute force: {two_sum_brute_force(nums6, target6)} (expected: None)")
    print(f"  Hash map:    {two_sum_hash_map(nums6, target6)} (expected: None)")

    # Test Case 7: Zero target
    nums7 = [-3, 4, 3, 90]
    target7 = 0
    print(f"\nTest 7: nums={nums7}, target={target7}")
    print(f"  Brute force: {two_sum_brute_force(nums7, target7)} (expected: [0, 2])")
    print(f"  Hash map:    {two_sum_hash_map(nums7, target7)} (expected: [0, 2])")

    print("\n" + "=" * 60)
