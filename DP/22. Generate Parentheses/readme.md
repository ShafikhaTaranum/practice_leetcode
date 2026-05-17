# 22. Generate Parentheses

## Difficulty
Medium

## Problem Link
https://leetcode.com/problems/generate-parentheses/

---

## Problem Statement
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

---

## Constraints
- `1 <= n <= 8`

---

## Examples

### Example 1
```text
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

### Example 2
```text
Input: n = 1
Output: ["()"]
```

---

## Concepts Used
- Backtracking
- Recursion
- Dynamic Programming

---

## Approach
Use backtracking to generate all valid combinations of parentheses.

### Rules
- Add `'('` if the number of opening brackets is less than `n`.
- Add `')'` only if the number of closing brackets is less than opening brackets.

Continue recursively until the string length becomes `2 * n`.

---

## Complexity
- Time Complexity: O(4ⁿ / √n)
- Space Complexity: O(n)

---

Created using LeetHub 🚀
