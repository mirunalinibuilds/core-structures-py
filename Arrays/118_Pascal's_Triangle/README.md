# Pascal's Triangle

**LeetCode:** 118. Pascal's Triangle

## Problem Statement

Given an integer `numRows`, return the first `numRows` rows of Pascal's Triangle.

In Pascal's Triangle:

- The first and last element of every row is `1`
- Every middle element is the sum of the two elements directly above it

### Example

**Input**

```python
numRows = 5
```

**Output**

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

## Approach

I used the **zero-padding technique** to generate each row.

Instead of handling the first and last elements separately, I pad the previous row with zeros on both sides and then add adjacent elements.

### Example

Previous Row:

```python
[1,2,1]
```

After Padding:

```python
[0,1,2,1,0]
```

Add adjacent pairs:

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

---

## Algorithm

1. Start with the first row `[1]`.
2. For each new row:
   - Take the last row generated.
   - Pad it with zeros on both sides.
   - Add adjacent elements.
   - Store the new row.
3. Repeat until `numRows` rows are generated.

---

## Solution

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

Padded Row:

```python
[0,1,2,1,0]
```

Adjacent Sums:

```python
0+1 = 1
1+2 = 3
2+1 = 3
1+0 = 1
```

Generated Row:

```python
[1,3,3,1]
```

---

## Complexity Analysis

### Time Complexity

```text
O(numRows²)
```

Each element of Pascal's Triangle is generated exactly once.

### Space Complexity

```text
O(numRows²)
```

The entire triangle is stored in memory.

---

## Concepts Practiced

- Arrays / Lists
- Pattern Recognition
- Simulation
- Dynamic Programming Intuition
- Matrix Construction

---

## Key Learning

A neat trick for Pascal's Triangle is to pad the previous row with zeros:

```python
temp = [0] + previous_row + [0]
```

Then generate the next row by adding adjacent elements.

This eliminates special handling for the first and last elements and leads to a clean solution.
