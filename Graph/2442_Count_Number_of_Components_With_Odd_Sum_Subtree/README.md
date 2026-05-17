# 2751. Robot Collisions

**LeetCode Link:** https://leetcode.com/problems/robot-collisions/

## Difficulty: Hard
**Category:** Graph | Stack

---

## Problem Statement
There are `n` robots on an infinite line, numbered from `0` to `n - 1`. Initially, robot `i` is at position `positions[i]` and moving in the direction `directions[i]` ('L' for left, 'R' for right) with `healths[i]` health.

When two robots collide:
- The robot with lower health disappears
- The robot with higher health survives with health reduced by 1
- If both have the same health, both disappear

Determine the survivors after all collisions.

---

## Approach

### Algorithm: Stack-based Collision Handling
- **Time Complexity:** O(n log n) due to sorting
- **Space Complexity:** O(n)

### Key Insight:
- Sort robots by position to process left-to-right
- Use a stack to handle collisions between robots moving right (R) and left (L)
- Process collisions when we encounter an 'L' moving robot
- Only robots moving 'R' remain in the stack as potential colliders

---

## Solution

```python
class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])
        dead = [False] * n
        st = []

        for i in order:
            if directions[i] == 'R':
                st.append(i)
            else:
                while st and directions[st[-1]] == 'R':
                    top = st[-1]
                    if healths[top] > healths[i]:
                        healths[top] -= 1
                        dead[i] = True
                        break
                    elif healths[top] < healths[i]:
                        healths[i] -= 1
                        dead[top] = True
                        st.pop()
                    else:
                        dead[i] = dead[top] = True
                        st.pop()
                        break
                if not dead[i]:
                    st.append(i)

        return [healths[i] for i in range(n) if not dead[i]]
```

---

## Examples

### Example 1:
```
Input: positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRLR"
Output: [2,17,9,15,10]
Explanation: No robots collide
```

### Example 2:
```
Input: positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
Output: [14]
Explanation: Collisions eliminate most robots
```
