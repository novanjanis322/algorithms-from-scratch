"""
Unit tests for Binary Search implementations
Run with: pytest tests/test_binary_search.py -v

These tests will help verify your implementation is correct!
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from searching.binary_search import (
    binary_search_iterative,
    binary_search_recursive,
    find_first_occurrence,
    find_last_occurrence,
    find_insertion_position
)


class TestBinarySearchIterative:
    """Test iterative binary search implementation"""

    def test_found_element_middle(self):
        """Test finding element in middle of array"""
        arr = [1, 3, 5, 7, 9, 11]
        assert binary_search_iterative(arr, 5) == 2

    def test_found_element_start(self):
        """Test finding first element"""
        arr = [1, 3, 5, 7, 9, 11]
        assert binary_search_iterative(arr, 1) == 0

    def test_found_element_end(self):
        """Test finding last element"""
        arr = [1, 3, 5, 7, 9, 11]
        assert binary_search_iterative(arr, 11) == 5

    def test_not_found_smaller(self):
        """Test element smaller than all elements"""
        arr = [1, 3, 5, 7, 9]
        assert binary_search_iterative(arr, 0) == -1

    def test_not_found_larger(self):
        """Test element larger than all elements"""
        arr = [1, 3, 5, 7, 9]
        assert binary_search_iterative(arr, 10) == -1

    def test_not_found_middle(self):
        """Test element that would be in middle but doesn't exist"""
        arr = [1, 3, 5, 7, 9]
        assert binary_search_iterative(arr, 4) == -1

    def test_single_element_found(self):
        """Test array with single element - found"""
        assert binary_search_iterative([5], 5) == 0

    def test_single_element_not_found(self):
        """Test array with single element - not found"""
        assert binary_search_iterative([5], 3) == -1

    def test_empty_array(self):
        """Test empty array"""
        assert binary_search_iterative([], 5) == -1

    def test_two_elements(self):
        """Test array with two elements"""
        arr = [1, 3]
        assert binary_search_iterative(arr, 1) == 0
        assert binary_search_iterative(arr, 3) == 1
        assert binary_search_iterative(arr, 2) == -1


class TestBinarySearchRecursive:
    """Test recursive binary search implementation"""

    def test_found_element(self):
        """Test finding elements at various positions"""
        arr = [2, 4, 6, 8, 10, 12]
        assert binary_search_recursive(arr, 6) == 2
        assert binary_search_recursive(arr, 2) == 0
        assert binary_search_recursive(arr, 12) == 5

    def test_not_found(self):
        """Test element not in array"""
        arr = [1, 3, 5, 7, 9]
        assert binary_search_recursive(arr, 2) == -1
        assert binary_search_recursive(arr, 11) == -1

    def test_large_array(self):
        """Test with large array (1000 elements)"""
        arr = list(range(0, 1000, 2))  # [0, 2, 4, ..., 998]
        assert binary_search_recursive(arr, 500) == 250
        assert binary_search_recursive(arr, 501) == -1
        assert binary_search_recursive(arr, 0) == 0
        assert binary_search_recursive(arr, 998) == 499

    def test_single_element(self):
        """Test single element array"""
        assert binary_search_recursive([10], 10) == 0
        assert binary_search_recursive([10], 5) == -1


class TestFirstOccurrence:
    """Test finding first occurrence with duplicates"""

    def test_duplicates_middle(self):
        """Test finding first of multiple duplicates in middle"""
        arr = [1, 2, 2, 2, 3, 4, 5]
        assert find_first_occurrence(arr, 2) == 1

    def test_duplicates_start(self):
        """Test when duplicates are at start"""
        arr = [1, 1, 1, 2, 3]
        assert find_first_occurrence(arr, 1) == 0

    def test_duplicates_end(self):
        """Test when duplicates are at end"""
        arr = [1, 2, 3, 5, 5, 5]
        assert find_first_occurrence(arr, 5) == 3

    def test_no_duplicates(self):
        """Test with no duplicates"""
        arr = [1, 2, 3, 4, 5]
        assert find_first_occurrence(arr, 3) == 2

    def test_all_same(self):
        """Test when all elements are the same"""
        arr = [5, 5, 5, 5, 5]
        assert find_first_occurrence(arr, 5) == 0

    def test_not_found(self):
        """Test when element not in array"""
        arr = [1, 2, 2, 3]
        assert find_first_occurrence(arr, 5) == -1


class TestLastOccurrence:
    """Test finding last occurrence with duplicates"""

    def test_duplicates_middle(self):
        """Test finding last of multiple duplicates in middle"""
        arr = [1, 2, 2, 2, 3, 4, 5]
        assert find_last_occurrence(arr, 2) == 3

    def test_duplicates_start(self):
        """Test when duplicates are at start"""
        arr = [1, 1, 1, 2, 3]
        assert find_last_occurrence(arr, 1) == 2

    def test_duplicates_end(self):
        """Test when duplicates are at end"""
        arr = [1, 2, 3, 5, 5, 5]
        assert find_last_occurrence(arr, 5) == 5

    def test_single_occurrence(self):
        """Test single occurrence (should return same as first)"""
        arr = [1, 2, 3, 4, 5]
        assert find_last_occurrence(arr, 1) == 0
        assert find_last_occurrence(arr, 5) == 4

    def test_all_same(self):
        """Test when all elements are the same"""
        arr = [5, 5, 5, 5, 5]
        assert find_last_occurrence(arr, 5) == 4

    def test_not_found(self):
        """Test when element not in array"""
        arr = [1, 2, 2, 3]
        assert find_last_occurrence(arr, 7) == -1


class TestInsertionPosition:
    """Test finding insertion position"""

    def test_insert_middle(self):
        """Test inserting in middle of array"""
        arr = [1, 3, 5, 7]
        assert find_insertion_position(arr, 4) == 2

    def test_insert_beginning(self):
        """Test inserting at beginning"""
        arr = [2, 4, 6, 8]
        assert find_insertion_position(arr, 1) == 0

    def test_insert_end(self):
        """Test inserting at end"""
        arr = [1, 2, 3, 4]
        assert find_insertion_position(arr, 5) == 4

    def test_insert_duplicate(self):
        """Test inserting duplicate (should be leftmost position)"""
        arr = [1, 3, 5, 7]
        # For duplicate 5, should insert at index 2 (before existing 5)
        assert find_insertion_position(arr, 5) == 2

    def test_empty_array(self):
        """Test insertion in empty array"""
        assert find_insertion_position([], 5) == 0

    def test_single_element(self):
        """Test insertion with single element"""
        assert find_insertion_position([5], 3) == 0  # Insert before
        assert find_insertion_position([5], 7) == 1  # Insert after
        assert find_insertion_position([5], 5) == 0  # Insert at same position

    def test_all_smaller(self):
        """Test when target is larger than all elements"""
        arr = [1, 2, 3, 4, 5]
        assert find_insertion_position(arr, 10) == 5

    def test_all_larger(self):
        """Test when target is smaller than all elements"""
        arr = [5, 6, 7, 8, 9]
        assert find_insertion_position(arr, 1) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
