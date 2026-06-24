# Special Positions in a Binary Matrix

## Problem Statement

Given an `m x n` binary matrix `mat`, return the number of special positions in the matrix.

A position `(i, j)` is considered special if:

- `mat[i][j] == 1`
- All other elements in row `i` are `0`
- All other elements in column `j` are `0`

In simple words:

```text
A special position is a 1 that is the only 1
in both its row and its column.
```

---

## Example

### Input

```python
mat = [
    [1,0,0],
    [0,0,1],
    [1,0,0]
]
```

### Output

```python
1
```

### Explanation

Position:

```python
mat[1][2]
```

is special because:

Row 1:

```python
[0,0,1]
```

contains exactly one `1`.

Column 2:

```python
[0,1,0]
```

contains exactly one `1`.

Therefore:

```python
count = 1
```

---

## LeetCode Link

https://leetcode.com/problems/special-positions-in-a-binary-matrix/

---

# My Initial Thought Process

For a position to be special:

```text
Cell must contain 1
AND
Row must contain exactly one 1
AND
Column must contain exactly one 1
```

The first idea is:

For every cell containing `1`:

- Check its entire row
- Check its entire column

But this repeatedly scans the same rows and columns.

We can do better.

---

# Key Observation

Instead of checking rows and columns repeatedly:

Let's calculate:

```python
row_sums[i]
```

which stores:

```text
Number of 1s in row i
```

and:

```python
col_sums[j]
```

which stores:

```text
Number of 1s in column j
```

Once these are computed, checking whether a position is special becomes very easy.

---

# Approach

## Pass 1

Count:

```python
row_sums
```

and

```python
col_sums
```

for the entire matrix.

---

## Pass 2

Visit every cell again.

If:

```python
mat[i][j] == 1
```

and

```python
row_sums[i] == 1
```

and

```python
col_sums[j] == 1
```

then:

```python
count += 1
```

---

# Solution

```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        row_sums = [0] * rows
        col_sums = [0] * cols

        for i in range(rows):
            for j in range(cols):
                row_sums[i] += mat[i][j]
                col_sums[j] += mat[i][j]

        count = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    count += 1

        return count
```

---

# Dry Run

### Input

```python
mat = [
    [1,0,0],
    [0,0,1],
    [1,0,0]
]
```

---

## First Pass

Compute row sums:

```python
row_sums = [1,1,1]
```

Compute column sums:

```python
col_sums = [2,0,1]
```

---

## Second Pass

Check:

```python
mat[0][0]
```

```python
1
```

Row count:

```python
row_sums[0] = 1
```

Column count:

```python
col_sums[0] = 2
```

Not special.

---

Check:

```python
mat[1][2]
```

```python
1
```

Row count:

```python
1
```

Column count:

```python
1
```

Special.

```python
count += 1
```

---

Final Answer:

```python
1
```

---

# Python Concepts Learned

## Creating an Array of Fixed Size

```python
row_sums = [0] * rows
```

Example:

```python
[0,0,0,0]
```

---

## Matrix Traversal

```python
for i in range(rows):
    for j in range(cols):
```

Used to visit every element in a 2D matrix.

---

## Counting Frequencies

```python
row_sums[i] += mat[i][j]
```

Stores the total number of `1`s in each row.

Similarly:

```python
col_sums[j] += mat[i][j]
```

stores the total number of `1`s in each column.

---

# Complexity Analysis

Let:

```text
m = number of rows
n = number of columns
```

---

## Time Complexity

First Pass:

```text
O(m × n)
```

Second Pass:

```text
O(m × n)
```

Total:

```text
O(m × n)
```

---

## Space Complexity

Arrays used:

```python
row_sums
col_sums
```

Space:

```text
O(m + n)
```

---

# Alternative Solutions

## Brute Force

For every cell containing `1`:

- Scan entire row
- Scan entire column

Time Complexity:

```text
O(m × n × (m + n))
```

Very inefficient.

---

## Optimized Solution (Used Here)

Precompute:

```python
row_sums
col_sums
```

once and reuse them.

Time Complexity:

```text
O(m × n)
```

Much better.

---

# Pattern Learned

## Precompute and Reuse

Instead of repeatedly calculating information:

```text
Compute once
Store it
Reuse it
```

This is a common DSA pattern.

Examples:

- Prefix Sum
- Hash Maps
- Frequency Arrays
- Dynamic Programming

---

# Key Takeaways

- Avoid recomputing the same information repeatedly.
- Precomputing often reduces time complexity significantly.
- Row and column counting is a common matrix technique.
- Think about what information can be stored and reused.

---

# Concepts Practiced

✅ Arrays

✅ 2D Arrays

✅ Matrix Traversal

✅ Counting Frequencies

✅ Precomputation

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Metric | Complexity |
|----------|----------|
| Time Complexity | O(m × n) |
| Space Complexity | O(m + n) |

---

## Status

✅ Solved

✅ Learned Matrix Traversal

✅ Learned Row and Column Counting

✅ Learned Precompute-and-Reuse Pattern

✅ Understood Optimized vs Brute Force Approach
