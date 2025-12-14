# Viva Preparation Guide

## Assignment 03: Knapsack Problem in Air Flight Optimization
**Student**: Basim Gul  
**Course**: CSC-321 (Design and Analysis of Algorithms)

---

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Algorithm-Specific Questions](#algorithm-specific-questions)
3. [Comparative Questions](#comparative-questions)
4. [Implementation Questions](#implementation-questions)
5. [Problem-Solving Questions](#problem-solving-questions)
6. [Advanced Topics](#advanced-topics)

---

## Core Concepts

### Q1: What is the Knapsack Problem?

**Answer**:
The Knapsack Problem is an optimization problem where we have a set of items, each with a weight and a value, and we need to select items to maximize total value while keeping total weight within a capacity limit.

**Real-world Application** (Airline Cargo):
Airlines need to load cargo items onto flights with limited weight capacity, where each item generates revenue. The goal is to maximize revenue while respecting weight constraints.

---

### Q2: What is the difference between 0/1 and Fractional Knapsack?

**Answer**:

| Aspect | 0/1 Knapsack | Fractional Knapsack |
|--------|--------------|---------------------|
| **Item Division** | Cannot split items | Can take fractions |
| **Decision** | Binary (0 or 1) | Continuous (0 to 1) |
| **Optimal Algorithm** | Dynamic Programming | Greedy Algorithm |
| **Complexity** | O(n × W) | O(n log n) |
| **Example** | Whole packages | Liquids, powders |

**In Airline Context**:
- **0/1**: Cargo containers, packages (indivisible)
- **Fractional**: Fuel, water, bulk materials (divisible)

---

### Q3: Why is the Knapsack Problem important?

**Answer**:

**Theoretical Importance**:
- Classic NP-complete problem (0/1 version)
- Demonstrates dynamic programming principles
- Foundation for resource allocation problems

**Practical Applications**:
1. **Airline Cargo Loading**: Maximize revenue per flight
2. **Portfolio Optimization**: Select investments with budget constraint
3. **Resource Allocation**: Assign tasks to limited resources
4. **Cutting Stock**: Minimize waste in manufacturing
5. **Memory Management**: Select data to cache

---

## Algorithm-Specific Questions

### Dynamic Programming Questions

#### Q4: Explain the Dynamic Programming approach for 0/1 Knapsack.

**Answer**:

**Principle**: Break problem into overlapping subproblems and build solution bottom-up.

**Recurrence Relation**:
```
DP[i][w] = maximum value using first i items with capacity w

Base Cases:
- DP[0][w] = 0  (no items)
- DP[i][0] = 0  (no capacity)

Recursive Case:
- If weight[i] > w:
    DP[i][w] = DP[i-1][w]  (can't include item)
- Else:
    DP[i][w] = max(
        DP[i-1][w],                      // exclude item i
        DP[i-1][w-weight[i]] + value[i]  // include item i
    )
```

**Example for our problem** (Item 7: Jewelry, 5kg, $80):
```
DP[7][50] = max(
    DP[6][50],           // don't take jewelry = 360
    DP[6][45] + 80       // take jewelry = 300 + 80 = 380
) = 380
```

---

#### Q5: How do you reconstruct the solution (find which items were selected)?

**Answer**:

**Backtracking Process**:

Start from DP[n][W] and trace back:

```python
i = n, w = W
while i > 0 and w > 0:
    if DP[i][w] != DP[i-1][w]:
        # Item i was included
        selected[i] = True
        w = w - weight[i]
    i = i - 1
```

**For Our Problem**:
```
DP[7][50] = 380 ≠ DP[6][50] = 360  → Select Item 7 (Jewelry)
DP[6][45] = 300 = DP[5][45] = 300  → Skip Item 6 (Textiles)
DP[5][45] = 300 = DP[4][45] = 300  → Skip Item 5 (Perishable)
DP[4][45] = 300 ≠ DP[3][45] = 280  → Select Item 4 (Machine Parts)
DP[3][20] = 120 ≠ DP[2][20] = 100  → Select Item 3 (Documents)
...
```

**Selected**: Jewelry (5kg), Machine Parts (25kg), Documents (15kg) = 45kg, $380

---

#### Q6: What is the time and space complexity of DP solution?

**Answer**:

**Time Complexity: O(n × W)**
- Fill (n+1) × (W+1) table
- Each cell computed in O(1)
- Backtracking: O(n)
- Total: O(n × W) + O(n) = **O(n × W)**

**Space Complexity: O(n × W)**
- DP table: (n+1) × (W+1)
- Auxiliary arrays: O(n)
- Total: **O(n × W)**

**For Our Problem**:
- n = 7, W = 50
- Operations: 7 × 50 = 350
- Memory: 8 × 51 = 408 cells

**Note**: This is **pseudopolynomial** (depends on W value, not just input size).

---

#### Q7: Can we optimize the space complexity?

**Answer**:

**Yes! Use 1D Array**:

Instead of 2D table DP[n][W], use 1D array DP[W]:

```python
DP = [0] * (W + 1)

for i in range(n):
    # Traverse backwards to avoid overwriting
    for w in range(W, weight[i]-1, -1):
        DP[w] = max(DP[w], DP[w-weight[i]] + value[i])
```

**New Space Complexity**: O(W) instead of O(n × W)

**Trade-off**: Cannot reconstruct solution path easily.

---

### Greedy Algorithm Questions

#### Q8: Explain the Greedy approach for Knapsack.

**Answer**:

**Strategy**: Make locally optimal choice at each step.

**Steps**:
1. Calculate value-to-weight ratio for each item
2. Sort items by ratio (descending)
3. Greedily select items with highest ratio first

**Example**:
```
Ratios:
- Jewelry: 80/5 = 16.00  (highest)
- Documents: 120/15 = 8.00
- Machine Parts: 180/25 = 7.20
- Medical Supplies: 60/10 = 6.00
...

Selection:
1. Take Jewelry (5kg) → Remaining: 45kg
2. Take Documents (15kg) → Remaining: 30kg
3. Take Machine Parts (25kg) → Remaining: 5kg
4. Cannot fit Medical Supplies (10kg > 5kg)

Total: 45kg, $380
```

---

#### Q9: Is Greedy optimal for 0/1 Knapsack?

**Answer**:

**No, NOT guaranteed optimal** for 0/1 Knapsack!

**Counter-Example**:
```
Capacity: 10kg
- Item A: 6kg, $10 (ratio = 1.67)  ← Greedy selects
- Item B: 5kg, $8  (ratio = 1.60)
- Item C: 4kg, $6  (ratio = 1.50)

Greedy Solution:
- Take A (6kg) → Remaining: 4kg
- Cannot fit B or C together
- Total: $10

Optimal Solution:
- Take B + C (9kg)
- Total: $14  ← Better!
```

**But**: Greedy IS optimal for **Fractional Knapsack**.

---

#### Q10: Why is Greedy optimal for Fractional Knapsack?

**Answer**:

**Proof Sketch**:

For fractional knapsack, we can always improve any non-greedy solution:

1. Suppose optimal solution has item with lower ratio before higher ratio item
2. Replace fraction of lower-ratio item with higher-ratio item
3. This increases total value (contradiction)
4. Therefore, optimal solution must follow greedy order

**Mathematically**:
- If ratio[i] > ratio[j] and we select more of j than i
- Swap Δw weight from j to i
- Value change: Δw × (ratio[i] - ratio[j]) > 0 (improvement!)

---

## Comparative Questions

#### Q11: Compare DP and Greedy for the Knapsack Problem.

**Answer**:

| Criteria | Dynamic Programming | Greedy Algorithm |
|----------|---------------------|------------------|
| **Time Complexity** | O(n × W) | O(n log n) |
| **Space Complexity** | O(n × W) | O(n) |
| **Optimality (0/1)** | ✓ Guaranteed | ✗ Not guaranteed |
| **Optimality (Frac)** | N/A | ✓ Guaranteed |
| **Speed** | Slower | Faster (1.46× in our test) |
| **Scalability** | Limited by W | Excellent |
| **Implementation** | Moderate | Simple |
| **Use Case** | Optimal required | Speed required |

**Our Results**:
- Both found $380 for 0/1 (coincidental for Greedy)
- Greedy (Fractional) found $410 (optimal for fractional)

---

#### Q12: When would you choose DP over Greedy, and vice versa?

**Answer**:

**Choose Dynamic Programming when**:
1. **Optimal solution is mandatory** (legal, financial requirements)
2. **Dataset is manageable** (n × W < 1,000,000)
3. **Offline computation** (pre-flight planning)
4. **0/1 constraint is strict** (indivisible items)
5. **Can afford time and memory**

**Example**: Final cargo manifest for regulatory compliance.

**Choose Greedy when**:
1. **Speed is critical** (real-time decisions)
2. **Large datasets** (n > 10,000 or W > 100,000)
3. **Items are divisible** (fractional knapsack)
4. **Near-optimal acceptable** (quick estimates)
5. **Memory constrained** (embedded systems)

**Example**: Quick quote for customer inquiry.

**Hybrid Approach**: Use Greedy for estimate, DP for final optimization if time permits.

---

## Implementation Questions

#### Q13: Walk through your code implementation.

**Answer**:

**My implementation has three main parts**:

**1. Dynamic Programming Class**:
```python
class DynamicProgrammingKnapsack:
    def solve(self):
        self._build_dp_table()    # Fill table bottom-up
        self._backtrack()          # Find selected items
        self._display_results()    # Show output
```

**2. Greedy Class**:
```python
class GreedyKnapsack:
    def solve_01(self):
        self._display_ratios()     # Calculate ratios
        self._sort_items()         # Sort by ratio
        self._select_items_01()    # Greedy selection
```

**3. Visualization**:
```python
create_visualizations()           # 8 matplotlib charts
```

**Key Features**:
- All code in ONE file (knapsack_solver.py)
- Comprehensive output with step-by-step process
- 8 visualization charts
- Clear complexity analysis
- Professional formatting with emojis and Unicode boxes

---

#### Q14: How did you handle the visualization?

**Answer**:

**Used matplotlib with 8 different charts**:

1. **Bar Chart**: Value comparison (DP vs Greedy vs Fractional)
2. **Bar Chart**: Capacity utilization comparison
3. **Bar Chart**: Execution time comparison
4. **Horizontal Bar**: Item selection (DP vs Greedy)
5. **Horizontal Bar**: Value-to-weight ratios
6. **Scatter Plot**: Weight vs Value distribution
7. **Pie Chart**: Capacity utilization (DP)
8. **Bar Chart**: Complexity comparison (operations count)

**Layout**: 3×3 GridSpec for professional appearance

**Features**:
- Color coding (green=selected, red=rejected)
- Annotations with values
- Grid lines for readability
- Legends and titles
- Saved as PNG (365KB)

---

## Problem-Solving Questions

#### Q15: If the greedy solution differs from DP, how do you explain it?

**Answer**:

**Explanation**:

Greedy makes **locally optimal** choices, which don't always lead to **globally optimal** solution for 0/1 knapsack.

**Why?**:
- Greedy commits to high-ratio items early
- Cannot reconsider if combination of lower-ratio items is better
- DP explores all possibilities systematically

**Example Scenario**:
```
Capacity: 50kg
- High-ratio item: 45kg, $200 (ratio=4.44)
- Two medium items: 25kg×2, $250 total (ratio=5.0 each)

Greedy: Takes high-ratio item (can't fit both medium) → $200
DP: Takes both medium items → $250 ← Better!
```

**In our case**: Both got $380 because item weights aligned favorably.

---

#### Q16: How would you modify the algorithm for additional constraints?

**Answer**:

**Common Additional Constraints**:

**1. Volume Constraint** (2D Knapsack):
```python
DP[i][w][v] = max value using i items, weight w, volume v
```
- Time: O(n × W × V)
- More memory intensive

**2. Multiple Knapsacks**:
- Assign items to different flights
- NP-hard, use branch-and-bound or approximation

**3. Item Dependencies**:
- Item A requires Item B
- Use graph to track dependencies

**4. Priority Tiers**:
```python
# Load high-priority items first
for priority in [HIGH, MEDIUM, LOW]:
    solve_knapsack(items[priority])
```

**5. Balance Constraint**:
- Weight distribution for flight stability
- Divide capacity into zones

**For Airline**:
```python
if is_medical_supply(item):
    priority_boost = 1.5
    effective_ratio = base_ratio * priority_boost
```

---

#### Q17: How would you test your implementation?

**Answer**:

**Test Strategy**:

**1. Base Cases**:
```python
# Test 1: Empty knapsack
items = [], capacity = 0 → Expected: 0

# Test 2: Single item fits
items = [(10, 60)], capacity = 50 → Expected: 60

# Test 3: Single item doesn't fit  
items = [(60, 100)], capacity = 50 → Expected: 0
```

**2. Known Cases**:
```python
# Test 4: All items fit
total_weight = 40, capacity = 50 → Expected: sum of all values

# Test 5: No items fit
all weights > capacity → Expected: 0
```

**3. Edge Cases**:
```python
# Test 6: Same ratios
All items have ratio = 2.0 → Check ordering

# Test 7: Zero values
Some items with value = 0 → Should skip

# Test 8: Very large W
W = 1000000 → Check memory/time
```

**4. Validation**:
```python
# Verify constraints
assert total_weight <= capacity
assert all_items_selected_are_valid
assert value == sum(selected_values)
```

**5. Compare Algorithms**:
```python
dp_result = solve_dp()
greedy_result = solve_greedy()
assert greedy_result <= dp_result  # DP should be ≥ Greedy
```

---

## Advanced Topics

#### Q18: What is the NP-completeness of the Knapsack Problem?

**Answer**:

**0/1 Knapsack is NP-Complete**:

**Decision Version**: "Is there a subset with total value ≥ V and weight ≤ W?"

**Proof**:
1. **In NP**: Given a solution, verify in polynomial time O(n)
2. **NP-Hard**: Reduce from Subset Sum problem

**Implications**:
- No known polynomial-time algorithm
- DP is pseudopolynomial (depends on W, not just n)
- Approximation algorithms exist (FPTAS)

**Fractional Knapsack**: NOT NP-complete (solvable in O(n log n))

---

#### Q19: What are approximation algorithms for Knapsack?

**Answer**:

**1. Greedy Approximation** (0/1):
- Ratio: Can be arbitrarily bad
- Fast: O(n log n)

**2. Greedy with Best Single Item**:
```python
result = max(greedy_solution, best_single_item)
```
- Approximation Ratio: 2 (within 2× of optimal)

**3. FPTAS** (Fully Polynomial-Time Approximation Scheme):
- For any ε > 0, find solution within (1+ε) of optimal
- Time: O(n³/ε)
- Good for high-precision requirements

**4. Branch and Bound**:
- Exact algorithm with pruning
- Better average-case than DP for sparse problems

---

#### Q20: How does this apply to real airline operations?

**Answer**:

**Real-World Airline Cargo Optimization**:

**1. Multi-Dimensional Constraints**:
- Weight (primary)
- Volume (secondary)
- Balance (center of gravity)
- Dangerous goods regulations

**2. Dynamic Environment**:
- Last-minute bookings
- Cancellations
- Weather changes affecting fuel weight

**3. Priority System**:
```
Priority 1: Medical supplies, organs
Priority 2: Perishable goods
Priority 3: Standard cargo
Priority 4: Low-priority freight
```

**4. Revenue Management**:
- Different rates for different cargo types
- Long-term contracts vs spot pricing
- Overbooking strategies

**5. Network Optimization**:
- Not just one flight, but entire network
- Transfer cargo between flights
- Multi-leg journeys

**6. Real Implementation**:
```python
def airline_cargo_optimization():
    # Phase 1: Priority items (DP for optimal)
    load_priority_cargo()
    
    # Phase 2: Regular cargo (Greedy for speed)
    load_regular_cargo()
    
    # Phase 3: Last-minute (Real-time greedy)
    handle_last_minute_changes()
    
    # Constraint check
    verify_balance_and_safety()
```

**Tools Used**:
- IBM ILOG CPLEX
- Gurobi Optimizer
- Custom heuristics

---

## Key Takeaways for Viva

### Must Know

1. ✓ **Recurrence relation** for DP
2. ✓ **Time/Space complexity** of both algorithms
3. ✓ **Why Greedy is not optimal** for 0/1
4. ✓ **Backtracking process** in DP
5. ✓ **Results from your implementation** ($380 vs $410)

### Be Prepared to

1. ✓ **Walk through code** line by line
2. ✓ **Trace algorithm** on small example
3. ✓ **Explain visualizations** 
4. ✓ **Discuss trade-offs**
5. ✓ **Suggest improvements**

### Common Mistakes to Avoid

1. ✗ Confusing 0/1 with Fractional
2. ✗ Saying Greedy is always optimal
3. ✗ Forgetting pseudopolynomial nature of DP
4. ✗ Not considering space optimization
5. ✗ Ignoring practical constraints

---

## Practice Problems

### Problem 1
**Given**: 4 items, capacity 8kg
- A: 4kg, $12
- B: 3kg, $8
- C: 5kg, $15
- D: 2kg, $5

**Question**: Solve using both DP and Greedy. Do they match?

**Answer**:
- **Ratios**: A=3.0, C=3.0, B=2.67, D=2.5
- **Greedy**: A+D = 6kg, $17
- **DP**: B+C = 8kg, $23 ← Optimal
- **Match?**: NO (Greedy suboptimal)

---

### Problem 2
**Question**: What if we can use each item multiple times (Unbounded Knapsack)?

**Answer**: Modify DP:
```python
for i in range(n):
    for w in range(weight[i], W+1):
        DP[w] = max(DP[w], DP[w-weight[i]] + value[i])
```
Time: Still O(n × W), but different recurrence.

---

**Good luck with your viva!** 🎓

Remember: **Understanding > Memorization**

---

**Document Version**: 1.0  
**Last Updated**: December 14, 2025  
**Author**: Basim Gul
