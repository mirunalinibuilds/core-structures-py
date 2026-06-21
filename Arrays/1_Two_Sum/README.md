# Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that:

- Each input has exactly one solution.
- You may not use the same element twice.
- The answer can be returned in any order.

### Example

#### Input

```python
nums = [2,7,11,15]
target = 9
```

#### Output

```python
[0,1]
```

#### Explanation

```python
nums[0] + nums[1] = 2 + 7 = 9
```

---

## LeetCode Link

https://leetcode.com/problems/two-sum/

---

# My Initial Thought Process

The most straightforward approach is to check every possible pair.

For each element:

- Compare it with every element after it.
- If the sum equals the target, return the indices.

Example:

```python
2 + 7 = 9 ✓
2 + 11 = 13
2 + 15 = 17
```

This works, but it becomes slow for large arrays because every element is compared with many others.

---

# Brute Force Solution

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n²)
```

Nested loops are used.

### Space Complexity

```text
O(1)
```

No extra data structure is used.

---

# Optimized Approach (Hash Map)

Instead of checking every possible pair, we can store previously seen numbers in a dictionary.

For every number:

1. Calculate the required complement.

```python
need = target - current_number
```

2. Check if the complement already exists in the dictionary.

3. If it exists, we have found the answer.

4. Otherwise, store the current number and its index.

---

## Dry Run

### Input

```python
nums = [2,7,11,15]
target = 9
```

### Iteration 1

Current Number:

```python
2
```

Required Complement:

```python
7
```

Dictionary:

```python
{2: 0}
```

---

### Iteration 2

Current Number:

```python
7
```

Required Complement:

```python
2
```

Since `2` already exists in the dictionary:

```python
2 + 7 = 9
```

Answer:

```python
[0,1]
```

---

# Optimized Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return seen[need],i
            else:
                seen[nums[i]] = i
```

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

Reason:

- Single traversal of the array.
- Dictionary lookup takes O(1) on average.

---

### Space Complexity

```text
O(n)
```

Reason:

- In the worst case, every element is stored in the dictionary.

---

# Pattern Learned

## 1. Hash Map / Dictionary

Store information that allows fast lookups.

```python
seen[value] = index
```

Lookup:

```python
if need in seen:
```

Average lookup time:

```text
O(1)
```

---

## 2. Complement Pattern

Instead of asking:

```text
Which pair adds up to target?
```

Ask:

```text
For the current number,
what number do I need to reach the target?
```

Formula:

```python
need = target - current_number
```

Example:

```python
target = 9
current = 7

need = 2
```

Then simply check if `2` has already been seen.

---

## 3. Array + Hash Map Pattern

This is one of the most important DSA patterns.

Structure:

```python
for element in array:

    if required_value in hashmap:
        return answer

    hashmap[current_value] = useful_information
```

Common problems using this pattern:

- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements
- Majority Element
- Frequency Counting Problems

---

# Key Takeaways

- Always solve the brute force solution first.
- Look for repeated work.
- Use a Hash Map when fast lookups are needed.
- Think in terms of complements.
- Trade extra space for faster execution when appropriate.

---

# Concepts Practiced

✅ Arrays

✅ Hash Maps (Dictionary)

✅ Complement Lookup

✅ Time Complexity Analysis

✅ Space Complexity Analysis

✅ Brute Force vs Optimized Solutions

✅ Pattern Recognition

---

# Final Complexity

| Approach | Time | Space |
|-----------|--------|--------|
| Brute Force | O(n²) | O(1) |
| Hash Map | O(n) | O(n) |

---

## Status

✅ Solved

✅ Understood Brute Force Solution

✅ Understood Optimized Solution

✅ Learned Hash Map Pattern
