# Mathematical Solutions - Step-by-Step Calculations

## Assignment 03: Knapsack Problem in Air Flight Optimization
**Student**: Basim Gul  
**Course**: CSC-321 (Design and Analysis of Algorithms)

---

## Problem Data

**Maximum Capacity (W)**: 50 kg

| Item # | Item Name | Weight (kg) | Value ($) | Value/Weight Ratio |
|--------|-----------|-------------|-----------|-------------------|
| 1 | Medical Supplies | 10 | 60 | 6.00 |
| 2 | Electronics | 20 | 100 | 5.00 |
| 3 | Documents | 15 | 120 | 8.00 |
| 4 | Machine Parts | 25 | 180 | 7.20 |
| 5 | Perishable Goods | 8 | 45 | 5.63 |
| 6 | Textiles | 12 | 70 | 5.83 |
| 7 | Jewelry | 5 | 80 | 16.00 |

---

## Section 1: Dynamic Programming Solution (0/1 Knapsack)

### Mathematical Formulation

The 0/1 Knapsack problem can be formulated as:

**Maximize**: Σ(vᵢ × xᵢ) for i = 1 to n

**Subject to**: Σ(wᵢ × xᵢ) ≤ W

**Where**: xᵢ ∈ {0, 1}

### Recurrence Relation

```
DP[i][w] = {
    0                                           if i = 0 or w = 0
    DP[i-1][w]                                 if wᵢ > w
    max(DP[i-1][w], DP[i-1][w-wᵢ] + vᵢ)      otherwise
}
```

### Step-by-Step DP Table Construction

We build a table DP[8][51] where:
- Rows represent items (0 to 7, where 0 means no items)
- Columns represent capacity (0 to 50 kg)

#### Initialization

- DP[0][w] = 0 for all w (no items selected)
- DP[i][0] = 0 for all i (no capacity available)

#### Table Filling Process

**For brevity, we show key capacity points and all items:**

#### Showing Critical Columns (w = 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)

**Row 0 (No items):**
All values = 0

**Row 1 (Item 1: Medical Supplies, w₁=10, v₁=60):**

- w=5: w₁(10) > 5 → DP[1][5] = DP[0][5] = 0
- w=10: DP[1][10] = max(DP[0][10], DP[0][10-10] + 60) = max(0, 0+60) = **60**
- w=15: DP[1][15] = max(DP[0][15], DP[0][5] + 60) = max(0, 0+60) = **60**
- w=20: DP[1][20] = max(DP[0][20], DP[0][10] + 60) = max(0, 0+60) = **60**
- w=25: DP[1][25] = max(DP[0][25], DP[0][15] + 60) = max(0, 0+60) = **60**
- w=30: DP[1][30] = max(DP[0][30], DP[0][20] + 60) = max(0, 0+60) = **60**
- w=35: DP[1][35] = max(DP[0][35], DP[0][25] + 60) = max(0, 0+60) = **60**
- w=40: DP[1][40] = max(DP[0][40], DP[0][30] + 60) = max(0, 0+60) = **60**
- w=45: DP[1][45] = max(DP[0][45], DP[0][35] + 60) = max(0, 0+60) = **60**
- w=50: DP[1][50] = max(DP[0][50], DP[0][40] + 60) = max(0, 0+60) = **60**

**Row 2 (Item 2: Electronics, w₂=20, v₂=100):**

- w=5: w₂(20) > 5 → DP[2][5] = DP[1][5] = 0
- w=10: w₂(20) > 10 → DP[2][10] = DP[1][10] = 60
- w=15: w₂(20) > 15 → DP[2][15] = DP[1][15] = 60
- w=20: DP[2][20] = max(DP[1][20], DP[1][0] + 100) = max(60, 0+100) = **100**
- w=25: DP[2][25] = max(DP[1][25], DP[1][5] + 100) = max(60, 0+100) = **100**
- w=30: DP[2][30] = max(DP[1][30], DP[1][10] + 100) = max(60, 60+100) = **160**
- w=35: DP[2][35] = max(DP[1][35], DP[1][15] + 100) = max(60, 60+100) = **160**
- w=40: DP[2][40] = max(DP[1][40], DP[1][20] + 100) = max(60, 60+100) = **160**
- w=45: DP[2][45] = max(DP[1][45], DP[1][25] + 100) = max(60, 60+100) = **160**
- w=50: DP[2][50] = max(DP[1][50], DP[1][30] + 100) = max(60, 60+100) = **160**

