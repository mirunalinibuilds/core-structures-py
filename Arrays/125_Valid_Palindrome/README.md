# 125. Valid Palindrome

## Problem Statement

A phrase is considered a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Example

**Input**

```text
s = "A man, a plan, a canal: Panama"
```

**Output**

```text
true
```

**Explanation**

After removing spaces, punctuation and converting to lowercase:

```text
amanaplanacanalpanama
```

Reading from left to right and right to left gives the same string.

---

## LeetCode Link

https://leetcode.com/problems/valid-palindrome/

---

# My Thought Process

Since the problem asks us to ignore spaces, punctuation and uppercase letters, my first step was to clean the string.

I converted every character to lowercase and kept only alphanumeric characters.

Once the string was cleaned, I noticed that checking whether it is a palindrome becomes straightforward.

Instead of reversing the string, I wanted to learn the **Two Pointers** pattern.

I placed one pointer at the beginning and another at the end of the string.

If both characters match, I move both pointers towards the center.

If any pair doesn't match, the string is not a palindrome.

---

# Optimized Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
```

---

# Dry Run

Input:

```text
"A man, a plan, a canal: Panama"
```

After preprocessing:

```text
amanaplanacanalpanama
```

Pointers:

```text
a m a n a p l a n a c a n a l p a n a m a
^                                       ^
L                                       R
```

Compare:

```
a == a ✅
```

Move both pointers.

```
m == m ✅
```

Move both pointers.

```
a == a ✅
```

Continue comparing until both pointers meet.

No mismatch is found.

Return:

```text
True
```

---

# Why Two Pointers Works

A palindrome reads the same from both directions.

Instead of checking every possible pair or reversing the string, we only compare the first and last characters simultaneously.

After each successful comparison, both pointers move one step towards the center.

Each character is visited only once.

---

# Complexity Analysis

## Time Complexity

Cleaning the string:

```
O(n)
```

Palindrome checking:

```
O(n)
```

Overall:

```
O(n)
```

---

## Space Complexity

A new cleaned string is created.

```
O(n)
```

---

# Pattern Learned

## Opposite-End Two Pointers

Place one pointer at the beginning and another at the end.

Compare both characters.

- If they match, move both pointers inward.
- If they don't match, the answer is immediately `False`.

This is one of the most common Two Pointer patterns.

---

# Key Takeaways

- Clean the input before solving the main problem.
- Two Pointers can compare elements from both ends efficiently.
- No nested loops are required.
- Each character is processed at most once.

---

# Concepts Practiced

✅ Strings

✅ String Preprocessing

✅ Two Pointers

✅ Opposite-End Two Pointer Pattern

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Two Pointers | O(n) | O(n) |

---

# Status

✅ Solved

✅ Learned Opposite-End Two Pointers

✅ Understood how to compare characters from both ends efficiently

✅ First Two Pointer problem solved independently
