# 5. Longest Palindromic Substring

## Difficulty
Medium

## Problem Link
https://leetcode.com/problems/longest-palindromic-substring/

## Concepts Used
- Dynamic Programming
- Strings

## Problem Statement
Given a string `s`, return the longest palindromic substring in `s`.

## Approach
Use Dynamic Programming to determine whether a substring is palindrome or not.

- Single characters are always palindromes.
- Two equal consecutive characters form a palindrome.
- For length greater than 2:
  - If first and last characters are equal
  - And the remaining substring is palindrome
  - Then the current substring is also palindrome.

Track the longest palindrome during traversal.

## Complexity
- Time Complexity: O(n²)
- Space Complexity: O(n²)

## Solution
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        max_len = 1
        
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
        
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    
                    if length > max_len:
                        start = i
                        max_len = length
        
        return s[start:start + max_len]
```

---
Created using LeetHub 🚀
