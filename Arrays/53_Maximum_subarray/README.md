# Maximum Subarray

## Problem Statement

Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.

A subarray is a contiguous part of an array.

---

## Example

### Input

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

### Output

```python
6
```

### Explanation

The maximum sum subarray is:

```python
[4,-1,2,1]
```

Its sum is:

```python
6
```

---

## LeetCode Link

https://leetcode.com/problems/maximum-subarray/

---

# My Initial Thought Process

Initially, I thought this might be another Sliding Window problem because it involved finding a contiguous subarray.

However, after understanding the problem more deeply, I realized Sliding Window cannot be applied here.

In Sliding Window problems, there is usually a condition that tells us when to expand or shrink the window.

For example:

- Window sum ≥ target
- Duplicate character exists
- Fixed window size `k`

In this problem, there is no such condition.

Instead, I learned a completely new pattern called **Kadane's Algorithm**.

The key idea is:

At every element, decide whether it is better to:

- Continue the previous subarray.
- Or start a brand new subarray from the current element.

---

# Key Observation

Suppose the current running sum is:

```python
-8
```

and the next number is:

```python
5
```

There are two choices:

Continue:

```python
-8 + 5 = -3
```

Start fresh:

```python
5
```

Clearly,

starting a new subarray is better.

This is exactly the decision Kadane's Algorithm makes at every element.

---

# Optimized Solution (Kadane's Algorithm)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = float('-inf')
        max_sum = float('-inf')

        for i in range(len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(current_sum, max_sum)

        return max_sum
```

---

# Dry Run

Example:

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

Initially:

```
current_sum = -∞
max_sum = -∞
```

Process each element:

| Current Number | Continue | Start Fresh | Current Sum | Max Sum |
|---------------|----------|-------------|-------------|----------|
| -2 | -∞ | -2 | -2 | -2 |
| 1 | -1 | 1 | 1 | 1 |
| -3 | -2 | -3 | -2 | 1 |
| 4 | 2 | 4 | 4 | 4 |
| -1 | 3 | -1 | 3 | 4 |
| 2 | 5 | 2 | 5 | 5 |
| 1 | 6 | 1 | 6 | 6 |
| -5 | 1 | -5 | 1 | 6 |
| 4 | 5 | 4 | 5 | 6 |

Final Answer:

```
6
```

---

# Why Kadane's Algorithm Works

At every index, only two possibilities exist:

1. Continue the current subarray.

```python
current_sum + nums[i]
```

2. Start a new subarray.

```python
nums[i]
```

We simply choose whichever gives the larger sum.

If the previous running sum is hurting us, we discard it and begin a new subarray.

This local decision eventually leads to the global maximum subarray.

---

# Complexity Analysis

Let:

```
n = length of nums
```

### Time Complexity

The array is traversed exactly once.

```
O(n)
```

---

### Space Complexity

Only two variables are maintained.

```
O(1)
```

---

# Pattern Learned

## Kadane's Algorithm

General template:

```python
current_sum = nums[0]
max_sum = nums[0]

for i in range(1, len(nums)):
    current_sum = max(current_sum + nums[i], nums[i])
    max_sum = max(max_sum, current_sum)
```

Core idea:

At every element,

- Continue the previous subarray.
- Or start a new subarray.

Choose whichever gives the larger sum.

---

# Key Takeaways

- Not every contiguous subarray problem is a Sliding Window problem.
- Sliding Window requires a condition to expand or shrink.
- Kadane's Algorithm is used for maximum or minimum contiguous subarray sum problems.
- At every element, decide whether to continue the existing subarray or start a new one.
- Kadane's Algorithm solves the problem in linear time.

---

# Concepts Practiced

✅ Arrays

✅ Dynamic Programming

✅ Kadane's Algorithm

✅ Greedy Decision Making

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Kadane's Algorithm | O(n) | O(1) |

---

# Status

✅ Solved

✅ Learned Kadane's Algorithm

✅ Understood why Sliding Window cannot be applied

✅ Understood the "Continue or Start Fresh" intuition

✅ Implemented Kadane's Algorithm successfully
