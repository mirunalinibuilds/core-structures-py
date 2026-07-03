# 11. Container With Most Water

## Problem Statement

You are given an integer array `height` of length `n`.

There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that can hold the **maximum amount of water**.

Return the maximum area of water the container can store.

---

## Example

**Input**

```text
height = [1,8,6,2,5,4,8,3,7]
```

**Output**

```text
49
```

---

## LeetCode Link

https://leetcode.com/problems/container-with-most-water/

---

# My Learning Journey

Initially, I was completely confused by the problem itself.

I wasn't even thinking about the algorithm because I couldn't understand **how the area was being calculated**.

I mistakenly thought the width and height of the container were:

```text
Width = right - left
Height = height[right] - height[left]
```

Then I realized that this is **not** how water behaves.

The biggest breakthrough was understanding the geometry of the problem.

---

# Key Observation 1

Imagine only two lines:

```text
height = [1,8]
```

The water **does not** rise to height `8`.

It leaks from the shorter wall.

So the water level becomes:

```text
min(1,8) = 1
```

This means:

```text
Area = Width × Water Height
```

Where:

```text
Width = right - left

Water Height = min(height[left], height[right])
```

Therefore,

```python
area = min(height[left], height[right]) * (right - left)
```

This was the biggest realization while solving this problem.

---

# Key Observation 2

Now the next question becomes:

After calculating the current area,

**Which pointer should move?**

Suppose:

```text
Left Height = 1

Right Height = 7
```

Current water height is:

```text
1
```

The left wall is limiting the amount of water.

If we move the taller wall:

- Width decreases.
- Water height still remains limited by the shorter wall.

So moving the taller wall can never help.

Instead,

we move the **shorter wall**, hoping to find a taller wall that can increase the water level enough to compensate for the reduced width.

This is the main greedy insight of the problem.

---

# Pattern Used

## Opposite Direction Two Pointers

Start with:

```text
Left Pointer  -> Beginning

Right Pointer -> End
```

At every step:

1. Compute current area.
2. Update maximum area.
3. Move only the pointer pointing to the shorter wall.

Repeat until both pointers meet.

---

# Optimized Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            current_area = min(height[left], height[right]) * (right - left)

            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

# Dry Run

```text
height = [1,8,6,2,5,4,8,3,7]
```

Initially:

```text
L                     R

1                     7
```

Area:

```text
Width = 8

Height = 1

Area = 8
```

Move left pointer because `1` is the shorter wall.

Continue repeating this process until both pointers meet.

The maximum area obtained is:

```text
49
```

---

# Complexity Analysis

## Time Complexity

Each pointer moves only towards the center.

Every index is visited at most once.

```
O(n)
```

---

## Space Complexity

Only constant extra variables are used.

```
O(1)
```

---

# Key Takeaways

- The water level is determined by the **shorter wall**, not the taller one.
- Width is simply the distance between the two pointers.
- Area is:

```text
min(left height, right height) × width
```

- Always move the pointer pointing to the **shorter wall**.
- This is an Opposite Direction Two Pointer problem with a greedy observation.

---

# Concepts Practiced

✅ Arrays

✅ Two Pointers

✅ Greedy Thinking

✅ Geometry Interpretation

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Two Pointers | O(n) | O(1) |

---

# Status

✅ Solved

✅ Understood how the area is actually formed

✅ Learned why the shorter wall determines the water level

✅ Learned the greedy insight behind moving the shorter pointer

✅ Successfully derived the complete optimal solution instead of memorizing it
