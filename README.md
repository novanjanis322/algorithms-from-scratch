# Algorithms From Scratch

A comprehensive collection of classic algorithms and data structures implemented in Python from scratch, with detailed explanations, complexity analysis, and unit tests.

## Purpose

This repository demonstrates deep understanding of fundamental algorithms by implementing them without relying on built-in libraries. Each implementation includes:
- Clean, readable code with type hints
- Detailed docstrings explaining the algorithm
- Time and space complexity analysis
- Unit tests using pytest
- Example usage

## Repository Structure

```
algorithms-from-scratch/
├── searching/          # Search algorithms
│   └── binary_search.py
├── sorting/            # Sorting algorithms
│   └── quick_sort.py
├── arrays/             # Array manipulation algorithms
│   ├── two_sum.py
│   └── find_duplicates.py
├── strings/            # String algorithms
│   └── valid_palindrome.py
├── linked_lists/       # Linked list operations
│   └── merge_sorted.py
├── python_concepts/    # Advanced Python patterns
│   ├── timing_decorator.py
│   ├── fibonacci_generator.py
│   ├── comprehensions_examples.py
│   ├── lambda_examples.py
│   └── custom_context_manager.py
└── tests/              # Unit tests
```

## Algorithms Implemented

### Searching
- **Binary Search** - O(log n) search in sorted arrays

### Sorting
- **Quick Sort** - O(n log n) average case divide-and-conquer sorting

### Arrays
- **Two Sum** - Finding pairs that sum to target
- **Find Duplicates** - Using hash maps efficiently

### Strings
- **Valid Palindrome** - String manipulation and two-pointer technique

### Linked Lists
- **Merge Two Sorted Lists** - Merging with O(1) space

### Advanced Python Concepts
- **Decorators** - Function wrappers and timing
- **Generators** - Memory-efficient iteration with yield
- **Comprehensions** - List/dict comprehensions
- **Lambda Functions** - Anonymous function patterns
- **Context Managers** - Custom with statement handlers

## Running Tests

```bash
# Install pytest
pip install pytest

# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_binary_search.py

# Run with verbose output
pytest -v
```
