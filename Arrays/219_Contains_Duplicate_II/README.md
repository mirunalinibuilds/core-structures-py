# Contains Duplicate II

## Problem Statement

Given an integer array `nums` and an integer `k`, return `True` if there are two distinct indices `i` and `j` in the array such that:

```text
nums[i] == nums[j]
```

and

```text
|i - j| <= k
```

Otherwise, return `False`.

### Example 1

### Input

```python
nums = [1,2,3,1]
k = 3
```

### Output

```python
True
```

### Explanation

The number `1` appears at:

```python
Index 0
Index 3
```

Distance:

```python
3 - 0 = 3
```

Since:

```python
3 <= k
```

return `True`.

---

## LeetCode Link

https://leetcode.com/problems/contains-duplicate-ii/

---

## My Initial Thought Process

The first thing I noticed was that we need to know:

1. Whether a duplicate exists.
2. How far apart the duplicate indices are.

Example:

```python
nums = [1,2,3,1]
```

The duplicate value is:

```python
1
```

at:

```python
Index 0
Index 3
```

To calculate the distance, I need to remember where I saw each number previously.

This suggested using a Hash Map (Dictionary).

---

## Key Observation

For every number:

```text
Store the most recent index where it appeared.
```

Example:

```python
nums = [1,2,3,1]
```

As we iterate:

```python
{
    1: 0
}
```

```python
{
    1: 0,
    2: 1
}
```

```python
{
    1: 0,
    2: 1,
    3: 2
}
```

When we encounter:

```python
1
```

again at index:

```python
3
```

we can immediately find its previous index:

```python
seen[1] = 0
```

Distance:

```python
3 - 0 = 3
```

---

## Why Hash Map Works

The dictionary stores:

```python
number -> latest index
```

Example:

```python
{
    5: 2,
    8: 4,
    10: 7
}
```

Meaning:

```python
5 was last seen at index 2
8 was last seen at index 4
10 was last seen at index 7
```

This allows us to check duplicates in:

```text
O(1)
```

time.

---

## Optimized Solution

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in seen:

                if i - seen[num] <= k:
                    return True

            seen[num] = i

        return False
```

---

## Dry Run

Input:

```python
nums = [1,2,3,1]
k = 3
```

Initially:

```python
seen = {}
```

---

### Index 0

```python
num = 1
```

Store:

```python
seen = {1:0}
```

---

### Index 1

```python
num = 2
```

Store:

```python
seen = {
    1:0,
    2:1
}
```

---

### Index 2

```python
num = 3
```

Store:

```python
seen = {
    1:0,
    2:1,
    3:2
}
```

---

### Index 3

```python
num = 1
```

Already exists.

Previous index:

```python
seen[1] = 0
```

Distance:

```python
3 - 0 = 3
```

Check:

```python
3 <= 3
```

True.

Return:

```python
True
```

---

## Why We Update The Index

Consider:

```python
nums = [1,0,1,1]
k = 1
```

At index:

```python
2
```

we see:

```python
1
```

again.

Distance:

```python
2 - 0 = 2
```

Not valid.

However, we update:

```python
seen[1] = 2
```

Now when we reach:

```python
Index 3
```

Distance becomes:

```python
3 - 2 = 1
```

which satisfies the condition.

Therefore we always store the latest index.

---

## Complexity Analysis

Let:

```text
n = length of nums
```

### Time Complexity

Single pass through the array:

```text
O(n)
```

Dictionary lookup is:

```text
O(1)
```

on average.

---

### Space Complexity

In the worst case all elements are unique.

Dictionary stores:

```text
n elements
```

Therefore:

```text
O(n)
```

---

## Pattern Learned

### Hash Map + Index Tracking

Store information about previously seen elements.

Pattern:

```python
seen = {}

for i, num in enumerate(nums):

    if num in seen:
        # use previous information

    seen[num] = i
```

This pattern appears frequently in:

- Two Sum
- Contains Duplicate
- Contains Duplicate II
- Longest Substring Without Repeating Characters
- Top K Frequent Elements

---

## Key Takeaways

- Hash Maps are useful when we need fast lookups.
- Store values as keys and indices as values.
- Sometimes we need to remember previous occurrences rather than just checking existence.
- Updating stored information is often as important as checking it.
- Many array problems become efficient using a Hash Map.

---

## Concepts Practiced

✅ Arrays

✅ Hash Maps (Dictionary)

✅ Index Tracking

✅ Distance Calculation

✅ Single Pass Traversal

✅ Time Complexity Optimization

---

## Final Complexity

| Approach | Time | Space |
|-----------|--------|--------|
| Brute Force | O(n²) | O(1) |
| Hash Map | O(n) | O(n) |

---

## Status

✅ Solved

✅ Learned Hash Map Pattern

✅ Learned Index Tracking

✅ Learned Previous Occurrence Storage

✅ Understood O(n²) → O(n) Optimization
