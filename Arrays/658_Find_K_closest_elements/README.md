# 658. Find K Closest Elements

## Problem Statement

Given a **sorted integer array** `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array.

The result should be sorted in ascending order.

If there is a tie (two numbers are equally close to `x`), the **smaller number** should be preferred.

---

## Example

**Input**

```text
arr = [1,2,3,4,5]
k = 4
x = 3
```

**Output**

```text
[1,2,3,4]
```

---

## LeetCode Link

https://leetcode.com/problems/find-k-closest-elements/

---

# My Learning Journey

Initially, I approached this problem completely the wrong way.

My first instinct was to **build the answer** by comparing the leftmost and rightmost elements and adding whichever one was closer to `x`.

Something felt wrong because I was making decisions too early.

After discussing the problem step by step, I realized that this is **not a "pick the best" problem**.

It is actually an **"eliminate the worst" problem**.

That completely changed how I looked at the solution.

---

# Key Observation 1

Instead of selecting the closest elements,

start with the **entire array** as the candidate answer.

```text
[1,2,3,4,5]
```

The whole array obviously contains all possible answers.

The only problem is that it contains **more than `k` elements**.

So instead of building the answer,

I should repeatedly **remove one bad element** until only `k` elements remain.

---

# Key Observation 2

At any moment, only the two boundary elements can be removed.

Suppose the current window is:

```text
Left ---------------- Right
```

Compare:

```text
|arr[left] - x|

vs

|arr[right] - x|
```

The element with the **larger distance** from `x` is definitely worse and can be removed.

---

# Key Observation 3

If both distances are equal,

the problem says:

> Prefer the **smaller** element.

Therefore,

if both ends are equally far from `x`:

```text
Keep the smaller element

Remove the larger element
```

Since the array is sorted,

the larger element is always on the **right**.

So in case of a tie:

```text
Move the right pointer.
```

---

# Pattern Used

## Opposite Direction Two Pointers

Instead of expanding a window,

this problem **shrinks** the window.

Start with:

```text
Left Pointer  -> Beginning

Right Pointer -> End
```

While the window contains more than `k` elements:

1. Compare both ends.
2. Remove the worse candidate.
3. Continue shrinking.

When the window size becomes exactly `k`,

the remaining window is the answer.

---

# Optimized Solution

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int):
        left = 0
        right = len(arr) - 1

        while right - left + 1 > k:

            left_diff = abs(arr[left] - x)
            right_diff = abs(arr[right] - x)

            if left_diff <= right_diff:
                right -= 1
            else:
                left += 1

        return arr[left:right + 1]
```

---

# Dry Run

```text
arr = [1,2,3,4,5]

k = 4

x = 3
```

Initially:

```text
L               R

1 2 3 4 5
```

Compare:

```text
|1-3| = 2

|5-3| = 2
```

Both are equally far.

Tie-breaking rule:

```text
Keep smaller value.

Remove larger value.
```

So:

```text
Remove 5
```

Window becomes:

```text
1 2 3 4
```

Window size is now exactly `k`.

Return:

```text
[1,2,3,4]
```

---

# Complexity Analysis

## Time Complexity

Initially the window size is:

```text
n
```

It shrinks until it becomes:

```text
k
```

The loop runs:

```text
n - k
```

times.

Each iteration performs constant work.

Overall:

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

# Key Takeaways

* Don't always think about **building the answer**.
* Sometimes it is easier to **remove the bad candidates**.
* Maintain a valid window instead of creating a new list.
* Compare only the two boundary elements.
* Remove the element farther from `x`.
* If both are equally far, remove the **right** element because the problem prefers the smaller value.

---

# Concepts Practiced

✅ Arrays

✅ Opposite Direction Two Pointers

✅ Greedy Thinking

✅ Shrinking Window

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach                        | Time | Space |
| ------------------------------- | ---- | ----- |
| Shrinking Window (Two Pointers) | O(n) | O(1)  |

---

# Status

✅ Solved

✅ Understood that this is an **eliminate-the-worst** problem rather than a **pick-the-best** problem

✅ Learned how to maintain a shrinking window

✅ Learned how the tie-breaking rule affects pointer movement

✅ Successfully derived the optimal two-pointer solution through reasoning instead of memorizing it
