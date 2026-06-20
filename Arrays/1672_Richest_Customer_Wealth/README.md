# 1672. Richest Customer Wealth

## Problem Statement

You are given an m x n integer grid `accounts` where `accounts[i][j]` is the amount of money the i-th customer has in the j-th bank.

Return the wealth that the richest customer has.

A customer's wealth is the sum of all money they have across all bank accounts.

The richest customer is the customer with the maximum wealth.

---

## Example 1

Input:

```python
accounts = [[1,2,3],[3,2,1]]
```

Output:

```python
6
```

Explanation:

- Customer 1 wealth = 1 + 2 + 3 = 6
- Customer 2 wealth = 3 + 2 + 1 = 6

Both customers have the same wealth, so the answer is 6.

---

## Example 2

Input:

```python
accounts = [[1,5],[7,3],[3,5]]
```

Output:

```python
10
```

---

## Constraints

```text
m == accounts.length
n == accounts[i].length

1 <= m, n <= 50
1 <= accounts[i][j] <= 100
```

---

## Solution

[View Solution](solution.py)

---

## My Thought Process

Each row in the matrix represents a customer.

To find a customer's wealth, I need to add all values in that row.

Once I know the wealth of every customer, I simply return the maximum wealth among them.

Python's built-in functions make this concise:

- `sum(account)` calculates the wealth of one customer.
- `max()` finds the largest wealth among all customers.

This allows me to solve the problem in a single line.

---

## Complexity Analysis

### Time Complexity

```text
O(m × n)
```

Every element in the matrix is visited once while calculating customer wealth.

### Space Complexity

```text
O(1)
```

No extra data structures are used.

---

## Concepts Learned

- Arrays
- 2D Arrays
- Iteration
- sum()
- max()
- Generator Expressions
