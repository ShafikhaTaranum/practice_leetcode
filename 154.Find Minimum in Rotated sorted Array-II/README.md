# LeetCode Problem 154 - Find Minimum in Rotated Sorted Array II

## Problem Description
Suppose an array sorted in ascending order is rotated at some unknown pivot index k (where 0 <= k < nums.length) and then possibly rotated multiple times.

For example:
- [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
- [2,1] might become [1,2]

Given an array nums that may contain duplicates, return the minimum element of the array.

You must decrease the overall operation complexity as much as possible.

## Constraints
- 1 <= nums.length <= 5000
- -5000 <= nums[i] <= 5000
- All integers in the array are unique

## Related Topics
- Binary Search
- Array

## Difficulty
Hard

## Solution Approach
The challenge here is that the array may contain duplicates, which makes binary search more tricky compared to the variant without duplicates. We need to handle cases where nums[mid] == nums[left][...]
