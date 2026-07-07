# 35. Search Insert Position

## Problem Statement

Given a **sorted** array of distinct integers `nums` and a `target` value, return the **index** if the target is found.

If the target is not found, return the **index where it would be inserted** to maintain the sorted order.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Example

**Input**

```text
nums = [1,3,5,6]

target = 5
```

**Output**

```text
2
```

---

**Input**

```text
nums = [1,3,5,6]

target = 2
```

**Output**

```text
1
```

---

## LeetCode Link

https://leetcode.com/problems/search-insert-position/

---

# My Learning Journey

Initially, I approached this exactly like a normal Binary Search problem.

If I found the target, I simply returned its index.

The confusing part was:

> "What should I return if the target doesn't exist?"

At first, I searched online and discovered Python's built-in `bisect` module, which returns the correct insertion position in a sorted array.

Although that worked, I later realized the Binary Search itself already gives us the answer without using any library.

---

# Key Observation 1

Binary Search continues until:

```text
left > right
```

At this point, the target was not found.

Initially, I thought I needed another algorithm to calculate the insertion position.

But the insertion position is already stored in one of the pointers.

---

# Key Observation 2

Consider:

```text
nums = [1,3,5,6]

target = 2
```

Binary Search finishes with:

```text
left = 1

right = 0
```

Where should `2` be inserted?

```text
[1, 2, 3, 5, 6]
```

Index:

```text
1
```

Exactly the value of:

```text
left
```

---

# Key Observation 3

Another example:

```text
nums = [1,3,5,6]

target = 7
```

Binary Search finishes with:

```text
left = 4

right = 3
```

Where should `7` be inserted?

```text
[1,3,5,6,7]
```

Index:

```text
4
```

Again,

the answer is simply:

```text
left
```

---

# Biggest Realization

I initially thought I needed Python's `bisect` module to find the insertion position.

Later I understood that the Binary Search pointers naturally provide it.

After the loop ends:

```python
return left
```

is enough.

The `left` pointer always represents the first valid position where the target can be inserted while keeping the array sorted.

---

# Pattern Used

## Binary Search

Perform a normal Binary Search.

* If the target is found, return its index.
* Otherwise, when the search finishes, return the `left` pointer.

---

# Optimized Solution

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int):

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

        return left
```

---

# Dry Run

```text
nums = [1,3,5,6]

target = 2
```

Initially:

```text
left = 0

right = 3
```

Binary Search continues.

Eventually:

```text
left = 1

right = 0
```

Since:

```text
left > right
```

the loop stops.

Return:

```text
left = 1
```

which is exactly the correct insertion position.

---

# Complexity Analysis

## Time Complexity

Binary Search halves the search space in every iteration.

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

* This is a standard Binary Search problem.
* If the target is found, return its index immediately.
* If the target is not found, **do not perform another search**.
* After Binary Search ends, the `left` pointer already represents the correct insertion position.
* Python's `bisect` module can solve the problem, but understanding why `left` works is more important.

---

# Concepts Practiced

✅ Arrays

✅ Binary Search

✅ Pointer Movement

✅ Search Space Reduction

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

✅ Understood why the `left` pointer becomes the insertion position

✅ Learned that Python's `bisect` module provides the same functionality

✅ Strengthened Binary Search fundamentals without relying on built-in functions
