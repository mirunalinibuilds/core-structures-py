# Self Dividing Numbers

## Problem Statement

A self-dividing number is a number that is divisible by every digit it contains.

For example:

```python
128
```

is a self-dividing number because:

```python
128 % 1 == 0
128 % 2 == 0
128 % 8 == 0
```

Given two integers `left` and `right`, return a list of all self-dividing numbers in the range `[left, right]`.

---

## Example

### Input

```python
left = 1
right = 22
```

### Output

```python
[1,2,3,4,5,6,7,8,9,11,12,15,22]
```

---

## LeetCode Link

https://leetcode.com/problems/self-dividing-numbers/

---

# My Initial Thought Process

To determine whether a number is self-dividing:

1. Extract all digits of the number.
2. Check every digit.
3. If any digit is:
   - Equal to 0
   - Does not divide the number evenly

then the number is not self-dividing.

If all digits pass the check, add the number to the result list.

---

# Key Observations

## Observation 1

A self-dividing number must be divisible by every digit it contains.

Example:

```python
128
```

Check:

```python
128 % 1 == 0
128 % 2 == 0
128 % 8 == 0
```

Therefore:

```python
128
```

is self-dividing.

---

## Observation 2

A number containing:

```python
0
```

can never be self-dividing.

Example:

```python
10
```

because:

```python
10 % 0
```

is invalid.

Therefore:

```python
10
```

is not a self-dividing number.

---

# Approach

For every number in the range:

1. Convert the number into individual digits.
2. Check every digit.
3. If a digit is zero, reject the number.
4. If the number is not divisible by a digit, reject the number.
5. If all digits pass, add the number to the answer list.

---

# Solution

```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_nums = []

        for i in range(left, right + 1):

            is_self_dividing = True
            digits = [int(char) for char in str(i)]

            for digit in digits:

                if digit == 0 or i % digit != 0:
                    is_self_dividing = False
                    break

            if is_self_dividing:
                self_dividing_nums.append(i)

        return self_dividing_nums
```

---

# Dry Run

### Example

```python
i = 128
```

Convert to digits:

```python
[1, 2, 8]
```

Check:

```python
128 % 1 == 0
```

```python
128 % 2 == 0
```

```python
128 % 8 == 0
```

All conditions pass.

Add:

```python
128
```

to the answer list.

---

### Example

```python
i = 26
```

Digits:

```python
[2, 6]
```

Check:

```python
26 % 2 == 0
```

```python
26 % 6 != 0
```

Fails.

Do not add the number.

---

# Python Concepts Learned

## Converting Number to Digits

```python
digits = [int(char) for char in str(i)]
```

Example:

```python
i = 128
```

becomes:

```python
[1, 2, 8]
```

---

## Modulus Operator (%)

Used to check divisibility.

Example:

```python
12 % 3
```

Output:

```python
0
```

meaning:

```python
12
```

is divisible by:

```python
3
```

---

## break Statement

```python
break
```

Stops the loop immediately.

Once a digit fails:

```python
digit == 0
```

or

```python
i % digit != 0
```

there is no need to check remaining digits.

---

# Complexity Analysis

Let:

```text
n = right - left + 1
```

and

```text
d = number of digits
```

---

## Time Complexity

For each number:

```text
O(d)
```

For all numbers:

```text
O(n × d)
```

---

## Space Complexity

```text
O(d)
```

because we create a list of digits.

---

# Alternative Optimization

Instead of converting the number into a string, digits can be extracted using:

```python
digit = temp % 10
temp = temp // 10
```

This reduces extra space usage to:

```text
O(1)
```

while maintaining the same time complexity.

---

# Pattern Learned

## Digit Extraction / Digit Validation Pattern

Many math-based problems require checking every digit of a number.

General structure:

```python
for each number:

    for each digit:

        validate digit

    if all digits are valid:
        accept number
```

Common examples:

- Self Dividing Numbers
- Palindrome Number
- Armstrong Number
- Happy Number
- Sum of Digits Problems

---

## Early Rejection Pattern

As soon as one condition fails:

```python
is_valid = False
break
```

stop checking further.

This avoids unnecessary work.

---

# Key Takeaways

- Break complex problems into smaller checks.
- Validate digits one by one.
- Handle edge cases such as digit `0`.
- Use early termination when possible.
- Learn common digit-processing patterns.

---

# Concepts Practiced

✅ Arrays (Result Collection)

✅ Number Manipulation

✅ Digit Processing

✅ Modulus Operator

✅ Divisibility Checks

✅ Early Termination (`break`)

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Metric | Complexity |
|----------|----------|
| Time Complexity | O(n × d) |
| Space Complexity | O(d) |

---

## Status

✅ Solved

✅ Understood Digit Processing

✅ Learned Divisibility Checks

✅ Learned Early Rejection Pattern

✅ Learned Number Validation Pattern
