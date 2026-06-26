# Minimum Size Subarray Sum

## Problem Statement

Given an array of **positive integers** `nums` and a positive integer `target`, return the **minimal length** of a contiguous subarray whose sum is **greater than or equal to** `target`.

If there is no such subarray, return `0`.

---

## Example

### Input

```python
target = 7
nums = [2,3,1,2,4,3]
```

### Output

```python
2
```

### Explanation

The subarray:

```python
[4,3]
```

has sum:

```python
7
```

which is greater than or equal to the target.

Its length is:

```python
2
```

and no shorter valid subarray exists.

---

## LeetCode Link

https://leetcode.com/problems/minimum-size-subarray-sum/

---

# My Initial Thought Process

Initially, I thought of generating every possible subarray.

For every starting index:

- Keep extending the subarray.
- Calculate its sum.
- Whenever the sum becomes greater than or equal to the target, record its length.
- Finally return the minimum length.

Although this works, it repeatedly recalculates sums and checks many unnecessary subarrays.

---

# Brute Force Solution

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_len = float('inf')

        for i in range(len(nums)):

            current_sum = 0

            for j in range(i, len(nums)):

                current_sum += nums[j]

                if current_sum >= target:
                    min_len = min(min_len, j - i + 1)
                    break

        return 0 if min_len == float('inf') else min_len
```

---

# Time Complexity

```
O(n²)
```

---

# Space Complexity

```
O(1)
```

---

# Key Observation

The array contains **only positive integers**.

This is extremely important.

Whenever we move the right pointer:

```
Window Sum
```

can only increase.

Whenever we move the left pointer:

```
Window Sum
```

can only decrease.

Because of this property, we never need to move either pointer backwards.

This makes the Sliding Window technique possible.

---

# Optimized Approach (Variable Sliding Window)

Maintain:

- left pointer
- right pointer
- current window sum

Expand the window by moving the right pointer.

Whenever the window sum becomes greater than or equal to the target:

- Update the minimum length.
- Shrink the window from the left to see if we can obtain a smaller valid window.

Repeat until the entire array has been processed.

---

# Optimized Solution

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_window_len = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                window_len = right - left + 1
                min_window_len = min(min_window_len, window_len)

                window_sum -= nums[left]
                left += 1

        if min_window_len == float('inf'):
            return 0
        else:
            return min_window_len
```

---

# Dry Run

Example:

```python
target = 7

nums = [2,3,1,2,4,3]
```

Initially:

```
left = 0
window_sum = 0
```

Expand:

```
[2]
sum = 2
```

Expand:

```
[2,3]
sum = 5
```

Expand:

```
[2,3,1]
sum = 6
```

Expand:

```
[2,3,1,2]
sum = 8
```

The window is now valid.

Length:

```
4
```

Now shrink.

Remove 2:

```
[3,1,2]
sum = 6
```

Not valid anymore.

Continue expanding.

Eventually:

```
[4,3]
sum = 7
```

Length:

```
2
```

This becomes the minimum answer.

---

# Why Variable Sliding Window Works

Since all numbers are positive:

Adding a new element always increases the window sum.

Removing an element always decreases the window sum.

Therefore:

- Expand until the condition becomes true.
- Shrink while the condition remains true.
- Update the answer during shrinking.

Each pointer moves only forward once.

---

# Complexity Analysis

Let:

```
n = length of nums
```

### Time Complexity

Each pointer moves at most:

```
n
```

times.

Therefore:

```
O(n)
```

---

### Space Complexity

Only a few variables are used.

```
O(1)
```

---

# Pattern Learned

## Variable Size Sliding Window

General template:

```python
left = 0

for right in range(len(arr)):

    # Expand window

    while condition:

        # Update answer

        # Shrink window
```

The window size is not fixed.

It expands until the condition becomes true and then shrinks to find a better answer.

---

# Key Takeaways

- Sliding Window works because every element is positive.
- Expand the window until it becomes valid.
- Shrink the window while keeping it valid.
- Update the answer while shrinking.
- Each pointer moves only once, resulting in linear time.

---

# Concepts Practiced

✅ Arrays

✅ Variable Size Sliding Window

✅ Two Pointers

✅ Window Expansion & Shrinking

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(n²) | O(1) |
| Sliding Window | O(n) | O(1) |

---

# Status

✅ Solved

✅ Learned Variable Size Sliding Window

✅ Understood Window Expansion & Shrinking

✅ Understood Why Positive Numbers Make Sliding Window Possible
