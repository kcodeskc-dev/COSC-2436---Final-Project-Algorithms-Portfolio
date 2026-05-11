# Chapter 3: Recursion — Lab Report

## Student Information
- **Name:** Karla Cuevas
- **Date:** 05/10/2026
- **Course:** COSC 2436

## Algorithm Summary
##1. What happens if you forget the base case?

    [the function will continue to call itself indefinitely.]
##2. Why is the naive Fibonacci implementation inefficient?
    [it recalculates values multiple times, memoization or an iterative approach can improve the efficiency to linear time, (O(n)).]

##3. Draw the call stack for fact(4).
[    fact(4)
    → 4 * fact(3)
        → 3 * fact(2)
        → 2 * fact(1)
            → fact(1) returns 1    ← Base case!
        → returns 2 * 1 = 2
        → returns 3 * 2 = 6
    → returns 4 * 6 = 24
]
