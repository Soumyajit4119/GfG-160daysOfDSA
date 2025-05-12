# [Move All Zeros to End](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green.svg)

## 📝 Problem Statement

You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

## 📊 Examples

### ✅ Example 1

```
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
```

### ✅ Example 2

```
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.
```

### ✅ Example 3

```
Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.
```

## 📌 Constraints

- 1 ≤ arr.size() ≤ 105  
- 0 ≤ arr[i] ≤ 105  