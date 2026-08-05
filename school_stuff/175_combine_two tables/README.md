# LeetCode 175: Combine Two Tables

## Problem Link
[LeetCode - Combine Two Tables](https://leetcode.com)

## Difficulty
**Easy**

## Topic
**Database (SQL)**

## Problem Description
Table: `Person`

| Column Name | Type    |
|-------------|---------|
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
`personId` is the primary key column for this table. This table contains information about the ID of some persons and their first and last names.

Table: `Address`

| Column Name | Type    |
|-------------|---------|
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
`addressId` is the primary key column for this table. Each row of this table contains information about the city and state of one person with ID = personId.

Write an SQL query to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not present in the `Address` table, report `null` instead.

Return the result table in **any order**.

## Solution
A `LEFT JOIN` is used here to ensure that all individuals from the `Person` table are included in the result, even if they do not have a corresponding record in the `Address` table.

```sql
# Write your MySQL query statement below
SELECT p.firstName , p.lastName , a.city , a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;
```

## Complexity Analysis
- **Time Complexity:** $O(N + M)$ where $N$ is the number of rows in the `Person` table and $M$ is the number of rows in the `Address` table.
- **Space Complexity:** $O(1)$ as no extra intermediate data structures are created; the output space depends on the size of the tables.
