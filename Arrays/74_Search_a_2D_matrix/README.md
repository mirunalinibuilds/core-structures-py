# 74. Search a 2D Matrix

## Problem Statement

You are given an `m x n` integer matrix with the following properties:

* Each row is sorted in **non-decreasing order**.
* The **first integer of each row is greater than the last integer of the previous row**.

Given an integer `target`, return **true** if the target exists in the matrix, otherwise return **false**.

You must write a solution with **O(log(m × n))** time complexity.

---

## Example

**Input**

```text
matrix = [
  [1,3,5,7],
  [10,11,16,20],
  [23,30,34,60]
]

target = 3
```

**Output**

```text
true
```

---

## LeetCode Link

https://leetcode.com/problems/search-a-2d-matrix/

---

# My Learning Journey

My first thought was to solve it using **Brute Force**.

I simply traversed every row and every element until I found the target.

Although it worked, I knew it wasn't optimal.

Then I noticed that **each row is sorted**, so I improved my approach by performing **Binary Search on every row**.

That reduced the complexity from:

```text
O(m × n)
```

to

```text
O(m log n)
```

At this point, I thought I had solved the problem.

But then I noticed something interesting in the problem statement.

---

# Biggest Clue

The problem didn't just say:

> Each row is sorted.

It also said:

> The first element of every row is greater than the last element of the previous row.

Initially, I ignored this line.

Then I realized:

The problem setter included this for a reason.

---

# Key Observation 1

Consider this matrix:

```text
1   3   5

7   9  11

13 15 17
```

If we imagine writing every element in one line:

```text
1 3 5 7 9 11 13 15 17
```

the order does **not change**.

The matrix behaves exactly like one large sorted array.

The important realization was:

**We don't actually flatten the matrix.**

We only **pretend** it is a single sorted array.

---

# Key Observation 2

Binary Search gives us an imaginary index.

Suppose:

```text
mid = 5
```

How do we know which element this represents inside the matrix?

This was the part that initially confused me.

Then I learned the mapping.

If the matrix has:

```text
cols columns
```

then

```python
row = mid // cols
col = mid % cols
```

The quotient tells us the row.

The remainder tells us the column.

For example,

```text
mid = 5

cols = 3
```

Then:

```text
row = 5 // 3 = 1

col = 5 % 3 = 2
```

So the element is:

```python
matrix[1][2]
```

which is:

```text
11
```

This was the biggest realization while solving this problem.

---

# Pattern Used

## Binary Search

Instead of Binary Searching every row,

treat the entire matrix as one imaginary sorted array.

Maintain:

```text
Left Pointer

Right Pointer
```

Perform Binary Search normally.

Convert every middle index into its corresponding matrix position using:

```python
row = mid // cols
col = mid % cols
```

---

# Optimized Solution

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
```

---

# Dry Run

```text
matrix =

1   3   5
7   9  11
13 15 17

target = 11
```

Pretend the matrix is:

```text
Index:

0 1 2 3 4 5 6 7 8
```

Binary Search eventually reaches:

```text
mid = 5
```

Convert:

```text
row = 5 // 3 = 1

col = 5 % 3 = 2
```

Element:

```text
matrix[1][2] = 11
```

Target found.

Return:

```text
True
```

---

# Complexity Analysis

## Time Complexity

Binary Search is performed over:

```text
m × n
```

elements.

Therefore,

```text
O(log(m × n))
```

---

## Space Complexity

Only constant extra variables are used.

```text
O(1)
```

---

# Key Takeaways

* Don't ignore every sentence in the problem statement.
* The extra property about rows allows us to treat the matrix as one sorted array.
* We never actually flatten the matrix.
* Convert an imaginary index into matrix coordinates using:

```python
row = mid // cols
col = mid % cols
```

* Once mapped, Binary Search works exactly like it does on a normal sorted array.

---

# Concepts Practiced

✅ 2D Arrays

✅ Binary Search

✅ Matrix Index Mapping

✅ Divide and Conquer

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach                       | Time          | Space |
| ------------------------------ | ------------- | ----- |
| Brute Force                    | O(m × n)      | O(1)  |
| Binary Search on Every Row     | O(m log n)    | O(1)  |
| Binary Search on Entire Matrix | O(log(m × n)) | O(1)  |

---

# Status

✅ Solved

✅ Learned to identify hidden clues in the problem statement

✅ Understood how a sorted matrix can be treated as one imaginary sorted array

✅ Learned how to convert a Binary Search index into matrix coordinates using quotient and remainder

✅ Successfully derived the optimal Binary Search solution instead of memorizing it