**Row 3 (Item 3: Documents, w₃=15, v₃=120):**

- w=5: w₃(15) > 5 → DP[3][5] = DP[2][5] = 0
- w=10: w₃(15) > 10 → DP[3][10] = DP[2][10] = 60
- w=15: DP[3][15] = max(DP[2][15], DP[2][0] + 120) = max(60, 0+120) = **120**
- w=20: DP[3][20] = max(DP[2][20], DP[2][5] + 120) = max(100, 0+120) = **120**
- w=25: DP[3][25] = max(DP[2][25], DP[2][10] + 120) = max(100, 60+120) = **180**
- w=30: DP[3][30] = max(DP[2][30], DP[2][15] + 120) = max(160, 60+120) = **180**
- w=35: DP[3][35] = max(DP[2][35], DP[2][20] + 120) = max(160, 100+120) = **220**
- w=40: DP[3][40] = max(DP[2][40], DP[2][25] + 120) = max(160, 100+120) = **220**
- w=45: DP[3][45] = max(DP[2][45], DP[2][30] + 120) = max(160, 160+120) = **280**
- w=50: DP[3][50] = max(DP[2][50], DP[2][35] + 120) = max(160, 160+120) = **280**

**Row 4 (Item 4: Machine Parts, w₄=25, v₄=180):**

- w=5: w₄(25) > 5 → DP[4][5] = DP[3][5] = 0
- w=10: w₄(25) > 10 → DP[4][10] = DP[3][10] = 60
- w=15: w₄(25) > 15 → DP[4][15] = DP[3][15] = 120
- w=20: w₄(25) > 20 → DP[4][20] = DP[3][20] = 120
- w=25: DP[4][25] = max(DP[3][25], DP[3][0] + 180) = max(180, 0+180) = **180**
- w=30: DP[4][30] = max(DP[3][30], DP[3][5] + 180) = max(180, 0+180) = **180**
- w=35: DP[4][35] = max(DP[3][35], DP[3][10] + 180) = max(220, 60+180) = **240**
- w=40: DP[4][40] = max(DP[3][40], DP[3][15] + 180) = max(220, 120+180) = **300**
- w=45: DP[4][45] = max(DP[3][45], DP[3][20] + 180) = max(280, 120+180) = **300**
- w=50: DP[4][50] = max(DP[3][50], DP[3][25] + 180) = max(280, 180+180) = **360**

**Row 5 (Item 5: Perishable Goods, w₅=8, v₅=45):**

- w=5: w₅(8) > 5 → DP[5][5] = DP[4][5] = 0
- w=10: DP[5][10] = max(DP[4][10], DP[4][2] + 45) = max(60, 0+45) = **60**
- w=15: DP[5][15] = max(DP[4][15], DP[4][7] + 45) = max(120, 0+45) = **120**
- w=20: DP[5][20] = max(DP[4][20], DP[4][12] + 45) = max(120, 60+45) = **120**
- w=25: DP[5][25] = max(DP[4][25], DP[4][17] + 45) = max(180, 120+45) = **180**
- w=30: DP[5][30] = max(DP[4][30], DP[4][22] + 45) = max(180, 120+45) = **180**
- w=35: DP[5][35] = max(DP[4][35], DP[4][27] + 45) = max(240, 180+45) = **240**
- w=40: DP[5][40] = max(DP[4][40], DP[4][32] + 45) = max(300, 180+45) = **300**
- w=45: DP[5][45] = max(DP[4][45], DP[4][37] + 45) = max(300, 240+45) = **300**
- w=50: DP[5][50] = max(DP[4][50], DP[4][42] + 45) = max(360, 300+45) = **360**

**Row 6 (Item 6: Textiles, w₆=12, v₆=70):**

