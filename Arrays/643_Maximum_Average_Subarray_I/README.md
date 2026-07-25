# 643. Maximum Average Subarray I

## Problem Statement

You are given an integer array `nums` consisting of `n` elements and an integer `k`.

Find the contiguous subarray of length exactly `k` that has the maximum average value and return that average.

Any answer within `10⁻⁵` of the actual answer will be accepted.

---

## Example

### Input

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

### Output

```text
12.75
```

### Explanation

The subarray with the maximum average is:

```text
[12,-5,-6,50]
```

Its sum is

```text
51
```

Average

```text
51 / 4 = 12.75
```

---

## LeetCode Link

https://leetcode.com/problems/maximum-average-subarray-i/

---

# My Learning Journey

This was my first Sliding Window problem.

Initially, my instinct was to generate every possible subarray of size `k`, calculate its sum, divide by `k`, and keep track of the maximum average.

Although this approach works,

I realized that every new subarray overlaps heavily with the previous one.

For example,

```text
[1,12,-5,-6]

↓

[12,-5,-6,50]
```

Three elements remain exactly the same.

Only:

- one element leaves
- one element enters

Recalculating the entire sum every time would repeat a lot of unnecessary work.

That is exactly why the Sliding Window pattern exists.

---

# Key Observation 1

The window size never changes.

If

```text
k = 4
```

every window always contains exactly four elements.

Example:

```text
Window 1

[1,12,-5,-6]
```

Slide once.

```text
Window 2

[12,-5,-6,50]
```

Slide again.

```text
Window 3

[-5,-6,50,3]
```

The size always remains **4**.

This immediately tells me that this is a **Fixed Sliding Window** problem.

---

# Key Observation 2

Instead of calculating the sum of every window from scratch,

I can reuse the previous window's sum.

Example:

Current window

```text
[1,12,-5,-6]
```

Current sum

```text
2
```

Next window

```text
[12,-5,-6,50]
```

Instead of doing

```text
12 + (-5) + (-6) + 50
```

again,

I simply remove the element leaving the window

```text
-1
```

and add the element entering the window

```text
+50
```

New sum

```text
2 - 1 + 50 = 51
```

This was the biggest realization for me.

---

# Biggest Realization

Sliding Window is all about **reusing previous work**.

The previous window already contains most of the information we need.

When the window moves,

only two things happen:

- One element enters.
- One element leaves.

Therefore,

instead of recalculating the entire sum,

we simply update it.

```python
window_sum += nums[right]
window_sum -= nums[right - k]
```

Understanding this made the pattern feel very natural instead of something to memorize.

---

# Why Don't We Need a Left Pointer?

Initially,

I expected every Sliding Window problem to use two pointers.

But this problem doesn't.

The reason is simple.

The window size is fixed.

If

```text
right = 4
```

and

```text
k = 4
```

then the element leaving the window is always

```text
right - k
```

Example:

```text
Window

[1,12,-5,-6]

↓

[12,-5,-6,50]
```

The element leaving is at index

```text
4 - 4 = 0
```

Since the left boundary can always be calculated,

a separate `left` pointer isn't necessary.

---

# Pattern Used

## Fixed Sliding Window

The window size always remains constant.

Instead of recalculating every window,

we maintain a running sum by:

- Adding the new element entering the window.
- Removing the old element leaving the window.

This reduces the time complexity from **O(n × k)** to **O(n)**.

---

# Optimized Solution

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window_sum = sum(nums[:k])
        ans = window_sum

        for right in range(k, len(nums)):
            window_sum = window_sum + nums[right] - nums[right - k]
            ans = max(ans, window_sum)

        return ans / k
```

---

# Dry Run

```text
nums = [1,12,-5,-6,50,3]

k = 4
```

### Initial Window

```text
[1,12,-5,-6]
```

Sum

```text
2
```

Maximum Sum

```text
2
```

---

### Slide Once

Leaving

```text
1
```

Entering

```text
50
```

New Sum

```text
2 - 1 + 50 = 51
```

Maximum Sum

```text
51
```

---

### Slide Again

Leaving

```text
12
```

Entering

```text
3
```

New Sum

```text
51 - 12 + 3 = 42
```

Maximum Sum remains

```text
51
```

Average

```text
51 / 4 = 12.75
```

Return

```text
12.75
```

---

# Complexity Analysis

## Time Complexity

The initial window sum takes

```text
O(k)
```

The window then slides across the array once.

```text
O(n-k)
```

Overall

```text
O(n)
```

---

## Space Complexity

Only a few variables are used.

```text
O(1)
```

---

# Key Takeaways

- When the problem says **exactly `k` elements**, think **Fixed Sliding Window**.
- Every new window differs from the previous window by only one element.
- Reuse the previous window's sum instead of recomputing it.
- A separate left pointer is unnecessary because the leaving index is always `right - k`.
- Sliding Window reduces repeated work and achieves linear time complexity.

---

# Concepts Practiced

✅ Arrays

✅ Fixed Sliding Window

✅ Running Sum

✅ Window Expansion

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Fixed Sliding Window | O(n) | O(1) |

---

# Status

✅ Solved

✅ Learned my first Sliding Window pattern

✅ Understood the difference between recalculating a window and updating a window

✅ Learned why Fixed Sliding Window doesn't require a left pointer

✅ Learned to identify problems that specify **exactly `k` elements**

✅ Successfully solved my first Fixed Sliding Window problem using the Sliding Window pattern
