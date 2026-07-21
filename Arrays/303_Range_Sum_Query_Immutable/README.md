# 303. Range Sum Query – Immutable

## Problem Statement

Given an integer array `nums`, handle multiple queries of the following type:

- Return the sum of the elements between indices `left` and `right` (inclusive).

Implement the `NumArray` class:

- `NumArray(int[] nums)` initializes the object with the integer array.
- `sumRange(int left, int right)` returns the sum of the elements between indices `left` and `right`.

The goal is to answer each query as efficiently as possible.

---

## Example

### Input

```text
["NumArray", "sumRange", "sumRange", "sumRange"]

[[[-2,0,3,-5,2,-1]], [0,2], [2,5], [0,5]]
```

### Output

```text
[null, 1, -1, -3]
```

### Explanation

```python
NumArray numArray = NumArray([-2,0,3,-5,2,-1]);

numArray.sumRange(0,2);   // 1
numArray.sumRange(2,5);   // -1
numArray.sumRange(0,5);   // -3
```

---

## LeetCode Link

https://leetcode.com/problems/range-sum-query-immutable/

---

# My Learning Journey

Initially, I thought of solving every query by iterating from `left` to `right` and calculating the sum.

Although this works for a single query, I realized that the array never changes and the function `sumRange()` can be called many times.

That means I would be repeating the same additions over and over again.

This is exactly the type of problem Prefix Sum was designed to solve.

The biggest realization was:

> Instead of calculating the same sums repeatedly, calculate them once and reuse them forever.

---

# Key Observation 1

Instead of storing the original numbers,

store the cumulative sum from the beginning of the array.

For example,

```text
nums

[2,5,3,6]
```

Prefix Sum becomes

```text
[2,7,10,16]
```

Each value represents:

> Sum of all elements from index `0` to the current index.

---

# Key Observation 2

Suppose we want the sum from index `1` to index `3`.

The Prefix Sum at index `3` already contains:

```text
2 + 5 + 3 + 6
```

The only extra part is everything before index `1`.

That extra part is:

```text
2
```

which is simply:

```text
prefix[0]
```

Therefore,

```text
Range Sum

=

Prefix at Right

-

Prefix before Left
```

This allows every query to be answered in constant time.

---

# Biggest Realization

The breakthrough for me was understanding that Prefix Sum is nothing more than carrying the history of everything seen so far.

Every Prefix Sum value stores the cumulative sum from the beginning.

Instead of recalculating the same values repeatedly,

we reuse previously computed information.

This changed the problem from:

> "Calculate every query."

to

> "Precompute once, answer forever."

---

# Why Handle `left == 0` Separately?

Suppose the query is:

```text
left = 0
right = 3
```

The required answer is simply

```text
prefix[3]
```

There is no Prefix Sum before index `0`.

Trying to access

```python
prefix[-1]
```

would be incorrect.

Therefore,

```python
if left == 0:
    return prefix[right]
```

handles this boundary condition separately.

---

# Pattern Used

## Prefix Sum

Instead of repeatedly computing the same range sums,

we preprocess the array once by storing cumulative sums.

Each query is then answered using previously computed information.

---

# Optimized Solution

```python
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)

        self.prefix[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:

        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]
```

---

# Dry Run

Suppose

```text
nums = [2,5,3,6]
```

Build Prefix Sum

```text
prefix

[2,7,10,16]
```

### Query

```text
left = 1

right = 3
```

Answer

```text
prefix[3] - prefix[0]

16 - 2

14
```

Which equals

```text
5 + 3 + 6
```

Correct.

---

# Complexity Analysis

## Initialization

Building the Prefix Sum array requires one traversal.

**Time Complexity**

```text
O(n)
```

---

## Query

Each query performs only constant-time operations.

**Time Complexity**

```text
O(1)
```

---

## Space Complexity

An additional Prefix Sum array of size `n` is maintained.

```text
O(n)
```

---

# Key Takeaways

- Prefix Sum stores cumulative sums instead of original values.
- Preprocessing once avoids repeated calculations.
- Every range sum can be answered using previously computed information.
- The formula is derived by removing the unnecessary left portion from the Prefix Sum.
- Handle `left == 0` separately because there is no Prefix Sum before index `0`.
- Prefix Sum is one of the most fundamental array preprocessing techniques.

---

# Concepts Practiced

✅ Arrays

✅ Prefix Sum

✅ Range Sum Queries

✅ Preprocessing

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Prefix Sum | O(n) preprocessing + O(1) per query | O(n) |

---

# Status

✅ Solved

✅ Learned how Prefix Sum avoids repeated computations

✅ Understood how to answer range sum queries in constant time

✅ Learned why `prefix[right] - prefix[left - 1]` works

✅ Understood the importance of preprocessing before handling multiple queries

✅ Strengthened my understanding of the Prefix Sum pattern
