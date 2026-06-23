# Running Sum of 1D Array

## Problem Statement

Given an array `nums`, return the running sum of `nums`.

The running sum of an array is defined as:

```text
runningSum[i] = sum(nums[0] ... nums[i])
```

In other words, each position stores the sum of all elements from the beginning of the array up to that index.

---

## Example

### Input

```python
nums = [1,2,3,4]
```

### Output

```python
[1,3,6,10]
```

### Explanation

```python
1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
```

Result:

```python
[1,3,6,10]
```

---

## LeetCode Link

https://leetcode.com/problems/running-sum-of-1d-array/

---

# My Initial Thought Process

For each position, I need the sum of all elements before it including itself.

Example:

```python
nums = [1,2,3,4]
```

Running Sum:

```python
[1,3,6,10]
```

This immediately suggests the Prefix Sum pattern.

---

# Key Observation

If we already know the running sum up to the previous index:

```python
prefix[i-1]
```

then the current running sum can be calculated as:

```python
prefix[i] = prefix[i-1] + nums[i]
```

This allows us to build the answer efficiently in one pass.

---

# Prefix Sum Formula

```python
prefix[i] = prefix[i-1] + nums[i]
```

Meaning:

```text
Current Prefix Sum
=
Previous Prefix Sum
+
Current Element
```

This is the foundation of many Prefix Sum problems.

---

# Solution

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        return prefix
```

---

# Dry Run

### Input

```python
nums = [1,2,3,4]
```

Create prefix array:

```python
prefix = [0,0,0,0]
```

Initialize:

```python
prefix[0] = nums[0]
```

```python
prefix = [1,0,0,0]
```

---

### i = 1

```python
prefix[1] = prefix[0] + nums[1]
```

```python
1 + 2 = 3
```

```python
[1,3,0,0]
```

---

### i = 2

```python
prefix[2] = prefix[1] + nums[2]
```

```python
3 + 3 = 6
```

```python
[1,3,6,0]
```

---

### i = 3

```python
prefix[3] = prefix[2] + nums[3]
```

```python
6 + 4 = 10
```

```python
[1,3,6,10]
```

Final Answer:

```python
[1,3,6,10]
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

The array is traversed exactly once.

---

## Space Complexity

```text
O(n)
```

An additional prefix array is created.

---

# Space Optimized Approach

Since the problem allows modifying the input array:

```python
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]

return nums
```

This achieves:

```text
Time Complexity: O(n)
Space Complexity: O(1)
```

---

# Pattern Learned

## Prefix Sum

Prefix Sum stores cumulative sums.

Example:

```python
nums = [1,2,3,4]
```

Prefix Sum:

```python
[1,3,6,10]
```

---

## Building Prefix Sum

Formula:

```python
prefix[i] = prefix[i-1] + nums[i]
```

---

## Using Prefix Sum

Once a prefix array is built, we can quickly find the sum of any range.

Formula:

```python
prefix[R] - prefix[L-1]
```

Example:

```python
nums = [2,4,6,8,10]
```

Prefix:

```python
[2,6,12,20,30]
```

Sum from index 1 to 3:

```python
4 + 6 + 8
```

Using Prefix Sum:

```python
prefix[3] - prefix[0]
```

```python
20 - 2 = 18
```

Time:

```text
O(1)
```

---

# Key Takeaways

- Running Sum is the simplest Prefix Sum problem.
- Prefix Sum allows cumulative calculations in a single pass.
- Many future Array and Sliding Window problems build upon this concept.
- Learning Prefix Sum early makes range-sum problems much easier.

---

# Concepts Practiced

✅ Arrays

✅ Prefix Sum

✅ Dynamic Array Construction

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Metric | Complexity |
|----------|----------|
| Time Complexity | O(n) |
| Space Complexity | O(n) |

---

## Status

✅ Solved

✅ Learned Prefix Sum Basics

✅ Understood Prefix Sum Formula

✅ Ready for Advanced Prefix Sum Problems
