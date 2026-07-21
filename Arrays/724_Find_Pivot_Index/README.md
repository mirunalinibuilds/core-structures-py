# 724. Find Pivot Index

## Problem Statement

Given an integer array `nums`, calculate the **pivot index** of the array.

The pivot index is the index where:

- The sum of all the numbers **strictly to the left** of the index
- is equal to
- The sum of all the numbers **strictly to the right** of the index.

If multiple pivot indices exist, return the **leftmost** pivot index.

If no such index exists, return `-1`.

---

## Example

### Input

```text
nums = [1,7,3,6,5,6]
```

### Output

```text
3
```

### Explanation

```text
Left Side

1 + 7 + 3 = 11

Right Side

5 + 6 = 11
```

Both sums are equal.

Therefore,

```text
Pivot Index = 3
```

---

## LeetCode Link

https://leetcode.com/problems/find-pivot-index/

---

# My Learning Journey

Initially, I thought of solving this problem by building **two arrays**.

- A Prefix Sum array storing the cumulative sum from the left.
- A Suffix Sum array storing the cumulative sum from the right.

Then for every index, I planned to compare:

```text
Left Sum

vs

Right Sum
```

While implementing this, I realized something important.

The pivot element itself should **not** be included in either side.

That means if the current index is the pivot,

the comparison should be between:

```text
sum_left[i - 1]

and

sum_right[i + 1]
```

This helped me understand what Prefix and Suffix arrays actually represent instead of blindly applying formulas.

After solving it this way, I learned an even better solution that uses only constant extra space.

---

# Key Observation 1

Suppose we already know the **total sum** of the array.

For example,

```text
nums

[1,7,3,6,5,6]

Total = 28
```

Now imagine standing at some index.

If we already know:

- Total Sum
- Left Sum

then we can calculate the Right Sum immediately.

---

# Key Observation 2

At every index,

the total array can be divided into three parts.

```text
Left Sum | Current Element | Right Sum
```

Since

```text
Total Sum

=

Left Sum

+

Current Element

+

Right Sum
```

we can rearrange it as

```text
Right Sum

=

Total Sum

-

Left Sum

-

Current Element
```

This completely eliminates the need for a Suffix Sum array.

---

# Biggest Realization

The breakthrough for me was understanding that I don't always need to store extra information.

Initially, I built both Prefix and Suffix arrays.

Then I realized:

If something can be derived mathematically,

there is no need to store it separately.

Since the Right Sum can always be computed from the Total Sum and Left Sum,

the Suffix Sum array becomes unnecessary.

This reduced the extra space from **O(n)** to **O(1)**.

---

# Why Update `left_sum` After Comparison?

Initially,

```text
left_sum = 0
```

because there are no elements to the left of index `0`.

At every iteration,

we first compute

```text
right_sum
```

and compare

```text
left_sum == right_sum
```

Only after checking the current index do we update

```python
left_sum += nums[i]
```

If we updated first,

the pivot element would incorrectly become part of the left side.

---

# Pattern Used

## Prefix Sum

Instead of storing both left and right cumulative sums,

Prefix Sum is combined with the Total Sum.

The Right Sum is calculated dynamically using:

```text
Right Sum

=

Total Sum

-

Left Sum

-

Current Element
```

This achieves the same result while using constant extra memory.

---

# Optimized Solution

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):

            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
```

---

# Dry Run

Suppose

```text
nums = [1,7,3,6,5,6]
```

Initially,

```text
Total = 28

Left = 0
```

---

### Index = 0

```text
Current = 1

Right

28 - 0 - 1 = 27
```

Compare

```text
0 == 27

No
```

Update

```text
Left = 1
```

---

### Index = 1

```text
Current = 7

Right

28 - 1 - 7 = 20
```

Compare

```text
1 == 20

No
```

Update

```text
Left = 8
```

---

### Index = 2

```text
Current = 3

Right

28 - 8 - 3 = 17
```

Compare

```text
8 == 17

No
```

Update

```text
Left = 11
```

---

### Index = 3

```text
Current = 6

Right

28 - 11 - 6 = 11
```

Compare

```text
11 == 11

Yes
```

Return

```text
3
```

---

# Complexity Analysis

## Time Complexity

We traverse the array only once.

```text
O(n)
```

---

## Space Complexity

Only two extra variables are maintained.

```text
O(1)
```

---

# Key Takeaways

- Prefix Sum can be optimized using mathematical observations.
- The pivot element should never be included in either side.
- Right Sum does not need to be stored separately.
- If the Total Sum is known, Right Sum can be computed instantly.
- Update `left_sum` **after** checking the pivot.
- Always ask whether extra memory can be replaced with a formula.

---

# Concepts Practiced

✅ Arrays

✅ Prefix Sum

✅ Running Sum

✅ Mathematical Observation

✅ Space Optimization

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Prefix Sum + Running Left Sum | O(n) | O(1) |

---

# Status

✅ Solved

✅ Learned how to identify the pivot using Prefix Sum

✅ Understood why the pivot element is excluded from both sides

✅ Learned to derive Right Sum instead of storing a Suffix Sum array

✅ Reduced space complexity from **O(n)** to **O(1)**

✅ Strengthened my understanding of Prefix Sum optimization through mathematical reasoning
