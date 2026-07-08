# 162. Find Peak Element

## Problem Statement

A **peak element** is an element that is **strictly greater than its neighbors**.

Given an integer array `nums`, find a peak element and return its index.

If the array contains multiple peaks, return the index of **any** peak.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Example

**Input**

```text
nums = [1,2,3,1]
```

**Output**

```text
2
```

Explanation:

```text
nums[2] = 3
```

is greater than both of its neighbors (`2` and `1`), so it is a peak.

---

## LeetCode Link

https://leetcode.com/problems/find-peak-element/

---

# My Learning Journey

Initially, I thought of solving this by iterating through the array and checking every element.

My idea was to compare each element with its left and right neighbors.

Although this works, I got confused with edge cases like:

* Strictly increasing arrays
* Strictly decreasing arrays

Then I realized the problem specifically asks for an **O(log n)** solution.

That meant Binary Search had to be involved.

The difficult part wasn't identifying Binary Search.

The difficult part was answering:

> **How do I know which pointer to move?**

---

# Key Observation 1

Suppose we are standing at:

```text
nums[mid]
```

Instead of comparing it with the target (like normal Binary Search),

we compare it with its **right neighbor**.

```python
if nums[mid] < nums[mid + 1]:
```

This tells us the array is currently going **uphill**.

Example:

```text
5 8
```

If we're climbing uphill,

a peak **must exist somewhere on the right**.

So we safely discard the left half.

```python
left = mid + 1
```

---

# Key Observation 2

Now suppose:

```python
nums[mid] > nums[mid + 1]
```

Example:

```text
8 5
```

Now we're walking **downhill**.

That means one of two things is true:

* `mid` itself is already a peak.
* A larger peak exists somewhere on the left.

Either way,

the peak must be in the **left half**, including `mid`.

So we keep:

```python
right = mid
```

Notice we **do not** write:

```python
right = mid - 1
```

because `mid` itself could be the answer.

---

# Biggest Realization

The breakthrough for me was understanding that I wasn't searching for a specific value.

I was searching for a **property**.

The Binary Search decision comes from asking:

> **What does this comparison prove?**

If the slope is increasing,

the peak is guaranteed to exist on the right.

If the slope is decreasing,

the peak is guaranteed to exist on the left.

This way of thinking helped me understand pointer movement instead of memorizing it.

---

# Why `while left < right`?

Initially, I always used:

```python
while left <= right
```

because that is how normal Binary Search works.

This problem is different.

We already know that **at least one peak always exists**.

Our goal is not to check whether an answer exists.

Our goal is to narrow the search space until only **one candidate remains**.

Therefore,

```python
while left < right
```

is the correct loop.

When the loop finishes:

```text
left == right
```

That single remaining index must be a peak.

---

# Pattern Used

## Binary Search

Instead of searching for a target value,

Binary Search is used to eliminate half of the search space based on the **direction of the slope**.

---

# Optimized Solution

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            else:
                right = mid

        return left
```

---

# Dry Run

```text
nums = [1,2,3,1]
```

Initially:

```text
left = 0

right = 3
```

First iteration:

```text
mid = 1

nums[mid] = 2

nums[mid+1] = 3
```

Since:

```text
2 < 3
```

we are moving uphill.

So:

```text
left = mid + 1
```

Now:

```text
left = 2

right = 3
```

Eventually:

```text
left == right == 2
```

Return:

```text
2
```

---

# Complexity Analysis

## Time Complexity

Every iteration removes half of the search space.

```text
O(log n)
```

---

## Space Complexity

Only constant extra variables are used.

```text
O(1)
```

---

# Key Takeaways

* This is **not** a normal Binary Search problem.
* We are searching for a **property**, not a value.
* Compare `nums[mid]` with `nums[mid + 1]`.
* If the slope is increasing, search the right half.
* If the slope is decreasing, search the left half (including `mid`).
* `while left < right` is used because one valid answer is guaranteed to exist.

---

# Concepts Practiced

✅ Arrays

✅ Binary Search

✅ Search Space Reduction

✅ Slope Observation

✅ Pointer Movement

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach      | Time     | Space |
| ------------- | -------- | ----- |
| Binary Search | O(log n) | O(1)  |

---

# Status

✅ Solved

✅ Learned how to move Binary Search pointers based on a property instead of a target value

✅ Understood the difference between `while left <= right` and `while left < right`

✅ Learned to use the slope around `mid` to eliminate half of the search space

✅ Successfully solved my first Binary Search problem based on observations rather than exact value matching
