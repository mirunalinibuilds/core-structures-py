# 34. Find First and Last Position of Element in Sorted Array

## Problem Statement

Given an array of integers `nums` sorted in **non-decreasing order**, find the **starting** and **ending** position of a given `target` value.

If the target is not found, return:

```text
[-1, -1]
```

You must design an algorithm with **O(log n)** runtime complexity.

---

## Example

**Input**

```text
nums = [5,7,7,8,8,10]

target = 8
```

**Output**

```text
[3,4]
```

---

## LeetCode Link

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

---

# My Learning Journey

At first, I treated this exactly like a normal Binary Search problem.

My first thought was:

> "Once I find the target, return its index."

But then I realized the problem is **not asking for any occurrence**.

It is asking for:

* the **first occurrence**
* the **last occurrence**

That completely changes the strategy.

---

# Key Observation 1

Suppose:

```text
nums = [5,7,7,8,8,8,10]
```

Binary Search lands here:

```text
5 7 7 8 8 8 10
      ^
     mid
```

Finding an `8` is **not enough**.

There might still be another `8` on the left.

So I **cannot return immediately**.

---

# Key Observation 2

To find the **first occurrence**:

Whenever I find the target,

I store its index.

But instead of stopping,

I continue searching the **left half**.

```python
right = mid - 1
```

because there might be another occurrence earlier in the array.

---

# Key Observation 3

To find the **last occurrence**:

Again, whenever I find the target,

I store its index.

But this time,

I continue searching the **right half**.

```python
left = mid + 1
```

because there might be another occurrence later in the array.

---

# Biggest Realization

I initially wondered:

> "Can I solve this using a single Binary Search?"

The answer is **No**.

Once Binary Search finds the target,

it has to choose **one direction**.

* Going left helps find the **first occurrence**.
* Going right helps find the **last occurrence**.

Since both goals require opposite directions,

we perform **two Binary Searches**.

---

# Pattern Used

## Binary Search

Two independent Binary Searches:

### Search 1

Find the **first occurrence**.

Whenever the target is found:

```text
Store answer

Move Left
```

---

### Search 2

Find the **last occurrence**.

Whenever the target is found:

```text
Store answer

Move Right
```

---

# Optimized Solution

```python
class Solution:
    def searchRange(self, nums: List[int], target: int):

        left = 0
        right = len(nums) - 1

        first_occur = -1
        last_occur = -1

        # Find first occurrence
        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                first_occur = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        # Reset pointers
        left = 0
        right = len(nums) - 1

        # Find last occurrence
        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                last_occur = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return [first_occur, last_occur]
```

---

# Dry Run

```text
nums = [5,7,7,8,8,10]

target = 8
```

### First Binary Search

Find an `8`.

Store the index.

Continue searching **left**.

Eventually:

```text
first occurrence = 3
```

---

### Second Binary Search

Find an `8`.

Store the index.

Continue searching **right**.

Eventually:

```text
last occurrence = 4
```

Return:

```text
[3,4]
```

---

# Complexity Analysis

## Time Complexity

First Binary Search:

```text
O(log n)
```

Second Binary Search:

```text
O(log n)
```

Overall:

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

* Finding **one occurrence** is different from finding the **first** or **last** occurrence.
* Do **not** return immediately after finding the target.
* Continue searching:

  * Left for the first occurrence.
  * Right for the last occurrence.
* Two Binary Searches are required because each search moves in a different direction.

---

# Concepts Practiced

✅ Arrays

✅ Binary Search

✅ Modified Binary Search

✅ Search Space Reduction

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach            | Time     | Space |
| ------------------- | -------- | ----- |
| Two Binary Searches | O(log n) | O(1)  |

---

# Status

✅ Solved

✅ Learned how to modify Binary Search instead of returning immediately

✅ Understood why finding the first and last occurrence requires two separate searches

✅ Successfully adapted the classic Binary Search pattern to solve a more advanced problem
