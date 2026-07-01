# 283. Move Zeroes

## Problem Statement

Given an integer array `nums`, move all the `0`s to the end of the array while maintaining the relative order of the non-zero elements.

The operation must be performed **in-place** without making a copy of the array.

### Example

**Input**

```text
nums = [0,1,0,3,12]
```

**Output**

```text
[1,3,12,0,0]
```

**Explanation**

All non-zero elements are moved to the front while preserving their original order, and all zeros are shifted to the end.

---

## LeetCode Link

https://leetcode.com/problems/move-zeroes/

---

# My Thought Process

Since I had just learned the **Same-Direction Two Pointer** pattern from the previous problem, I immediately thought of using a **slow pointer** and a **fast pointer**.

Initially, I made one mistake.

I was swapping whenever the fast pointer found a **zero**, which ended up moving all the zeros to the beginning of the array instead of the end.

After thinking about it, I realized that the slow pointer should always point to the position where the **next non-zero element** should be placed.

So instead of checking for zeros, I should process only the **non-zero elements**.

Whenever the fast pointer finds a non-zero number:

- Swap it with the slow pointer.
- Move the slow pointer forward.

The fast pointer continues scanning the array until the end.

---

# Optimized Solution

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        for fast in range(len(nums)):

            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
```

---

# Dry Run

Input:

```text
nums = [0,1,0,3,12]
```

Initially:

```text
0 1 0 3 12
S
F
```

Fast sees:

```
0
```

Ignore it.

Move fast.

Fast now points to:

```
1
```

Non-zero found.

Swap:

```text
1 0 0 3 12
```

Move slow.

Continue scanning.

Next non-zero:

```
3
```

Swap:

```text
1 3 0 0 12
```

Move slow.

Next non-zero:

```
12
```

Swap:

```text
1 3 12 0 0
```

Return the modified array.

---

# Why Same-Direction Two Pointers Works

The fast pointer scans every element exactly once.

The slow pointer always points to the position where the next non-zero element should be placed.

Whenever a non-zero element is found, it is moved to the correct position.

All zeros naturally accumulate towards the end of the array.

---

# Complexity Analysis

## Time Complexity

Each element is visited exactly once.

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

- Fast Pointer → Reads every element.
- Slow Pointer → Tracks where the next valid element should be placed.

This pattern is commonly used for in-place array modification while preserving the order of elements.

---

# Key Takeaways

- Focus on moving the useful elements instead of the unwanted ones.
- The slow pointer always represents the next correct position.
- The fast pointer scans the array exactly once.
- Same-Direction Two Pointers are very useful for in-place array problems.

---

# Concepts Practiced

✅ Arrays

✅ Same-Direction Two Pointers

✅ In-place Array Modification

✅ Swapping Elements

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

✅ Strengthened the Same-Direction Two Pointer pattern

✅ Learned to distinguish between moving useful elements and unwanted elements

✅ Understood how swapping can be used for in-place array modification
