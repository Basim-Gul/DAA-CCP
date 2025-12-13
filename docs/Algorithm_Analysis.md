# Algorithm Analysis Document

## Assignment 03: Knapsack Problem in Air Flight Optimization
**Student**: Basim Gul  
**Course**: CSC-321 (Design and Analysis of Algorithms)  
**Instructor**: Dr. Muhammad Tariq Siddique

---

## Table of Contents
1. [Algorithm Overview](#algorithm-overview)
2. [Dynamic Programming Analysis](#dynamic-programming-analysis)
3. [Greedy Algorithm Analysis](#greedy-algorithm-analysis)
4. [Comparative Analysis](#comparative-analysis)
5. [Performance Evaluation](#performance-evaluation)
6. [Scalability Analysis](#scalability-analysis)

---

## Algorithm Overview

### Problem Statement
Given a set of items, each with a weight and a value, determine which items to include in a collection (knapsack) so that the total weight is less than or equal to a given limit and the total value is as large as possible.

### Variants Implemented
1. **0/1 Knapsack (Dynamic Programming)**: Items cannot be divided
2. **0/1 Knapsack (Greedy)**: Greedy heuristic for 0/1 constraint
3. **Fractional Knapsack (Greedy)**: Items can be divided

---

## Dynamic Programming Analysis

### Algorithm Description

The Dynamic Programming (DP) approach solves the 0/1 knapsack problem optimally by building a table that stores solutions to subproblems.

### Recurrence Relation

```
DP[i][w] = {
    0                                           if i = 0 or w = 0
    DP[i-1][w]                                 if weight[i] > w
    max(DP[i-1][w], DP[i-1][w-weight[i]] + value[i])  otherwise
}
```

Where:
- `DP[i][w]` = maximum value achievable using first i items with capacity w
- `i` = item index (0 to n)
- `w` = capacity (0 to W)

### Time Complexity Analysis

**Worst Case: O(n × W)**

1. **Table Filling**: 
   - Two nested loops: outer loop runs n times, inner loop runs W times
   - Each cell computation is O(1)
   - Total: n × W operations

2. **Backtracking**:
   - Single loop through at most n items
   - Each step is O(1)
   - Total: O(n)

3. **Overall**: O(n × W) + O(n) = **O(n × W)**

**For our problem**:
- n = 7 items
- W = 50 kg
- Operations = 7 × 50 = **350 operations**

### Space Complexity Analysis

**Space: O(n × W)**

1. **DP Table**: (n+1) × (W+1) array = O(n × W)
2. **Selected Items Array**: O(n)
3. **Input Arrays**: O(n)
4. **Total**: **O(n × W)**

**For our problem**: 8 × 51 = **408 memory cells**

### Characteristics

**Advantages**:
- ✓ Guarantees optimal solution
- ✓ Systematic approach
- ✓ Can reconstruct solution path
- ✓ Solves all subproblems (useful if multiple queries)

**Disadvantages**:
- ✗ High space complexity for large W
- ✗ Slower than greedy for large datasets
- ✗ Not suitable for real-time applications
- ✗ Pseudopolynomial time (dependent on W value)

### Optimization Techniques

1. **Space Optimization**: Use 1D array instead of 2D (O(W) space)
2. **Early Termination**: Stop if all items fit
3. **Memoization**: Top-down approach to avoid computing unused states

---

## Greedy Algorithm Analysis

### Algorithm Description

The Greedy approach makes locally optimal choices by selecting items with the highest value-to-weight ratio first.

### Steps

1. **Calculate Ratios**: For each item i, compute ratio[i] = value[i] / weight[i]
2. **Sort**: Sort items by ratio in descending order
3. **Select**: Greedily select items until capacity is exhausted

### Time Complexity Analysis

**Worst Case: O(n log n)**

1. **Ratio Calculation**:
   - Single loop through n items
   - Each calculation is O(1)
   - Total: O(n)

2. **Sorting**:
   - Using efficient sorting (merge sort, quick sort)
   - Total: O(n log n)

3. **Selection**:
   - Single loop through sorted items
   - Each iteration is O(1)
   - Total: O(n)

4. **Overall**: O(n) + O(n log n) + O(n) = **O(n log n)**

**For our problem**:
- n = 7 items
- Operations ≈ 7 log₂ 7 ≈ 7 × 2.807 ≈ **19.6 operations**

### Space Complexity Analysis

**Space: O(n)**

1. **Item Objects Array**: O(n)
2. **Selection Arrays**: O(n)
3. **Sorting Space**: O(log n) for recursive stack
4. **Total**: **O(n)**

**For our problem**: **7 items** (much less than DP)

### Characteristics

**Advantages**:
- ✓ Very fast: O(n log n)
- ✓ Low space complexity: O(n)
- ✓ Simple to implement
- ✓ Optimal for fractional knapsack
- ✓ Suitable for real-time applications
- ✓ Scales well to large datasets

**Disadvantages**:
- ✗ NOT optimal for 0/1 knapsack (except in special cases)
- ✗ No guarantee of finding best solution
- ✗ Cannot recover if wrong choice is made

### Optimality Conditions

**Greedy is Optimal When**:
1. Fractional knapsack (items can be divided)
2. 0/1 knapsack with specific item patterns (coincidentally)

**Greedy May Fail When**:
- Items with low ratio but perfect fit are available
- Combinations of items yield better value than high-ratio items

---

## Comparative Analysis

### Test Case Results

**Problem Instance**:
- Capacity: 50 kg
- Items: 7 cargo items
- Total available weight: 95 kg
- Total available value: $655

| Algorithm | Value | Weight | Utilization | Time (ms) | Space |
|-----------|-------|--------|-------------|-----------|-------|
| DP (0/1) | $380 | 45 kg | 90.0% | 0.55 | O(350) |
| Greedy (0/1) | $380 | 45 kg | 90.0% | 0.38 | O(7) |
| Greedy (Frac) | $410 | 50 kg | 100.0% | 0.38 | O(7) |

### Key Observations

1. **Optimality**:
   - DP found the optimal solution ($380)
   - Greedy (0/1) coincidentally found the same optimal solution
   - Greedy (Fractional) found the theoretical upper bound ($410)

2. **Speed**:
   - Greedy is ~1.46x faster than DP
   - Difference is small for n=7, but grows significantly for larger n

3. **Space Efficiency**:
   - Greedy uses 50x less space (7 vs 350 cells)

4. **Value Efficiency**:
   - DP achieves 92.68% of fractional optimum
   - This is excellent for a 0/1 constraint

### When Each Algorithm Excels

| Criteria | DP | Greedy |
|----------|-----|--------|
| Small n, small W | ✓ | ✓ |
| Small n, large W | ✗ | ✓ |
| Large n, small W | ~ | ✓ |
| Large n, large W | ✗ | ✓ |
| Optimal required | ✓ | ✗ |
| Real-time needed | ✗ | ✓ |
| Fractional items | N/A | ✓ |

---

## Performance Evaluation

### Experimental Setup

**Hardware**: Standard computing environment
**Language**: Python 3.x
**Test Data**: 7 airline cargo items, 50 kg capacity

### Execution Time Measurements

```
Dynamic Programming:  0.5512 ms
Greedy (0/1):        0.3769 ms
Greedy (Fractional): 0.3839 ms
```

**Speedup**: Greedy is 1.46× faster than DP

### Memory Usage

```
DP Table Size:     8 × 51 = 408 cells (integer array)
Greedy Array:      7 items (object array)
Memory Ratio:      DP uses ~50× more memory
```

### Accuracy

```
DP (0/1):          100% optimal (guaranteed)
Greedy (0/1):      100% optimal (coincidental for this dataset)
Greedy (Fractional): 100% optimal (guaranteed)
```

### Scalability Test (Theoretical)

| n | W | DP Ops | Greedy Ops | Ratio |
|---|---|--------|------------|-------|
| 7 | 50 | 350 | 19.6 | 17.9× |
| 100 | 1000 | 100,000 | 664 | 150× |
| 1000 | 10000 | 10,000,000 | 9,966 | 1003× |
| 10000 | 100000 | 1,000,000,000 | 132,877 | 7,525× |

**Conclusion**: Greedy advantage increases dramatically with scale.

---

## Scalability Analysis

### Small Scale (n ≤ 100, W ≤ 1000)

**Both algorithms acceptable**
- DP: ~0.1-1 ms
- Greedy: ~0.01-0.1 ms
- Recommendation: Use DP for guaranteed optimality

### Medium Scale (n ≤ 1000, W ≤ 10000)

**DP becomes slower**
- DP: ~10-100 ms
- Greedy: ~0.1-1 ms
- Recommendation: Use DP if time permits, otherwise Greedy

### Large Scale (n > 1000 or W > 10000)

**DP impractical**
- DP: seconds to minutes
- Greedy: milliseconds
- Recommendation: Use Greedy or hybrid approach

### Memory Constraints

For embedded systems or memory-limited environments:
- **DP**: May not fit in memory for large W
- **Greedy**: Always feasible
- **Recommendation**: Use space-optimized DP (1D array) or Greedy

### Real-Time Requirements

For time-critical applications:
- **DP**: Not suitable (unpredictable time)
- **Greedy**: Excellent (O(n log n) worst-case)
- **Recommendation**: Always use Greedy

---

## Practical Recommendations

### For Airline Cargo Loading

1. **Pre-flight Planning** (hours before):
   - Use DP for optimal solution
   - Time available: minutes
   - Optimal revenue is critical

2. **Last-minute Changes** (minutes before):
   - Use Greedy for quick recalculation
   - Time available: seconds
   - Near-optimal is acceptable

3. **Real-time Booking** (continuous):
   - Use Greedy for instant quotes
   - Time available: milliseconds
   - Fast response is critical

### Hybrid Approach

```
IF time_available > threshold AND dataset_size < limit THEN
    Use Dynamic Programming
ELSE
    Use Greedy Algorithm
END IF
```

**Suggested Thresholds**:
- Time: 100 ms
- Dataset: n × W < 1,000,000

### Error Bounds

For greedy 0/1 knapsack:
- **Worst case**: Can be arbitrarily bad
- **Average case**: Typically within 10-20% of optimal
- **Best case**: Optimal (as in our example)

**Recommendation**: Run both if possible, compare results.

---

## Conclusion

### Key Findings

1. **Dynamic Programming**:
   - Best for guaranteed optimal solutions
   - Acceptable for small-medium problems
   - Memory-intensive for large W

2. **Greedy Algorithm**:
   - Best for speed and scalability
   - Optimal for fractional knapsack
   - Heuristic for 0/1 knapsack (no guarantee)

3. **For Our Test Case**:
   - Both found same optimal solution
   - Greedy was 1.46× faster
   - Greedy used 50× less memory

### Final Recommendation

**Use Dynamic Programming when**:
- Optimal solution is mandatory
- Dataset is manageable (n × W < 1M)
- Offline computation is acceptable

**Use Greedy Algorithm when**:
- Speed is critical
- Dataset is large
- Near-optimal solution is acceptable
- Items can be fractional

**Use Both (Hybrid) when**:
- Resources permit
- Validation is needed
- Learning optimal vs heuristic trade-offs

---

## References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

2. Kleinberg, J., & Tardos, É. (2006). *Algorithm Design*. Pearson Education.

3. Vazirani, V. V. (2001). *Approximation Algorithms*. Springer.

4. Martello, S., & Toth, P. (1990). *Knapsack Problems: Algorithms and Computer Implementations*. Wiley.

---

**Document Version**: 1.0  
**Last Updated**: December 14, 2025  
**Author**: Basim Gul
