# Count Negative Numbers in a Sorted Matrix

## Problem Statement

Given a matrix `grid` sorted in non-increasing order both row-wise and column-wise, return the total number of negative numbers in the matrix.

---

## Example

### Input

```python
grid = [
    [4,3,2,-1],
    [3,2,1,-1],
    [1,1,-1,-2],
    [-1,-1,-2,-3]
]
```

### Output

```python
8
```

### Explanation

Negative numbers are:

```text
-1
-1
-1
-2
-1
-1
-2
-3
```

Total:

```python
8
```

---

## LeetCode Link

https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

---

# My Initial Thought Process

The most straightforward approach is:

1. Visit every element in the matrix.
2. Count how many are negative.

This works, but ignores the fact that the matrix is sorted.


# Brute Force Solution

```python
count = 0

for row in grid:
    for num in row:
        if num < 0:
            count += 1
```

### Time Complexity

```text
O(m × n)
```

### Space Complexity

```text
O(1)
```

---

# Key Observation

Each row is sorted in decreasing order.

Example:

```python
[5,3,1,-2,-4,-7]
```

Notice:

```text
Positive Positive Positive Negative Negative Negative
```

Once we find the first negative number:

```python
-2
```

every number to its right is also negative.

This suggests Binary Search.

---

# Binary Search Idea

Instead of checking every element:

Find the index of the first negative number in each row.

Example:

```python
[5,3,1,-2,-4,-7]
```

First negative:

```python
index = 3
```

Number of negatives:

```python
len(row) - index
```

```python
6 - 3 = 3
```

---

# Optimized Solution

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:

            left = 0
            right = len(row) - 1
            answer = -1

            while left <= right:

                mid = (left + right) // 2

                if row[mid] < 0:
                    answer = mid
                    right = mid - 1

                else:
                    left = mid + 1

            if answer == -1:
                total_negatives_of_row = 0
            else:
                total_negatives_of_row = len(row) - answer

            count += total_negatives_of_row

        return count
```

---

# Dry Run

### Row

```python
[5,3,1,-2,-4,-7]
```

Initially:

```python
left = 0
right = 5
```

---

### Iteration 1

```python
mid = 2
row[mid] = 1
```

Positive.

Move right:

```python
left = mid + 1
```

```python
left = 3
```

---

### Iteration 2

```python
mid = 4
row[mid] = -4
```

Negative.

Store answer:

```python
answer = 4
```

Search left side:

```python
right = 3
```

---

### Iteration 3

```python
mid = 3
row[mid] = -2
```

Negative.

Update:

```python
answer = 3
```

Search further left:

```python
right = 2
```

Loop ends.

---

First negative index:

```python
3
```

Negative count:

```python
6 - 3 = 3
```

---

# Why Binary Search Works

Binary Search is useful whenever we need to find a boundary.

Here the boundary is:

```text
Positive Numbers | Negative Numbers
```

Example:

```python
[5,3,1,-2,-4,-7]
```

```text
+ + + | - - -
```

We are searching for:

```text
First Negative Number
```

---

# Complexity Analysis

Let:

```text
m = number of rows
n = number of columns
```

---

## Time Complexity

Binary Search per row:

```text
O(log n)
```

For all rows:

```text
O(m log n)
```

---

## Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Pattern Learned

## Binary Search on Boundary

Instead of searching for an exact value:

```text
Find the first element satisfying a condition.
```

Examples:

- First Negative Number
- First Positive Number
- First Occurrence
- Lower Bound
- Upper Bound

---

## Sorted Array / Matrix Optimization

Whenever a problem says:

```text
sorted
```

ask:

```text
Can Binary Search help?
```

Often the answer is yes.

---

# Key Takeaways

- Always read problem constraints carefully.
- Use sorting information to reduce unnecessary work.
- Binary Search is not only for finding exact values.
- Boundary-searching is a powerful pattern.

---

# Concepts Practiced

✅ Arrays

✅ 2D Arrays

✅ Binary Search

✅ Boundary Search Pattern

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|-----------|--------|--------|
| Brute Force | O(m × n) | O(1) |
| Binary Search | O(m log n) | O(1) |

---

## Status

✅ Solved

✅ Learned Binary Search Boundary Pattern

✅ Learned Sorted Matrix Optimization

✅ Understood Brute Force vs Optimized Approach
