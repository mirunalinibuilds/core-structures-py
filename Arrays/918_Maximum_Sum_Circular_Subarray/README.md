# Maximum Sum Circular Subarray

## Problem Statement

Given a **circular integer array** `nums`, return the maximum possible sum of a non-empty subarray.

A circular array means the element after the last element is the first element of the array.

A subarray may wrap around the end of the array, but each element can be included at most once.

---

## Example

### Input

```python
nums = [5,-3,5]
```

### Output

```python
10
```

### Explanation

The maximum circular subarray is:

```python
[5] (last element) + [5] (first element)
```

which gives:

```python
10
```

---

## LeetCode Link

https://leetcode.com/problems/maximum-sum-circular-subarray/

---

# My Initial Thought Process

Initially, I had just learned Kadane's Algorithm from the previous problem.

The normal Maximum Subarray problem finds the best subarray that does **not** wrap around.

The new challenge in this problem was understanding what happens when the subarray wraps around the end of the array.

At first, I thought the wrapped subarray simply meant taking the first and last elements.

After working through multiple examples, I realized something much more important.

A wrapped subarray is actually equivalent to:

```
Entire Array
−
One Continuous Middle Subarray
```

Once I understood this observation, the solution became much simpler.

---

# Key Observation

There are only two possible answers.

## Case 1

The maximum subarray does **not** wrap around.

Example:

```python
[-2,1,-3,4,-1,2,1]
```

This is simply the normal Maximum Subarray problem.

Kadane's Algorithm already solves this.

---

## Case 2

The maximum subarray wraps around.

Instead of directly finding the wrapped subarray,

we can think of it as:

```
Entire Array
−
Minimum Sum Subarray
```

So,

```
Wrapped Sum = Total Sum − Minimum Subarray Sum
```

To find the minimum subarray,

Kadane's Algorithm can be slightly modified by replacing `max()` with `min()`.

---

# Optimized Solution

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        current_min_sum = nums[0]
        current_max_sum = nums[0]

        min_sum = nums[0]
        max_sum = nums[0]

        total = sum(nums)

        for i in range(1, len(nums)):

            current_min_sum = min(current_min_sum + nums[i], nums[i])
            min_sum = min(current_min_sum, min_sum)

            current_max_sum = max(current_max_sum + nums[i], nums[i])
            max_sum = max(current_max_sum, max_sum)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)
```

---

# Dry Run

Example:

```python
nums = [5,-3,5]
```

Maximum Kadane:

```
max_sum = 7
```

Minimum Kadane:

```
min_sum = -3
```

Total Sum:

```
7
```

Wrapped Sum:

```
7 - (-3) = 10
```

Final Answer:

```
max(7,10)

= 10
```

---

# Edge Case

Consider:

```python
nums = [-3,-2,-5]
```

Maximum Kadane:

```
-2
```

Minimum Kadane:

```
-10
```

Total Sum:

```
-10
```

Wrapped Sum:

```
-10 - (-10)

= 0
```

But this is invalid because removing the minimum subarray removes the **entire array**, leaving an empty subarray.

Since the problem requires a **non-empty** subarray,

we simply return:

```
max_sum
```

whenever:

```python
max_sum < 0
```

---

# Why This Works

The answer must belong to one of two categories:

1. Normal maximum subarray.
2. Wrapped maximum subarray.

The wrapped subarray is equivalent to removing the minimum contiguous subarray from the total array.

Therefore,

we compute:

- Maximum Subarray Sum
- Minimum Subarray Sum
- Total Sum

and choose the larger valid answer.

---

# Complexity Analysis

Let:

```
n = length of nums
```

### Time Complexity

Finding the total sum:

```
O(n)
```

Kadane's traversal:

```
O(n)
```

Overall:

```
O(n)
```

---

### Space Complexity

Only a few integer variables are maintained.

```
O(1)
```

---

# Pattern Learned

## Modified Kadane's Algorithm

Kadane's Algorithm can solve more than just the maximum subarray.

For Maximum Subarray:

```python
current_sum = max(current_sum + nums[i], nums[i])
```

For Minimum Subarray:

```python
current_sum = min(current_sum + nums[i], nums[i])
```

The circular subarray problem combines both versions of Kadane's Algorithm in a single solution.

---

# Key Takeaways

- Circular arrays introduce wrapped subarrays.
- A wrapped subarray can be viewed as removing a continuous middle subarray.
- The wrapped sum is calculated using:

```
Total Sum − Minimum Subarray Sum
```

- Kadane's Algorithm can be modified to find both maximum and minimum subarrays.
- Always handle the special case where all elements are negative.

---

# Concepts Practiced

✅ Arrays

✅ Kadane's Algorithm

✅ Modified Kadane's Algorithm

✅ Circular Arrays

✅ Dynamic Programming

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Modified Kadane's Algorithm | O(n) | O(1) |

---

# Status

✅ Solved

✅ Learned Circular Array intuition

✅ Learned Modified Kadane's Algorithm

✅ Understood the "Total Sum − Minimum Subarray" concept

✅ Understood the all-negative edge case
