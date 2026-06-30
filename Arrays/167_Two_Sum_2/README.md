# 167. Two Sum II - Input Array Is Sorted

## Problem Statement

Given a **1-indexed** array of integers `numbers` that is already sorted in **non-decreasing order**, find two numbers such that they add up to a specific `target`.

Return the indices of the two numbers (1-indexed) as an array `[index1, index2]`.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

### Example

**Input**

```text
numbers = [2,7,11,15]
target = 9
```

**Output**

```text
[1,2]
```

**Explanation**

```
2 + 7 = 9
```

Their 1-indexed positions are:

```
[1,2]
```

---

## LeetCode Link

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

---

# My Thought Process

Initially, I tried approaching this problem using one fixed pointer and another moving pointer.

Although it worked for a few public test cases, I realized that I wasn't fully utilizing the fact that the array was **already sorted**.

After thinking about the sorted property, I understood the key observation:

- If the current sum is **smaller** than the target, I need a **larger** sum.
- Since the array is sorted, moving the **left pointer** to the right increases the sum.

Similarly,

- If the current sum is **greater** than the target, I need a **smaller** sum.
- Moving the **right pointer** to the left decreases the sum.

This led me to the Opposite-End Two Pointer pattern.

---

# Optimized Solution

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int):
        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum < target:
                left += 1

            elif current_sum > target:
                right -= 1

            else:
                return [left + 1, right + 1]
```

---

# Dry Run

Input:

```text
numbers = [2,7,11,15]
target = 9
```

Initially:

```text
left = 0
right = 3
```

Current sum:

```text
2 + 15 = 17
```

Too large.

Move right pointer.

```
right = 2
```

Current sum:

```text
2 + 11 = 13
```

Still too large.

Move right pointer.

```
right = 1
```

Current sum:

```text
2 + 7 = 9
```

Target found.

Return:

```text
[1,2]
```

---

# Why Two Pointers Works

The array is already sorted.

If the current sum is too small, moving the left pointer is the only way to increase the sum.

If the current sum is too large, moving the right pointer is the only way to decrease the sum.

Because each pointer only moves inward once, every element is processed at most once.

---

# Complexity Analysis

## Time Complexity

Each pointer moves at most `n` times.

```
O(n)
```

---

## Space Complexity

Only two pointers and a few variables are used.

```
O(1)
```

---

# Pattern Learned

## Opposite-End Two Pointers on Sorted Arrays

Start with one pointer at the beginning and another at the end.

- If sum < target → move left pointer.
- If sum > target → move right pointer.
- If sum == target → return the answer.

The sorted property allows us to eliminate impossible pairs efficiently.

---

# Key Takeaways

- Always look for useful properties given in the problem statement.
- A sorted array often suggests Binary Search or Two Pointers.
- Opposite-End Two Pointers reduce the brute-force `O(n²)` solution to `O(n)`.
- Think about **how moving a pointer affects the sum**, rather than memorizing pointer movements.

---

# Concepts Practiced

✅ Arrays

✅ Sorted Arrays

✅ Two Pointers

✅ Opposite-End Two Pointer Pattern

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(n²) | O(1) |
| Two Pointers | O(n) | O(1) |

---

# Status

✅ Solved

✅ Learned how sorted arrays enable the Two Pointer technique

✅ Understood why moving the left pointer increases the sum and moving the right pointer decreases the sum

✅ Strengthened understanding of the Opposite-End Two Pointer pattern
