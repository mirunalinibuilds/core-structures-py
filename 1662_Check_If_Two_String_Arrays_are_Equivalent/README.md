# 1662. Check If Two String Arrays are Equivalent

## Problem Statement

Two string arrays are considered **equivalent** if they represent the same string when all their elements are concatenated in order.

Given two string arrays `word1` and `word2`, return `true` if they are equivalent, otherwise return `false`.

---

## Example

**Input**

```text
word1 = ["ab", "c"]
word2 = ["a", "bc"]
```

**Output**

```text
true
```

**Explanation**

Concatenating both arrays gives:

```text
word1 → "abc"

word2 → "abc"
```

Since both strings are identical, the answer is **true**.

---

## LeetCode Link

https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

---

# My Learning Journey

When I first looked at the problem, I noticed that comparing the arrays directly would not work because the strings were split differently.

For example,

```text
["ab", "c"]
```

and

```text
["a", "bc"]
```

look completely different as arrays.

However, the problem statement says they should be compared **after concatenating all the strings**.

That completely changed how I approached the problem.

---

# My First Thought

Instead of comparing the arrays,

I decided to convert both arrays into their complete strings.

For the first array,

```text
["ab", "c"]
```

I built

```text
"abc"
```

For the second array,

```text
["a", "bc"]
```

I also built

```text
"abc"
```

Once both arrays were transformed into their final string representation,

the comparison became very simple.

---

# Biggest Realization

I wasn't actually comparing two arrays.

I was comparing **their final representation**.

Instead of worrying about how the strings were split,

I only cared about the complete string they represented.

This taught me an important problem-solving idea:

> Sometimes it is easier to transform both inputs into a common representation before comparing them.

---

# Pattern Used

## Normalize → Compare

Rather than comparing the original inputs directly,

I first transformed both arrays into their canonical representation.

```text
["ab","c"]

↓

"abc"
```

```text
["a","bc"]

↓

"abc"
```

Once both inputs had the same representation,

checking equality became a simple string comparison.

This normalization technique appears in many interview problems.

---

# Optimized Solution

```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_new1, word_new2 = '', ''

        for word in word1:
            word_new1 += word

        for word in word2:
            word_new2 += word

        return word_new1 == word_new2
```

---

# Dry Run

```text
word1 = ["ab", "c"]

word2 = ["a", "bc"]
```

Initially,

```text
word_new1 = ""

word_new2 = ""
```

Loop through `word1`

```text
word_new1 = "ab"

word_new1 = "abc"
```

Loop through `word2`

```text
word_new2 = "a"

word_new2 = "abc"
```

Finally,

```text
"abc" == "abc"
```

Return

```text
True
```

---

# Complexity Analysis

## Time Complexity

Every character from both arrays is visited exactly once.

```text
O(n + m)
```

where

* `n` = total number of characters in `word1`
* `m` = total number of characters in `word2`

---

## Space Complexity

Two additional strings are created.

```text
O(n + m)
```

---

# Key Takeaways

* The arrays themselves are not compared.
* First, concatenate all strings in each array.
* Compare the final strings.
* Converting different representations into the same representation often simplifies the problem.
* Sometimes preprocessing is the easiest way to solve a problem.

---

# Concepts Practiced

✅ Arrays

✅ Strings

✅ String Concatenation

✅ Simulation

✅ Normalize → Compare Pattern

✅ Time Complexity Analysis

✅ Space Complexity Analysis

---

# Final Complexity

| Approach                | Time     | Space    |
| ----------------------- | -------- | -------- |
| Concatenate and Compare | O(n + m) | O(n + m) |

---

# Status

✅ Solved

✅ Learned that different array representations can represent the same final string

✅ Understood the **Normalize → Compare** pattern

✅ Learned to build complete strings using iteration

✅ Successfully solved a string simulation problem by transforming both inputs into a common representation before comparing them
