# 304. Range Sum Query 2D – Immutable

## Problem Statement

Given a 2D matrix `matrix`, handle multiple queries of the form:

```text
sumRegion(row1, col1, row2, col2)
```

Return the sum of all elements inside the rectangle defined by:

- Top-left corner → `(row1, col1)`
- Bottom-right corner → `(row2, col2)`

The matrix never changes after initialization.

Since multiple queries will be asked, the goal is to make each query as fast as possible.

---

## Example

### Input

```text
matrix =

[
 [3,0,1,4,2],
 [5,6,3,2,1],
 [1,2,0,1,5],
 [4,1,0,1,7],
 [1,0,3,0,5]
]

sumRegion(2,1,4,3)
```

### Output

```text
8
```

### Explanation

The rectangle contains:

```text
2 0 1
1 0 1
0 3 0
```

Sum

```text
2 + 0 + 1 + 1 + 0 + 1 + 0 + 3 + 0 = 8
```

---

## LeetCode Link

https://leetcode.com/problems/range-sum-query-2d-immutable/

---

# My Learning Journey

Initially, I thought this problem would be exactly like **1D Prefix Sum**.

In 1D, every prefix value stores:

```text
Sum from index 0 → i
```

So naturally, I assumed that while traversing the matrix row by row,

the prefix value at a cell should contain the cumulative sum of everything visited before it.

For example,

```text
1 2 3
4 5 6
7 8 9
```

I thought the prefix value at `5` should be:

```text
1 + 2 + 3 + 4 + 5 = 15
```

This was my biggest misconception.

Then I realized that 2D Prefix Sum is not based on traversal order.

It is based on **rectangles**.

The prefix value at every cell represents the sum of the rectangle from the **top-left corner** to the current cell.

So for the value `5`, the correct prefix is:

```text
1 + 2
4 + 5

= 12
```

That completely changed how I visualized the pattern.

---

# Key Observation 1

A 2D Prefix Sum stores the sum of a rectangle.

For every cell,

imagine drawing a rectangle from the top-left corner.

Example:

```text
1 2 3
4 5 6
7 8 9
```

Standing at `5`,

the stored rectangle is:

```text
+-------+
| 1 | 2 |
|-------|
| 4 | 5 |
+-------+
```

So

```text
Prefix = 12
```

The prefix does **not** depend on the order in which we visit cells.

It depends on the rectangle ending at that cell.

---

# Key Observation 2

While building the Prefix Matrix,

every cell receives information from:

- Above
- Left
- Current Cell

If we simply add:

```text
Above + Left + Current
```

we accidentally count the **top-left rectangle twice**.

Example:

```text
1 2
4 5
```

Above:

```text
1 2
```

Left:

```text
1
4
```

The value `1` appears in both.

Therefore,

we subtract the overlapping rectangle once.

This gives the construction formula:

```python
prefix[row][col] =
current
+ above
+ left
- overlap
```

---

# Biggest Realization

The formula is not something to memorize.

It comes naturally from the Inclusion-Exclusion Principle.

Whenever we combine:

```text
Above

+

Left
```

the top-left rectangle gets counted twice.

Subtracting the overlap fixes the double counting.

Understanding **why** the overlap exists made the formula easy to remember forever.

---

# Why Do We Create an Extra Row and Column?

Initially I wondered why every solution creates:

```python
prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
```

instead of

```python
prefix = [[0] * cols for _ in range(rows)]
```

The extra row and column are filled with zeros.

This eliminates all boundary checks.

Every real cell always has:

- Above
- Left
- Top-left

even for the first row and first column.

This keeps the implementation clean without writing special cases.

---

# Why Use `row - 1` and `col - 1`?

The Prefix Matrix has one extra row and one extra column.

So,

```text
prefix[1][1]
```

actually represents

```text
matrix[0][0]
```

Therefore,

every time we access the original matrix,

we shift by one:

```python
matrix[row - 1][col - 1]
```

---

# Query Formula

After building the Prefix Matrix,

each query can be answered using four rectangles.

Start with the largest rectangle.

```text
prefix[row2][col2]
```

Remove everything above.

```text
prefix[row1-1][col2]
```

Remove everything on the left.

```text
prefix[row2][col1-1]
```

The top-left rectangle gets removed twice,

so we add it back.

```text
prefix[row1-1][col1-1]
```

This gives:

```python
Big Rectangle
- Top Rectangle
- Left Rectangle
+ Overlap
```

---

# Memory Trick

Instead of memorizing coordinates,

I learned to ask four questions.

**1. Which rectangle already contains my answer?**

```text
(row2, col2)
```

**2. Remove everything above.**

Only the row changes.

```text
(row1-1, col2)
```

**3. Remove everything on the left.**

Only the column changes.

```text
(row2, col1-1)
```

**4. Add back the overlap.**

Both row and column change.

```text
(row1-1, col1-1)
```

Thinking about changing boundaries instead of memorizing coordinates made the query formula much easier.

---

# Pattern Used

## 2D Prefix Sum

Instead of storing cumulative sums in one dimension,

we store the cumulative sum of every rectangle from the top-left corner.

This allows every rectangle query to be answered in constant time.

---

# Optimized Solution

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):

                self.prefix[row][col] = (
                    matrix[row - 1][col - 1]
                    + self.prefix[row - 1][col]
                    + self.prefix[row][col - 1]
                    - self.prefix[row - 1][col - 1]
                )

    def sumRegion(self, row1: int, col1: int,
                  row2: int, col2: int) -> int:

        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        return (
            self.prefix[row2][col2]
            - self.prefix[row1 - 1][col2]
            - self.prefix[row2][col1 - 1]
            + self.prefix[row1 - 1][col1 - 1]
        )
```

---

# Dry Run

Suppose

```text
1 2
3 4
```

The Prefix Matrix becomes

```text
0 0 0

0 1 3

0 4 10
```

Now suppose we want the rectangle

```text
2
4
```

The answer is computed using

```text
Big Rectangle

-

Top Rectangle

-

Left Rectangle

+

Overlap
```

No iteration is required.

Only four Prefix values are accessed.

---

# Complexity Analysis

## Initialization

Every matrix cell is processed once.

```text
O(rows × cols)
```

---

## Query

Only four Prefix values are used.

```text
O(1)
```

---

## Space Complexity

The Prefix Matrix stores one value for every cell.

```text
O(rows × cols)
```

---

# Key Takeaways

- 2D Prefix Sum stores rectangle sums, not traversal sums.
- Every Prefix value represents the rectangle from the top-left corner.
- The construction formula comes from Inclusion-Exclusion.
- Padding with one extra row and column removes boundary checks.
- Rectangle queries are answered using four Prefix values.
- Think about changing boundaries instead of memorizing coordinates.

---

# Concepts Practiced

✅ Matrices

✅ Matrix Traversal

✅ 2D Prefix Sum

✅ Inclusion-Exclusion Principle

✅ Rectangle Sum Queries

✅ Dynamic Preprocessing

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| 2D Prefix Sum | O(rows × cols) preprocessing, O(1) per query | O(rows × cols) |

---

# Status

✅ Solved

✅ Understood the difference between 1D and 2D Prefix Sum

✅ Learned to think in rectangles instead of traversal order

✅ Derived the construction formula using Inclusion-Exclusion instead of memorizing it

✅ Understood why padding removes boundary checks

✅ Learned how rectangle queries are answered using four Prefix values

✅ Successfully mastered the 2D Prefix Sum pattern
