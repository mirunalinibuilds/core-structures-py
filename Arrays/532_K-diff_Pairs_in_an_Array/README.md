# 532. K-diff Pairs in an Array

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of **unique** `k-diff` pairs in the array.

A `k-diff` pair is defined as:

- `i != j`
- `|nums[i] - nums[j]| == k`

### Example

**Input**

```text
nums = [3,1,4,1,5]
k = 2
```

**Output**

```text
2
```

**Explanation**

The unique pairs are:

```text
(1,3)
(3,5)
```

---

## LeetCode Link

https://leetcode.com/problems/k-diff-pairs-in-an-array/

---

# My Thought Process

Initially, I tried solving this problem using the Two Pointer pattern because it was part of my Two Pointer learning journey.

However, I struggled to understand how the pointers should move. I first assumed this was an **Opposite-End Two Pointer** problem, but later realized that assumption was incorrect.

Instead of forcing the pattern, I stepped back and focused on understanding the problem itself.

The key realization was:

For every number `num`, I simply need to check whether another number with value `num + k` exists.

This immediately suggested using a **Hash Set**, since membership checks are `O(1)`.

---

# Important Observation

For every unique number:

```text
Current Number = num
```

Search for:

```text
num + k
```

If it exists, then one unique pair is found.

Example:

```text
nums = [1,3,5]
k = 2
```

For:

```text
1
```

Search for:

```text
3
```

Found.

For:

```text
3
```

Search for:

```text
5
```

Found.

For:

```text
5
```

Search for:

```text
7
```

Not found.

Answer:

```text
2
```

---

# Why We Iterate Over a Set

Suppose:

```text
nums = [1,1,3]
k = 2
```

If we iterate over the array directly, we would count:

```text
(1,3)
(1,3)
```

twice.

The problem asks for **unique pairs**.

So we first convert the array into a set:

```python
seen = set(nums)
```

Now each unique number is processed only once.

---

# Special Case: k == 0

This is the only tricky part.

Suppose:

```text
nums = [1]
k = 0
```

A set contains:

```text
{1}
```

Checking:

```text
1 + 0 = 1
```

would incorrectly count one pair.

But there is only one occurrence of `1`.

The problem requires:

```text
i != j
```

Therefore, we need at least **two occurrences** of the same value.

For this reason, when:

```text
k == 0
```

we use a **Frequency Map (Dictionary)** instead of a set.

Only numbers appearing at least twice contribute one unique pair.

---

# Optimized Solution (Hashing)

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        if k < 0:
            return 0

        count = 0

        if k > 0:

            seen = set(nums)

            for num in seen:
                if num + k in seen:
                    count += 1

            return count

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for value in freq.values():
            if value >= 2:
                count += 1

        return count
```

---

# Dry Run

Input:

```text
nums = [3,1,4,1,5]
k = 2
```

Set:

```text
{1,3,4,5}
```

Current:

```text
1
```

Search:

```text
3
```

Found.

Count = 1

Current:

```text
3
```

Search:

```text
5
```

Found.

Count = 2

Current:

```text
4
```

Search:

```text
6
```

Not found.

Current:

```text
5
```

Search:

```text
7
```

Not found.

Final Answer:

```text
2
```

---

# Complexity Analysis

## Time Complexity

Building the set:

```
O(n)
```

Traversing the set:

```
O(n)
```

Overall:

```
O(n)
```

---

## Space Complexity

Set / Dictionary:

```
O(n)
```

---

# Pattern Learned

## Hashing

Instead of searching the array repeatedly, store values inside a Hash Set for constant-time lookup.

When:

```text
k > 0
```

Hash Set is sufficient.

When:

```text
k == 0
```

A Frequency Map is required because we need to know whether a value appears **at least twice**.

---

# Key Takeaways

- Always understand the problem before choosing a pattern.
- Think from the perspective of one number:
  - "Does `num + k` exist?"
- Hash Sets are useful for fast existence checks.
- Frequency Maps are required whenever duplicate counts matter.
- `k == 0` is an important edge case because of the condition `i != j`.

---

# Concepts Practiced

✅ Arrays

✅ Hash Set

✅ Hash Map (Dictionary)

✅ Frequency Counting

✅ Edge Case Handling

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Hashing | O(n) | O(n) |

---

# Status

✅ Solved

✅ Learned how to convert a brute-force search into constant-time lookups using hashing

✅ Understood when to use a Hash Set vs a Frequency Map

✅ Learned to handle the special `k == 0` edge case
