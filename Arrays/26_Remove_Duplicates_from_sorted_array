# 26. Remove Duplicates from Sorted Array

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once.

The relative order of the elements should be kept the same.

Return the number of unique elements.

### Example

**Input**

```text
nums = [1,1,2]
```

**Output**

```text
2
```

**Explanation**

After removing duplicates, the first two elements become:

```text
[1,2]
```

The returned value is:

```text
2
```

---

## LeetCode Link

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

---

# My Thought Process

The important observation in this problem is that the array is already **sorted**.

Since duplicate elements always appear next to each other, I don't need any extra data structure like a set or dictionary.

I learned a new variation of the Two Pointer pattern called **Same-Direction Two Pointers**.

In this pattern:

- The **fast pointer** scans every element in the array.
- The **slow pointer** keeps track of the position where the next unique element should be placed.

Whenever the fast pointer finds a new unique value, I move the slow pointer forward and copy the new value there.

---

# Optimized Solution

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in range(len(nums)):

            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
```

---

# Dry Run

Input:

```text
nums = [1,1,2,2,3]
```

Initially:

```text
1 1 2 2 3
S
F
```

Fast moves to the second element.

```
1 == 1
```

Duplicate found.

Do nothing.

Fast moves again.

```
1 != 2
```

New unique element found.

Move slow forward.

Copy:

```text
1 2 2 2 3
  S
```

Continue scanning.

Next duplicate:

```
2 == 2
```

Ignore it.

Next unique value:

```
3
```

Move slow forward.

Copy:

```text
1 2 3 2 3
    S
```

The first `slow + 1` elements now contain all unique values.

Return:

```text
3
```

---

# Why Same-Direction Two Pointers Works

The array is already sorted.

This means duplicate values always appear together.

The fast pointer scans every element.

The slow pointer always points to the last unique element stored in the array.

Whenever a new unique element is found, it is copied to the next available position.

Everything before the slow pointer always contains only unique values.

---

# Complexity Analysis

## Time Complexity

The fast pointer visits every element exactly once.

```
O(n)
```

---

## Space Complexity

Only two pointers are used.

```
O(1)
```

---

# Pattern Learned

## Same-Direction Two Pointers

Unlike the opposite-end pattern, both pointers move from left to right.

- Fast Pointer → Reads every element.
- Slow Pointer → Tracks where the next valid element should be written.

This pattern is commonly used for in-place array modification.

---

# Key Takeaways

- Always pay attention if the array is already sorted.
- Sorted arrays often allow in-place solutions.
- Same-Direction Two Pointers use one pointer for reading and another for writing.
- No extra data structures are required.

---

# Concepts Practiced

✅ Arrays

✅ Sorted Arrays

✅ Same-Direction Two Pointers

✅ In-place Array Modification

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Same-Direction Two Pointers | O(n) | O(1) |

---

# Status

✅ Solved

✅ Learned the Same-Direction Two Pointer pattern

✅ Understood the roles of the Fast Pointer and Slow Pointer

✅ Learned how to modify an array in-place without using extra space