- w=5: w₆(12) > 5 → DP[6][5] = DP[5][5] = 0
- w=10: w₆(12) > 10 → DP[6][10] = DP[5][10] = 60
- w=15: DP[6][15] = max(DP[5][15], DP[5][3] + 70) = max(120, 0+70) = **120**
- w=20: DP[6][20] = max(DP[5][20], DP[5][8] + 70) = max(120, 45+70) = **120**
- w=25: DP[6][25] = max(DP[5][25], DP[5][13] + 70) = max(180, 60+70) = **180**
- w=30: DP[6][30] = max(DP[5][30], DP[5][18] + 70) = max(180, 120+70) = **190**
- w=35: DP[6][35] = max(DP[5][35], DP[5][23] + 70) = max(240, 120+70) = **240**
- w=40: DP[6][40] = max(DP[5][40], DP[5][28] + 70) = max(300, 180+70) = **300**
- w=45: DP[6][45] = max(DP[5][45], DP[5][33] + 70) = max(300, 180+70) = **300**
- w=50: DP[6][50] = max(DP[5][50], DP[5][38] + 70) = max(360, 240+70) = **360**

**Row 7 (Item 7: Jewelry, w₇=5, v₇=80):**

- w=5: DP[7][5] = max(DP[6][5], DP[6][0] + 80) = max(0, 0+80) = **80**
- w=10: DP[7][10] = max(DP[6][10], DP[6][5] + 80) = max(60, 0+80) = **80**
- w=15: DP[7][15] = max(DP[6][15], DP[6][10] + 80) = max(120, 60+80) = **140**
- w=20: DP[7][20] = max(DP[6][20], DP[6][15] + 80) = max(120, 120+80) = **200**
- w=25: DP[7][25] = max(DP[6][25], DP[6][20] + 80) = max(180, 120+80) = **200**
- w=30: DP[7][30] = max(DP[6][30], DP[6][25] + 80) = max(190, 180+80) = **260**
- w=35: DP[7][35] = max(DP[6][35], DP[6][30] + 80) = max(240, 190+80) = **270**
- w=40: DP[7][40] = max(DP[6][40], DP[6][35] + 80) = max(300, 240+80) = **320**
- w=45: DP[7][45] = max(DP[6][45], DP[6][40] + 80) = max(300, 300+80) = **380**
- w=50: DP[7][50] = max(DP[6][50], DP[6][45] + 80) = max(360, 300+80) = **380**

### Final DP Table (Simplified - Key Weights)

| Item | w=0 | w=5 | w=10 | w=15 | w=20 | w=25 | w=30 | w=35 | w=40 | w=45 | w=50 |
|------|-----|-----|------|------|------|------|------|------|------|------|------|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 |
| 2 | 0 | 0 | 60 | 60 | 100 | 100 | 160 | 160 | 160 | 160 | 160 |
| 3 | 0 | 0 | 60 | 120 | 120 | 180 | 180 | 220 | 220 | 280 | 280 |
| 4 | 0 | 0 | 60 | 120 | 120 | 180 | 180 | 240 | 300 | 300 | 360 |
| 5 | 0 | 0 | 60 | 120 | 120 | 180 | 180 | 240 | 300 | 300 | 360 |
| 6 | 0 | 0 | 60 | 120 | 120 | 180 | 190 | 240 | 300 | 300 | 360 |
| 7 | 0 | 80 | 80 | 140 | 200 | 200 | 260 | 270 | 320 | 380 | 380 |

### Backtracking to Find Selected Items

Starting from DP[7][50] = 380, we backtrack to find which items were selected:

**Step 1:** At DP[7][50] = 380
- Check: DP[7][50] (380) ≠ DP[6][50] (360)
- **Item 7 (Jewelry) is SELECTED**
- New capacity: 50 - 5 = 45 kg
- Move to DP[6][45]

**Step 2:** At DP[6][45] = 300
- Check: DP[6][45] (300) = DP[5][45] (300)
- **Item 6 (Textiles) is NOT selected**
- Move to DP[5][45]

**Step 3:** At DP[5][45] = 300
- Check: DP[5][45] (300) = DP[4][45] (300)
- **Item 5 (Perishable Goods) is NOT selected**
- Move to DP[4][45]

**Step 4:** At DP[4][45] = 300
- Check: DP[4][45] (300) ≠ DP[3][45] (280)
- **Item 4 (Machine Parts) is SELECTED**
- New capacity: 45 - 25 = 20 kg
- Move to DP[3][20]

