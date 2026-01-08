"""
Test suite for Two Sum algorithm implementations.

Run with: pytest tests/test_two_sum.py -v
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from arrays.two_sum import two_sum_brute_force, two_sum_hash_map


class TestTwoSumBruteForce:
    """Tests for brute force approach."""

    def test_basic_case(self):
        assert two_sum_brute_force([2, 7, 11, 15], 9) == [0, 1]

    def test_target_at_end(self):
        assert two_sum_brute_force([1, 2, 3, 4, 5], 9) == [3, 4]

    def test_no_solution(self):
        assert two_sum_brute_force([1, 2, 3], 10) is None

    def test_empty_array(self):
        assert two_sum_brute_force([], 5) is None

    def test_single_element(self):
        assert two_sum_brute_force([5], 5) is None

    def test_negative_numbers(self):
        assert two_sum_brute_force([-1, -2, -3, -4, -5], -8) == [2, 4]

    def test_duplicate_values(self):
        assert two_sum_brute_force([3, 3], 6) == [0, 1]

    def test_zero_target(self):
        assert two_sum_brute_force([-3, 4, 3, 90], 0) == [0, 2]


class TestTwoSumHashMap:
    """Tests for hash map approach."""

    def test_basic_case(self):
        assert two_sum_hash_map([2, 7, 11, 15], 9) == [0, 1]

    def test_target_at_end(self):
        assert two_sum_hash_map([1, 2, 3, 4, 5], 9) == [3, 4]

    def test_target_at_start(self):
        assert two_sum_hash_map([5, 4, 3, 2, 1], 9) == [0, 1]

    def test_no_solution(self):
        assert two_sum_hash_map([1, 2, 3], 10) is None

    def test_empty_array(self):
        assert two_sum_hash_map([], 5) is None

    def test_single_element(self):
        assert two_sum_hash_map([5], 5) is None

    def test_negative_numbers(self):
        assert two_sum_hash_map([-1, -2, -3, -4, -5], -8) == [2, 4]

    def test_mixed_positive_negative(self):
        assert two_sum_hash_map([-10, 20, 10, -20], 0) == [0, 2]

    def test_duplicate_values(self):
        assert two_sum_hash_map([3, 3], 6) == [0, 1]

    def test_zero_target(self):
        assert two_sum_hash_map([-3, 4, 3, 90], 0) == [0, 2]

    def test_large_numbers(self):
        assert two_sum_hash_map([1000000, 999999, 1], 1000001) == [0, 2]


class TestBothMethodsAgree:
    """Verify both methods find valid solutions."""

    @pytest.mark.parametrize("nums,target", [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([-1, -2, -3, -4, -5], -8),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19),
    ])
    def test_both_find_valid_solution(self, nums, target):
        brute = two_sum_brute_force(nums, target)
        hashmap = two_sum_hash_map(nums, target)

        assert brute is not None
        assert hashmap is not None
        assert nums[brute[0]] + nums[brute[1]] == target
        assert nums[hashmap[0]] + nums[hashmap[1]] == target


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
