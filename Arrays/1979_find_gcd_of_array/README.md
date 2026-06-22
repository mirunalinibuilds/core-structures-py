# Find Greatest Common Divisor of Array

## Problem Statement

Given an integer array `nums`, return the greatest common divisor (GCD) of the smallest number and the largest number in the array.

The Greatest Common Divisor (GCD) of two numbers is the largest positive integer that divides both numbers without leaving a remainder.

---

## Example

### Input

```python
nums = [2,5,6,9,10]
```

### Output

```python
2
```

### Explanation

Smallest element:

```python
2
```

Largest element:

```python
10
```

GCD:

```python
gcd(2,10) = 2
```

---

## LeetCode Link

https://leetcode.com/problems/find-greatest-common-divisor-of-array/

---

# My Initial Thought Process

At first glance, it might seem like we need to find the GCD of all elements in the array.

However, reading the problem carefully reveals that we only need the GCD of:

- The minimum element
- The maximum element

Therefore, the problem can be broken down into:

1. Find the smallest element.
2. Find the largest element.
3. Find the GCD of those two values.

---

# Key Observation

The problem does **not** ask for:

```text
GCD of all elements
```

It asks for:

```text
GCD of minimum element and maximum element
```

So we can directly use:

```python
math.gcd(min(nums), max(nums))
```

---

# Solution

```python
import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))
```

---

# Dry Run

### Input

```python
nums = [2,5,6,9,10]
```

Find minimum:

```python
min(nums) = 2
```

Find maximum:

```python
max(nums) = 10
```

Find GCD:

```python
gcd(2,10)
```

Factors of 2:

```text
1, 2
```

Factors of 10:

```text
1, 2, 5, 10
```

Greatest Common Divisor:

```python
2
```

Return:

```python
2
```

---

# Python Concepts Learned

## min()

Returns the smallest element in an iterable.

Example:

```python
min([5,2,8,1])
```

Output:

```python
1
```

---

## max()

Returns the largest element in an iterable.

Example:

```python
max([5,2,8,1])
```

Output:

```python
8
```

---

## math.gcd()

Returns the Greatest Common Divisor of two integers.

Example:

```python
import math

math.gcd(12,18)
```

Output:

```python
6
```

Because:

```text
Factors of 12:
1, 2, 3, 4, 6, 12

Factors of 18:
1, 2, 3, 6, 9, 18
```

Largest common factor:

```python
6
```

---

# Complexity Analysis

## Time Complexity

### Finding Minimum

```text
O(n)
```

### Finding Maximum

```text
O(n)
```

### Finding GCD

```text
O(log(min(a,b)))
```

Overall:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

No extra data structures are used.

---

# Pattern Learned

## Array Traversal

Use built-in functions to efficiently find:

- Minimum element
- Maximum element

---

## Mathematical Observation

Many coding problems become easier when we carefully read the requirement.

Instead of solving:

```text
GCD of entire array
```

we only needed:

```text
GCD of minimum and maximum element
```

The key insight was understanding the problem correctly before coding.

---

# Key Takeaways

- Read the problem carefully before designing an algorithm.
- Identify exactly what is being asked.
- Use built-in Python functions when appropriate.
- Mathematical observations can simplify a problem significantly.
- Sometimes the optimal solution is only a few lines long.

---

# Concepts Practiced

✅ Arrays

✅ Minimum and Maximum in Arrays

✅ Mathematical Observation

✅ Greatest Common Divisor (GCD)

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Metric | Complexity |
|----------|----------|
| Time Complexity | O(n) |
| Space Complexity | O(1) |

---

## Status

✅ Solved

✅ Understood Problem Requirement

✅ Learned GCD Concept

✅ Learned Mathematical Observation Pattern
