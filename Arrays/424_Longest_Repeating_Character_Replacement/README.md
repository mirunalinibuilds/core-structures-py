# 424. Longest Repeating Character Replacement

## Problem Statement

You are given a string `s` consisting of only uppercase English letters and an integer `k`.

You can perform **at most `k` character replacements**.

In one replacement, you can change any character into any other uppercase English letter.

Return the **length of the longest substring** that can be transformed into a string containing **only one repeating character**.

---

## Example

**Input**

```text
s = "AABABBA"
k = 1
```

**Output**

```text
4
```

**Explanation**

One possible transformation is:

```text
AABA → AAAA
```

by replacing one `'B'` with `'A'`.

So the longest valid substring has length **4**.

---

## LeetCode Link

https://leetcode.com/problems/longest-repeating-character-replacement/

---

# My Learning Journey

When I first read the problem, I immediately recognized that this was a **Sliding Window** problem because we were looking for the **longest valid substring**.

The difficult part wasn't creating the window.

The difficult part was answering:

> **When is my current window valid?**

Unlike the previous Sliding Window problems, there was no sum to maintain and no duplicate restriction.

Instead, I had to discover an entirely new window validity condition.

---

# My First Thought

Initially, I thought:

> A valid window means every character inside it should already be the same.

For example,

```text
AAAA
```

would be valid,

while

```text
AAB
```

would be invalid.

This was incorrect.

The problem never says the window must already contain identical characters.

It says we are allowed to perform **at most `k` replacements**.

That completely changes how we think about validity.

---

# Biggest Realization

Suppose my current window is

```text
A A B A C
```

The frequency map becomes

```text
A → 3

B → 1

C → 1
```

If I want every character to become the same,

which character should I choose?

Obviously,

```text
A
```

because it already appears the most.

Replacing every other character with the **most frequent character** always requires the fewest replacements.

That was the key observation.

---

# Key Observation 1

Suppose the window is

```text
A A B A C
```

Window length:

```text
5
```

Highest frequency:

```text
3
```

The remaining characters are

```text
B

C
```

There are

```text
5 - 3 = 2
```

characters that need to be replaced.

This led me to the most important formula in the problem:

```text
Replacements Needed = Window Length − Maximum Frequency
```

---

# Key Observation 2

The problem allows only

```text
k
```

replacements.

Therefore,

a window is valid only if

```text
Window Length − Maximum Frequency ≤ k
```

If this condition becomes false,

the current window is no longer valid,

so the left pointer must move until the window becomes valid again.

This is exactly the Variable Sliding Window pattern I learned earlier.

---

# Pattern Used

## Variable Sliding Window + Frequency Map

Instead of maintaining a running sum,

the window maintains a property.

The property is:

```text
Window Length − Maximum Frequency ≤ k
```

Whenever this condition becomes false,

the window is shrunk from the left until it becomes valid again.

---

# Why a Frequency Map?

A set was enough in **Longest Substring Without Repeating Characters** because I only needed to know whether a character existed.

This problem is different.

I need to know

> Which character appears the most inside the current window?

A frequency map stores both the character and its count.

Example:

```python
{
    'A': 3,
    'B': 1,
    'C': 1
}
```

This allows me to calculate the minimum replacements needed.

---

# Biggest Realization

The Sliding Window template never changed.

Only the **validity condition** changed.

Previous problem:

```text
Window is valid when all characters are unique.
```

This problem:

```text
Window is valid when

Window Length − Maximum Frequency ≤ k
```

That helped me understand that many Sliding Window problems share the same structure.

Only the rule that defines a valid window changes.

---

# Optimized Solution

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        ans = 0
        max_freq = 0

        for right in range(len(s)):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            max_freq = max(max_freq, freq[ch])

            window_length = right - left + 1

            if window_length - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            else:
                ans = max(ans, window_length)

        return ans
```

---

# Dry Run

```text
s = "AABABBA"

k = 1
```

Initially,

```text
left = 0

right = 0

Window = A
```

Frequency:

```text
A → 1
```

Window length:

```text
1
```

Maximum frequency:

```text
1
```

Replacements needed:

```text
1 − 1 = 0
```

Valid.

Answer becomes

```text
1
```

---

Expand further:

```text
A A B A
```

Frequency:

```text
A → 3

B → 1
```

Window length:

```text
4
```

Maximum frequency:

```text
3
```

Replacements needed:

```text
4 − 3 = 1
```

Still valid because

```text
1 ≤ k
```

Answer becomes

```text
4
```

Whenever the replacements required become greater than `k`, the left pointer moves until the window becomes valid again.

---

# Complexity Analysis

## Time Complexity

Each character enters the window once and leaves the window at most once.

```text
O(n)
```

---

## Space Complexity

The frequency map stores counts for the characters inside the window.

Since the string contains only uppercase English letters, the map stores at most 26 entries.

```text
O(1)
```

(General case: `O(m)`, where `m` is the number of distinct characters.)

---

# Key Takeaways

* This is an Advanced Variable Sliding Window problem.
* A frequency map is required because we need character counts.
* Always convert the window into the **most frequent character**, since that minimizes replacements.
* The number of replacements needed is:

```text
Window Length − Maximum Frequency
```

* The window is valid when:

```text
Window Length − Maximum Frequency ≤ k
```

* The Sliding Window template remains the same; only the validity condition changes.

---

# Concepts Practiced

✅ Sliding Window

✅ Variable Sliding Window

✅ Frequency Map (Dictionary)

✅ Hash Map

✅ Window Validity

✅ Greedy Observation

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach                                | Time | Space |
| --------------------------------------- | ---- | ----- |
| Variable Sliding Window + Frequency Map | O(n) | O(1)  |

---

# Status

✅ Solved

✅ Learned how to use a frequency map inside a Sliding Window

✅ Understood that a valid window is determined by a condition, not by the characters already being equal

✅ Derived the formula:

```text
Window Length − Maximum Frequency
```

to calculate the minimum replacements required

✅ Learned that Sliding Window problems are mostly about discovering the correct **window validity condition**

✅ Successfully solved my second property-based Sliding Window problem by identifying the validity rule instead of memorizing the algorithm