**Step 5:** At DP[3][20] = 120
- Check: DP[3][20] (120) = DP[2][20] (100)... NO, 120 ≠ 100
- **Item 3 (Documents) is SELECTED**
- New capacity: 20 - 15 = 5 kg
- Move to DP[2][5]

**Step 6:** At DP[2][5] = 0
- Check: DP[2][5] (0) = DP[1][5] (0)
- **Item 2 (Electronics) is NOT selected**
- Move to DP[1][5]

**Step 7:** At DP[1][5] = 0
- Check: DP[1][5] (0) = DP[0][5] (0)
- **Item 1 (Medical Supplies) is NOT selected**
- Done (reached row 0)

### Final Solution (Dynamic Programming)

**Selected Items:**
1. Item 7: Jewelry (5 kg, $80)
2. Item 4: Machine Parts (25 kg, $180)
3. Item 3: Documents (15 kg, $120)

**Total Weight:** 45 kg (out of 50 kg capacity)
**Total Value:** $380
**Capacity Utilization:** 90%

---

## Section 2: Greedy Algorithm Solution

### Step 1: Calculate Value-to-Weight Ratios

| Item # | Item Name | Weight (kg) | Value ($) | Ratio ($/kg) |
|--------|-----------|-------------|-----------|--------------|
| 1 | Medical Supplies | 10 | 60 | 60/10 = **6.00** |
| 2 | Electronics | 20 | 100 | 100/20 = **5.00** |
| 3 | Documents | 15 | 120 | 120/15 = **8.00** |
| 4 | Machine Parts | 25 | 180 | 180/25 = **7.20** |
| 5 | Perishable Goods | 8 | 45 | 45/8 = **5.63** |
| 6 | Textiles | 12 | 70 | 70/12 = **5.83** |
| 7 | Jewelry | 5 | 80 | 80/5 = **16.00** |

### Step 2: Sort Items by Ratio (Descending Order)

| Rank | Item # | Item Name | Weight (kg) | Value ($) | Ratio ($/kg) |
|------|--------|-----------|-------------|-----------|--------------|
| 1 | 7 | Jewelry | 5 | 80 | 16.00 |
| 2 | 3 | Documents | 15 | 120 | 8.00 |
| 3 | 4 | Machine Parts | 25 | 180 | 7.20 |
| 4 | 1 | Medical Supplies | 10 | 60 | 6.00 |
| 5 | 6 | Textiles | 12 | 70 | 5.83 |
| 6 | 5 | Perishable Goods | 8 | 45 | 5.63 |
| 7 | 2 | Electronics | 20 | 100 | 5.00 |

### Step 3: Greedy Selection Process (0/1 Version)

**Initial Capacity:** 50 kg

**Iteration 1: Consider Jewelry**
- Weight: 5 kg, Value: $80, Ratio: 16.00
- Can fit? 5 kg ≤ 50 kg → **YES**
- **Action:** SELECT Jewelry
- Running totals: Weight = 5 kg, Value = $80
- Remaining capacity: 50 - 5 = 45 kg

**Iteration 2: Consider Documents**
- Weight: 15 kg, Value: $120, Ratio: 8.00
- Can fit? 15 kg ≤ 45 kg → **YES**
- **Action:** SELECT Documents
- Running totals: Weight = 20 kg, Value = $200
- Remaining capacity: 45 - 15 = 30 kg

**Iteration 3: Consider Machine Parts**
- Weight: 25 kg, Value: $180, Ratio: 7.20
- Can fit? 25 kg ≤ 30 kg → **YES**
- **Action:** SELECT Machine Parts
- Running totals: Weight = 45 kg, Value = $380
- Remaining capacity: 30 - 25 = 5 kg

**Iteration 4: Consider Medical Supplies**
- Weight: 10 kg, Value: $60, Ratio: 6.00
- Can fit? 10 kg ≤ 5 kg → **NO**
- **Action:** REJECT Medical Supplies

**Iteration 5: Consider Textiles**
- Weight: 12 kg, Value: $70, Ratio: 5.83
- Can fit? 12 kg ≤ 5 kg → **NO**
- **Action:** REJECT Textiles

