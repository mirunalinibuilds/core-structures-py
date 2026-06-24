# Transpose Matrix

## Problem Statement

Given a 2D integer matrix `matrix`, return the transpose of the matrix.

The transpose of a matrix is obtained by converting all rows into columns and all columns into rows.

In simple words:

```text
Swap rows and columns.
```

---

## Example 1

### Input

```python
matrix = [
    [1,2,3],
    [4,5,6]
]
```

### Output

```python
[
    [1,4],
    [2,5],
    [3,6]
]
```

---

### Visualization

Original Matrix:

```text
1 2 3
4 5 6
```

Transposed Matrix:

```text
1 4
2 5
3 6
```

Notice:

```text
Rows become columns.
Columns become rows.
```

---

## LeetCode Link

https://leetcode.com/problems/transpose-matrix/

---

# My Initial Thought Process

The transpose operation moves every element from:

```python
matrix[i][j]
```

to:

```python
result[j][i]
```

The row index and column index simply swap places.

Example:

```python
matrix[0][1] = 2
```

moves to:

```python
result[1][0] = 2
```

This observation is the entire solution.

---

# Key Observation

For every element:

```python
matrix[i][j]
```

the new position becomes:

```python
transpose[j][i]
```

Formula:

```python
result[j][i] = matrix[i][j]
```

---

# Approach

### Step 1

Find the dimensions of the original matrix.

```python
rows = len(matrix)
cols = len(matrix[0])
```

---

### Step 2

Create an empty result matrix.

Notice:

```text
Original Size = rows × cols
Transposed Size = cols × rows
```

Therefore:

```python
result = [[0] * rows for _ in range(cols)]
```

---

### Step 3

Traverse every element.

```python
for i in range(rows):
    for j in range(cols):
```

---

### Step 4

Place the element in its transposed position.

```python
result[j][i] = matrix[i][j]
```

---

# Solution

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        result = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]

        return result
```

---

# Dry Run

### Input

```python
matrix = [
    [1,2,3],
    [4,5,6]
]
```

---

### Create Result Matrix

```python
result = [
    [0,0],
    [0,0],
    [0,0]
]
```

---

### i = 0, j = 0

```python
result[0][0] = matrix[0][0]
```

```python
1
```

Result:

```python
[
    [1,0],
    [0,0],
    [0,0]
]
```

---

### i = 0, j = 1

```python
result[1][0] = matrix[0][1]
```

```python
2
```

Result:

```python
[
    [1,0],
    [2,0],
    [0,0]
]
```

---

### i = 0, j = 2

```python
result[2][0] = matrix[0][2]
```

```python
3
```

Result:

```python
[
    [1,0],
    [2,0],
    [3,0]
]
```

---

### Continue for second row

Final Result:

```python
[
    [1,4],
    [2,5],
    [3,6]
]
```

---

# Python Concepts Learned

## Creating a 2D Matrix

```python
result = [[0] * rows for _ in range(cols)]
```

Creates:

```python
[
    [0,0],
    [0,0],
    [0,0]
]
```

---

## Matrix Traversal

```python
for i in range(rows):
    for j in range(cols):
```

Visits every element exactly once.

---

## Index Transformation

```python
result[j][i] = matrix[i][j]
```

This is the most important concept in this problem.

```text
(i,j)
 ↓
(j,i)
```

---

# Alternative Pythonic Solution

Python provides a built-in shortcut:

```python
return [list(row) for row in zip(*matrix)]
```

Explanation:

```python
zip(*matrix)
```

converts rows into columns.

Example:

```python
matrix = [
    [1,2,3],
    [4,5,6]
]
```

becomes:

```python
[
    (1,4),
    (2,5),
    (3,6)
]
```

Converting tuples to lists gives:

```python
[
    [1,4],
    [2,5],
    [3,6]
]
```

Although shorter, the manual solution teaches the actual transpose logic.

---

# Complexity Analysis

Let:

```text
m = number of rows
n = number of columns
```

---

## Time Complexity

Every element is visited once.

```text
O(m × n)
```

---

## Space Complexity

A new matrix is created.

```text
O(m × n)
```

---

# Pattern Learned

## Index Swapping

Transpose is one of the simplest examples of index transformation.

```python
matrix[i][j]
```

becomes:

```python
result[j][i]
```

Many future matrix problems use a similar idea:

- Rotate Image
- Spiral Matrix
- Set Matrix Zeroes
- Game of Life

---

# Key Takeaways

- Rows become columns.
- Columns become rows.
- The transpose operation swaps indices.
- Matrix dimensions change from:

```text
rows × cols
```

to:

```text
cols × rows
```

- Understanding index movement is more important than memorizing code.

---

# Concepts Practiced

✅ Arrays

✅ 2D Arrays

✅ Matrix Traversal

✅ Matrix Construction

✅ Index Transformation

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Metric | Complexity |
|----------|----------|
| Time Complexity | O(m × n) |
| Space Complexity | O(m × n) |

---

## Status

✅ Solved

✅ Learned Matrix Transpose

✅ Learned Index Swapping

✅ Learned 2D Matrix Construction

✅ Understood Pythonic Alternative Solution
