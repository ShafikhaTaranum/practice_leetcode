# 126. Word Ladder II

**LeetCode Link:** https://leetcode.com/problems/word-ladder-ii/

## Difficulty: Hard
**Category:** Graph | BFS | Backtracking

---

## Problem Statement
A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words:
- `begin_word -> s1 -> s2 -> ... -> sk` where each `si` for `1 <= i <= k` is in `wordList`
- Each `si[j]` (character at position j) differs from `si-1[j]` by exactly one letter
- `sk == endWord`

Return *all the shortest transformation sequences* from `beginWord` to `endWord`, or an empty list if no such sequence exists. You can return the sequences in **any order**.

---

## Approach

### Algorithm: BFS + DFS/Backtracking
- **Time Complexity:** O(N × L × 26) for BFS, O(2^N × L) for backtracking
- **Space Complexity:** O(N)

Where N is number of words and L is word length

### Key Insight:
- Use BFS to find the shortest distance from each word to the end word
- Build a parent graph during BFS to track which words can lead to shorter paths
- Use DFS/backtracking to reconstruct all shortest paths from the result

---

## Solution

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        parents={}
        level=set([beginWord])
        found=False
        while level and not found:
            next_level=set()
            for word in level:
                if word in wordset:
                    wordset.remove(word)
            for word in level:
                for i in range(len(word)):
                    for ch in 'qwertyuiopasdfghjklzxcvbnm':
                        new_word=word[:i]+ch+word[i+1:]
                        if new_word in wordset:
                            if new_word not in parents:
                                parents[new_word]=[]
                            parents[new_word].append(word)
                            next_level.add(new_word)
                            if new_word==endWord:
                                found=True
            level=next_level
        res=[]
        def dfs(word,path):
            if word==beginWord:
                res.append(path[::-1])
                return
            if word not in parents:
                return
            for p in parents[word]:
                dfs(p,path+[p])
        if found:
            dfs(endWord,[endWord])
        return res
```

---

## Examples

### Example 1:
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
```

### Example 2:
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: endWord "cog" is not in wordList
```
