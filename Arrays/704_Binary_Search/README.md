# 704. Binary Search

## Problem Statement

Given an array of integers `nums` which is sorted in **ascending order**, and an integer `target`, return the **index** of `target` if it exists in the array.

If `target` does not exist, return `-1`.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Example

**Input**

```text
nums = [-1,0,3,5,9,12]
target = 9
```

**Output**

```text
4
```

---

## LeetCode Link

https://leetcode.com/problems/binary-search/

---

# My Learning Journey

This was my first Binary Search problem.

Initially, I made one important mistake.

I compared the **middle index** with the target instead of comparing the **middle element**.

I wrote:

```python
if mid == target:
```

Instead of:

```python
if nums[mid] == target:
```

This made me realize that Binary Search is never about comparing indices.

It is always about comparing the **value stored at the middle index**.

---

# Key Observation 1

Since the array is already **sorted**, I don't have to search every element.

Every comparison allows me to eliminate **half of the remaining search space**.

This is what makes Binary Search much faster than Linear Search.

---

# Key Observation 2

Maintain two pointers:

```text
Left Pointer  -> Beginning

Right Pointer -> End
```

These pointers represent the current search space.

While the search space is still valid:

```text
left <= right
```

calculate the middle element.

---

# Key Observation 3

Find the middle index:

```python
mid = (left + right) // 2
```

Now compare:

```python
nums[mid]
```

with the target.

There are only three possibilities:

### Case 1

```text
nums[mid] == target
```

Target found.

Return the index.

---

### Case 2

```text
nums[mid] < target
```

The target can only exist in the **right half**.

Discard the left half.

```python
left = mid + 1
```

---

### Case 3

```text
nums[mid] > target
```

The target can only exist in the **left half**.

Discard the right half.

```python
right = mid - 1
```

---

# Pattern Used

## Binary Search

Maintain a search window.

At every step:

1. Find the middle.
2. Compare the middle element with the target.
3. Discard one half of the search space.
4. Repeat until the target is found or the search space becomes empty.

---

# Optimized Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
```

---

# Dry Run

```text
nums = [-1,0,3,5,9,12]

target = 9
```

Initially:

```text
L              R

-1 0 3 5 9 12
```

Middle:

```text
mid = 2

nums[mid] = 3
```

Since:

```text
3 < 9
```

Discard the left half.

```text
left = mid + 1
```

Now:

```text
5 9 12
```

Middle becomes:

```text
9
```

Target found.

Return its index.

---

# Complexity Analysis

## Time Complexity

At every iteration, half of the search space is discarded.

```text
n → n/2 → n/4 → n/8 ...
```

Therefore:

```
O(log n)
```

---

## Space Complexity

Only a few variables are used.

```
O(1)
```

---

# Key Takeaways

* Binary Search works **only on sorted data**.
* Compare the **middle element**, not the middle index.
* Every comparison removes half of the search space.
* Use:

```python
while left <= right
```

for searching an exact target.

---

# Concepts Practiced

✅ Arrays

✅ Binary Search

✅ Divide and Conquer

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

✅ Learned the Binary Search pattern

✅ Understood how the search space shrinks after every comparison

✅ Learned to compare `nums[mid]` with the target instead of comparing `mid`

✅ Successfully implemented the classic Binary Search algorithm
