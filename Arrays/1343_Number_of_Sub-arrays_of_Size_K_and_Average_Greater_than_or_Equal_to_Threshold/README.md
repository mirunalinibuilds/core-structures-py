# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

## Problem Statement

Given an integer array `arr` and two integers `k` and `threshold`, return the number of subarrays of size `k` whose average is greater than or equal to `threshold`.

### Example

### Input

```python
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
```

### Output

```python
3
```

### Explanation

Subarrays of size 3:

```python
[2,2,2] -> average = 2
[2,2,2] -> average = 2
[2,2,5] -> average = 3
[2,5,5] -> average = 4
[5,5,5] -> average = 5
[5,5,8] -> average = 6
```

Valid subarrays:

```python
[2,5,5]
[5,5,5]
[5,5,8]
```

Count:

```python
3
```

---

## LeetCode Link

https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

---

## My Initial Thought Process

My first idea was straightforward.

Generate every subarray of size `k`, calculate its average, and count how many satisfy the condition.

Example:

```python
for i in range(len(arr)-k+1):
    avg = sum(arr[i:i+k]) / k
```

This solution works correctly but repeatedly calculates the sum for overlapping windows.

For example:

```python
[2,2,2]
```

and

```python
[2,2,5]
```

share many elements, yet the sum is recomputed from scratch each time.

This caused a Time Limit Exceeded error on larger test cases.

---

## Brute Force Solution

```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0

        for i in range(len(arr)-k+1):
            avg = sum(arr[i:i+k]) / k

            if avg >= threshold:
                count += 1

        return count
```

---

## Complexity Analysis (Brute Force)

### Time Complexity

For every window:

```python
sum(arr[i:i+k])
```

takes:

```text
O(k)
```

Number of windows:

```text
O(n)
```

Total:

```text
O(n × k)
```

---

### Space Complexity

```text
O(1)
```

---

## Key Observation

The problem asks for:

```text
Subarrays of a fixed size k
```

This is a strong hint for the Sliding Window pattern.

Consider:

```python
[2,2,2]
```

Sum:

```python
6
```

Next window:

```python
[2,2,5]
```

Instead of recalculating:

```python
2 + 2 + 5
```

we can reuse the previous sum.

Remove:

```python
2
```

Add:

```python
5
```

New sum:

```python
6 - 2 + 5 = 9
```

This avoids repeated work.

---

## Another Optimization

The problem asks:

```python
average >= threshold
```

Instead of calculating:

```python
window_sum / k >= threshold
```

we can rewrite it as:

```python
window_sum >= threshold * k
```

This removes the division operation entirely.

---

## Sliding Window Idea

First window:

```python
window_sum = sum(arr[:k])
```

Then slide the window one position at a time.

Formula:

```python
window_sum = window_sum - leaving_element + entering_element
```

More specifically:

```python
window_sum = window_sum - arr[right-k] + arr[right]
```

---

## Optimized Solution

```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0

        window_sum = sum(arr[:k])

        if window_sum >= threshold * k:
            count += 1

        for right in range(k, len(arr)):

            window_sum = window_sum - arr[right-k] + arr[right]

            if window_sum >= threshold * k:
                count += 1

        return count
```

---

## Dry Run

Input:

```python
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
```

First window:

```python
[2,2,2]
```

Sum:

```python
6
```

Check:

```python
6 >= 12
```

False.

---

### Slide 1

Remove:

```python
arr[0] = 2
```

Add:

```python
arr[3] = 2
```

New sum:

```python
6 - 2 + 2 = 6
```

Still invalid.

---

### Slide 2

Remove:

```python
arr[1] = 2
```

Add:

```python
arr[4] = 5
```

New sum:

```python
6 - 2 + 5 = 9
```

Still invalid.

---

### Slide 3

Remove:

```python
arr[2] = 2
```

Add:

```python
arr[5] = 5
```

New sum:

```python
9 - 2 + 5 = 12
```

Check:

```python
12 >= 12
```

Valid.

Count = 1

---

Continue similarly and obtain:

```python
Count = 3
```

---

## Why Sliding Window Works

Adjacent windows overlap heavily.

Example:

```python
[2,2,5]
[2,5,5]
```

Most elements are shared.

Instead of recomputing everything, we update the sum using only:

```text
One element leaving
One element entering
```

This reduces the complexity significantly.

---

## Complexity Analysis

Let:

```text
n = length of array
```

### Time Complexity

First window sum:

```text
O(k)
```

Sliding through remaining elements:

```text
O(n)
```

Total:

```text
O(n)
```

---

### Space Complexity

Only a few variables are used.

```text
O(1)
```

---

## Pattern Learned

### Fixed Size Sliding Window

Whenever a problem mentions:

```text
Subarray of size k
```

ask:

```text
Can Sliding Window be used?
```

Common examples:

- Maximum Sum Subarray of Size K
- Maximum Average Subarray
- Find All Anagrams in a String
- Number of Subarrays of Size K

---

## Key Takeaways

- Fixed-size subarray problems often use Sliding Window.
- Reuse previous computations whenever possible.
- Avoid recalculating overlapping windows.
- Mathematical transformations can simplify conditions.
- Sliding Window can reduce O(n × k) solutions to O(n).

---

## Concepts Practiced

✅ Arrays

✅ Sliding Window

✅ Fixed-Size Window

✅ Running Sum

✅ Optimization

✅ Time Complexity Analysis

---

## Final Complexity

| Approach | Time | Space |
|-----------|--------|--------|
| Brute Force | O(n × k) | O(1) |
| Sliding Window | O(n) | O(1) |

---

## Status

✅ Solved

✅ Learned Fixed-Size Sliding Window

✅ Learned Window Sum Reuse

✅ Learned Sliding Formula

✅ Understood O(n × k) → O(n) Optimization
