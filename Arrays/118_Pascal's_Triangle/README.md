# Pascal's Triangle

## Problem Statement

Given an integer `numRows`, return the first `numRows` rows of Pascal's Triangle.

In Pascal's Triangle:

- The first and last element of every row is `1`
- Every middle element is the sum of the two elements directly above it

### Example

### Input

```python
numRows = 5
```

### Output

```python
[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
]
```

---

## LeetCode Link

https://leetcode.com/problems/pascals-triangle/

---

## My Initial Thought Process

I first tried to understand the pattern manually.

```text
Row 0 -> [1]

Row 1 -> [1,1]

Row 2 -> [1,2,1]

Row 3 -> [1,3,3,1]

Row 4 -> [1,4,6,4,1]
```

I noticed:

- Every row starts with `1`
- Every row ends with `1`
- The middle elements come from adding adjacent elements of the previous row

Example:

```python
Previous Row

[1,3,3,1]

Current Row

[1,4,6,4,1]
```

Because:

```python
1 + 3 = 4
3 + 3 = 6
3 + 1 = 4
```

I understood the pattern but struggled to convert it into code.

---

## Learning From NeetCode

After attempting the problem, I watched NeetCode's explanation and learned a very clever trick.

Instead of handling:

- First element separately
- Middle elements separately
- Last element separately

we can use **zero padding**.

---

## Key Observation

Suppose the previous row is:

```python
[1,2,1]
```

Pad zeros on both sides:

```python
[0,1,2,1,0]
```

Now add adjacent elements:

```python
0 + 1 = 1
1 + 2 = 3
2 + 1 = 3
1 + 0 = 1
```

Result:

```python
[1,3,3,1]
```

which is exactly the next row of Pascal's Triangle.

This completely eliminates the need for special cases.

---

## Optimized Solution

```python
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):

            temp = [0] + res[-1] + [0]
            row = []

            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])

            res.append(row)

        return res
```

---

## Dry Run

Current Row:

```python
[1,2,1]
```

Padding:

```python
[0,1,2,1,0]
```

Generate next row:

```python
0+1 = 1
1+2 = 3
2+1 = 3
1+0 = 1
```

New Row:

```python
[1,3,3,1]
```

Store it inside the result.

Continue until all rows are generated.

---

## Why This Works

Padding creates automatic boundaries.

Example:

```python
[0,1,2,1,0]
```

First element:

```python
0 + 1 = 1
```

Last element:

```python
1 + 0 = 1
```

Middle elements:

```python
1 + 2 = 3
2 + 1 = 3
```

Thus every element of the next row is generated correctly using a single rule:

```text
Add adjacent elements.
```

---

## Complexity Analysis

Let:

```text
n = numRows
```

### Time Complexity

Each element of Pascal's Triangle is generated exactly once.

```text
O(n²)
```

### Space Complexity

We store the complete triangle.

```text
O(n²)
```

---

## Pattern Learned

### Building Current State From Previous State

Each row is generated using information from the previous row.

Example:

```python
Previous Row
↓
Pad With Zeros
↓
Add Adjacent Elements
↓
Generate Current Row
```

This introduces the intuition behind Dynamic Programming:

```text
Build future results using already computed results.
```

---

## Key Takeaways

- Always look for patterns before coding.
- Understanding the structure of Pascal's Triangle is more important than memorizing the code.
- Zero-padding is a clever technique that removes edge-case handling.
- Dynamic Programming often involves building new answers from previously computed answers.
- Sometimes watching an optimized solution after attempting the problem can reveal cleaner approaches.

---

## Concepts Practiced

✅ Arrays

✅ 2D Arrays

✅ Pattern Recognition

✅ Simulation

✅ Dynamic Programming Intuition

✅ Matrix Construction

---

## Final Complexity

| Approach | Time | Space |
|-----------|--------|--------|
| Generate Entire Triangle | O(n²) | O(n²) |

---

## Status

✅ Solved

✅ Learned Pascal's Triangle Pattern

✅ Learned Zero-Padding Technique

✅ Introduced to Dynamic Programming Intuition

✅ Understood Building Current State From Previous State
