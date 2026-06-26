# Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters.

---

## Example

### Input

```python
s = "abcabcbb"
```

### Output

```python
3
```

### Explanation

The longest substring without repeating characters is:

```python
"abc"
```

whose length is:

```python
3
```

---

## LeetCode Link

https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

# My Initial Thought Process

Before attempting this problem, I had just learned **Variable Size Sliding Window**.

The first thing I identified was that the window size is **not fixed**.

As we keep expanding the window:

- If there are no duplicate characters, we continue expanding.
- As soon as a duplicate appears, the window becomes invalid.
- We then keep shrinking the window until the duplicate is removed.

Initially, I was confused about:

- whether to use an `if` or a `while`
- whether to use a `set` or a `dictionary`
- where exactly to update the maximum length

After understanding the sliding window pattern, the solution became much clearer.

---

# Key Observation

The current window should always contain **unique characters only**.

Whenever the current character already exists inside the window,

the window becomes invalid.

Instead of restarting everything,

we simply remove characters from the left until the duplicate disappears.

Then we continue expanding the window.

---

# Optimized Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            current_len = right - left + 1
            max_len = max(max_len, current_len)

        return max_len
```

---

# Dry Run

Example:

```python
s = "abcabcbb"
```

Initially:

```
Window = ""
Seen = {}
```

Expand:

```
"a"
```

Window becomes:

```
"a"
```

Length:

```
1
```

Expand:

```
"ab"
```

Length:

```
2
```

Expand:

```
"abc"
```

Length:

```
3
```

Next character:

```
'a'
```

Duplicate found.

Shrink the window:

Remove:

```
'a'
```

Window becomes:

```
"bc"
```

Now add the new:

```
'a'
```

Window:

```
"bca"
```

Continue this process until the end of the string.

Maximum length found:

```
3
```

---

# Why This Works

The window always contains only unique characters.

Whenever a duplicate appears,

we repeatedly remove characters from the left until the duplicate no longer exists.

After that,

we safely add the current character and update the answer.

Each character is added to the set at most once and removed at most once.

---

# Complexity Analysis

Let:

```
n = length of string
```

### Time Complexity

Each character is:

- added once
- removed once

Therefore:

```
O(n)
```

---

### Space Complexity

The set stores only characters currently inside the window.

Worst case:

```
O(n)
```

---

# Pattern Learned

## Variable Size Sliding Window + Set

General template:

```python
left = 0

for right in range(len(data)):

    while window_is_invalid:
        # shrink window

    # expand window

    # update answer
```

Unlike the previous sliding window problem,

here the window is considered invalid whenever a duplicate character exists.

---

# Key Takeaways

- Sliding Window can also be applied to strings.
- A `while` loop is required because removing one character may not remove the duplicate.
- A `set` is enough to keep track of characters currently inside the window.
- Always update the answer only after the window becomes valid.

---

# Concepts Practiced

✅ Strings

✅ Hash Set

✅ Variable Size Sliding Window

✅ Two Pointers

✅ Time Complexity Analysis

---

# Final Complexity

| Approach | Time | Space |
|----------|------|-------|
| Sliding Window + Set | O(n) | O(n) |

---

# Status

✅ Solved

✅ Learned Variable Size Sliding Window on Strings

✅ Learned to use a Hash Set with Sliding Window

✅ Understood why `while` is needed instead of `if`

✅ Understood the correct order of expanding, shrinking and updating the answer