**Iteration 6: Consider Perishable Goods**
- Weight: 8 kg, Value: $45, Ratio: 5.63
- Can fit? 8 kg ≤ 5 kg → **NO**
- **Action:** REJECT Perishable Goods

**Iteration 7: Consider Electronics**
- Weight: 20 kg, Value: $100, Ratio: 5.00
- Can fit? 20 kg ≤ 5 kg → **NO**
- **Action:** REJECT Electronics

### Final Solution (Greedy 0/1)

**Selected Items:**
1. Jewelry (5 kg, $80)
2. Documents (15 kg, $120)
3. Machine Parts (25 kg, $180)

**Total Weight:** 45 kg (out of 50 kg capacity)
**Total Value:** $380
**Capacity Utilization:** 90%

### Step 4: Greedy Selection Process (Fractional Version)

Using the same sorted order:

**Iteration 1: Consider Jewelry**
- Weight: 5 kg, Value: $80, Ratio: 16.00
- Can fit fully? 5 kg ≤ 50 kg → **YES**
- **Action:** SELECT 100% of Jewelry
- Running totals: Weight = 5 kg, Value = $80
- Remaining capacity: 45 kg

**Iteration 2: Consider Documents**
- Weight: 15 kg, Value: $120, Ratio: 8.00
- Can fit fully? 15 kg ≤ 45 kg → **YES**
- **Action:** SELECT 100% of Documents
- Running totals: Weight = 20 kg, Value = $200
- Remaining capacity: 30 kg

**Iteration 3: Consider Machine Parts**
- Weight: 25 kg, Value: $180, Ratio: 7.20
- Can fit fully? 25 kg ≤ 30 kg → **YES**
- **Action:** SELECT 100% of Machine Parts
- Running totals: Weight = 45 kg, Value = $380
- Remaining capacity: 5 kg

**Iteration 4: Consider Medical Supplies**
- Weight: 10 kg, Value: $60, Ratio: 6.00
- Can fit fully? 10 kg ≤ 5 kg → **NO**
- Can fit partially? YES
- Fraction that fits: 5/10 = 0.5 (50%)
- Fractional value: $60 × 0.5 = $30
- **Action:** SELECT 50% of Medical Supplies
- Running totals: Weight = 50 kg, Value = $410
- Remaining capacity: 0 kg (FULL)

**Process terminates** (capacity fully utilized)

### Final Solution (Greedy Fractional)

**Selected Items:**
1. Jewelry - 5 kg (100%), $80
2. Documents - 15 kg (100%), $120
3. Machine Parts - 25 kg (100%), $180
4. Medical Supplies - 5 kg (50%), $30

**Total Weight:** 50 kg (out of 50 kg capacity)
**Total Value:** $410
**Capacity Utilization:** 100%

---

## Section 3: Comparative Summary

| Algorithm | Items Selected | Total Weight | Total Value | Capacity Used | Optimal? |
|-----------|---------------|--------------|-------------|---------------|----------|
| Dynamic Programming | Jewelry, Documents, Machine Parts | 45 kg | $380 | 90% | ✓ Yes |
| Greedy (0/1) | Jewelry, Documents, Machine Parts | 45 kg | $380 | 90% | Coincidental |
| Greedy (Fractional) | Above + 50% Medical Supplies | 50 kg | $410 | 100% | ✓ Yes |

### Key Observations

1. **Dynamic Programming** guarantees the optimal solution for 0/1 knapsack
2. **Greedy (0/1)** happened to find the optimal solution for this dataset, but this is not guaranteed in general
3. **Greedy (Fractional)** achieves the highest value by utilizing 100% of capacity
4. The greedy approach is faster (O(n log n)) compared to DP (O(n × W))
5. For this problem instance, both DP and Greedy (0/1) selected the same items

### Example Where Greedy Fails (0/1)

Consider: Capacity = 10 kg
- Item A: 6 kg, $10 (ratio = 1.67)
- Item B: 5 kg, $8 (ratio = 1.6)
- Item C: 4 kg, $6 (ratio = 1.5)

Greedy selects: A (6kg, $10) → Can't fit B or C together → Total = $10
Optimal (DP): B + C (9kg, $14) → Total = $14

This demonstrates why DP is necessary for guaranteed optimal solutions in 0/1 knapsack.
