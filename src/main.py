"""
Main Driver Program for Airline Cargo Loading Optimization
Using Knapsack Problem Solutions

Assignment 03 - Design and Analysis of Algorithms (CSC-321)

@author Basim Gul
@course CSC-321 - BS(CS)-5
@instructor Dr. Muhammad Tariq Siddique
@date December 14, 2025
"""

import math
from dynamic_programming_knapsack import DynamicProgrammingKnapsack
from greedy_knapsack import GreedyKnapsack


def print_header():
    """Print program header."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║   ASSIGNMENT 03: KNAPSACK PROBLEM APPLICATION" + " " * 11 + "║")
    print("║     Air Flight Cargo Loading Optimization" + " " * 16 + "║")
    print("╠" + "=" * 58 + "╣")
    print("║ Student: Basim Gul" + " " * 40 + "║")
    print("║ Course:  CSC-321 (DAA) - BS(CS)-5" + " " * 24 + "║")
    print("║ Instructor: Dr. Muhammad Tariq Siddique" + " " * 18 + "║")
    print("╚" + "=" * 58 + "╝")
    print("\n")


def print_comparative_analysis(items, weights, values, capacity,
                              dp_value, dp_weight, dp_selected,
                              greedy_01_value, greedy_01_weight, greedy_01_selected,
                              greedy_fractional_value):
    """Print comparative analysis of all algorithms."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║           COMPARATIVE ANALYSIS" + " " * 28 + "║")
    print("╚" + "=" * 58 + "╝")
    
    print("\n" + "=" * 60)
    print("ALGORITHM COMPARISON TABLE")
    print("=" * 60 + "\n")
    
    print(f"{'Algorithm':<27} | {'Total Value':<12} | {'Total Weight':<12} | {'Capacity Used':<15}")
    print("-" * 78)
    
    print(f"{'Dynamic Programming':<27} | ${dp_value:<11} | {dp_weight:<11}kg | {(dp_weight * 100.0) / capacity:>14.2f}%")
    print(f"{'Greedy (0/1)':<27} | ${greedy_01_value:<11.0f} | {greedy_01_weight:<11}kg | {(greedy_01_weight * 100.0) / capacity:>14.2f}%")
    print(f"{'Greedy (Fractional)':<27} | ${greedy_fractional_value:<11.2f} | {capacity:<11}kg | {100.0:>14.2f}%")
    
    print("\n" + "=" * 60)
    print("ITEM SELECTION COMPARISON")
    print("=" * 60 + "\n")
    
    print(f"{'Item':<20} | {'Details':<8} | {'DP Selected':<15} | {'Greedy Selected':<15}")
    print("-" * 72)
    
    for i in range(len(items)):
        details = f"{weights[i]}kg/${values[i]}"
        dp_status = "✓ YES" if dp_selected[i] else "✗ NO"
        greedy_status = "✓ YES" if greedy_01_selected[i] else "✗ NO"
        
        print(f"{items[i]:<20} | {details:<8} | {dp_status:<15} | {greedy_status:<15}")
    
    print("\n" + "=" * 60)
    print("PERFORMANCE METRICS")
    print("=" * 60 + "\n")
    
    n = len(items)
    print("Time Complexity:")
    print("-" * 16)
    print(f"Dynamic Programming: O(n × W) = O({n} × {capacity}) = O({n * capacity})")
    print(f"Greedy Algorithm:    O(n log n) = O({n} log {n}) ≈ O({int(n * math.log2(n))})")
    
    print("\nSpace Complexity:")
    print("-" * 17)
    print(f"Dynamic Programming: O(n × W) = O({n} × {capacity}) = O({n * capacity})")
    print(f"Greedy Algorithm:    O(n) = O({n})")
    
    print("\nOptimality:")
    print("-" * 11)
    print("Dynamic Programming (0/1): OPTIMAL ✓")
    print("Greedy (0/1):              NOT GUARANTEED")
    print("Greedy (Fractional):       OPTIMAL ✓")
    
    print("\n" + "=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60 + "\n")
    
    if dp_value == int(greedy_01_value):
        print("✓ Both DP and Greedy (0/1) achieved the same optimal value!")
        print("  This demonstrates that for this particular dataset,")
        print("  the greedy approach happened to find the optimal solution.")
    elif dp_value > greedy_01_value:
        difference = dp_value - int(greedy_01_value)
        percentage = (difference * 100.0) / dp_value
        print(f"⚠ Dynamic Programming achieved ${difference} more value ({percentage:.2f}% better)")
        print("  This demonstrates why DP guarantees optimal solutions")
        print("  while greedy approach may miss the optimal in 0/1 knapsack.")
    
    print(f"\n✓ Greedy (Fractional) achieved maximum possible value of ${greedy_fractional_value:.2f}")
    print("  by utilizing 100% of the capacity with fractional items.")
    print()


def print_recommendations():
    """Print recommendations for airline operations."""
    print("\n" + "=" * 60)
    print("RECOMMENDATIONS FOR AIRLINE CARGO MANAGEMENT")
    print("=" * 60 + "\n")
    
    print("1. When to Use Dynamic Programming:")
    print("   • Items cannot be split (0/1 constraint)")
    print("   • Optimal solution is critical")
    print("   • Dataset is moderately sized (n ≤ 1000, W ≤ 10000)")
    print("   • Have computational resources available")
    print()
    
    print("2. When to Use Greedy Algorithm:")
    print("   • Items can be split (fractional knapsack)")
    print("   • Need fast computation (real-time decisions)")
    print("   • Large datasets (n > 10000)")
    print("   • Approximate solution is acceptable (0/1 case)")
    print()
    
    print("3. Practical Considerations:")
    print("   • Consider item priority (medical supplies first)")
    print("   • Factor in handling time and space requirements")
    print("   • Account for weight distribution for flight balance")
    print("   • Include safety margins in weight calculations")
    print()
    
    print("4. Hybrid Approach:")
    print("   • Use greedy for initial quick estimate")
    print("   • Apply DP for final optimization if time permits")
    print("   • Combine with other constraints (volume, fragility)")
    print()


def main():
    """Main function to run all knapsack algorithms."""
    print_header()
    
    # Define the airline cargo loading problem
    items = [
        "Medical Supplies",
        "Electronics",
        "Documents",
        "Machine Parts",
        "Perishable Goods",
        "Textiles",
        "Jewelry"
    ]
    
    weights = [10, 20, 15, 25, 8, 12, 5]  # in kg
    values = [60, 100, 120, 180, 45, 70, 80]  # in dollars
    capacity = 50  # maximum capacity in kg
    
    print("=" * 60)
    print("PROBLEM DEFINITION: AIRLINE CARGO LOADING")
    print("=" * 60)
    print("\nScenario: An airline needs to optimize cargo loading")
    print("for a flight with limited weight capacity.\n")
    print(f"Maximum Cargo Capacity: {capacity} kg\n")
    
    print("Available Items:")
    print("-" * 16)
    print(f"{'Item':<20} | {'Weight(kg)':<10} | {'Value($)':<10}")
    print("-" * 51)
    for i in range(len(items)):
        print(f"{items[i]:<20} | {weights[i]:>10} | {values[i]:>10}")
    print()
    
    # Solve using Dynamic Programming
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║        SOLUTION 1: DYNAMIC PROGRAMMING" + " " * 19 + "║")
    print("╚" + "=" * 58 + "╝")
    
    dp_solver = DynamicProgrammingKnapsack(items, weights, values, capacity)
    dp_max_value = dp_solver.solve()
    dp_total_weight = dp_solver.get_total_weight()
    dp_selected = dp_solver.get_selected_items()
    
    # Solve using Greedy Algorithm (0/1 version)
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║        SOLUTION 2: GREEDY ALGORITHM (0/1)" + " " * 16 + "║")
    print("╚" + "=" * 58 + "╝")
    
    greedy_solver = GreedyKnapsack(items, weights, values, capacity)
    greedy_01_max_value = greedy_solver.solve_01()
    
    # Get greedy 0/1 total weight
    greedy_01_selected = greedy_solver.get_selected_items_01()
    greedy_01_total_weight = sum(weights[i] for i in range(len(items)) if greedy_01_selected[i])
    
    # Solve using Greedy Algorithm (Fractional version)
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║    SOLUTION 3: GREEDY ALGORITHM (FRACTIONAL)" + " " * 13 + "║")
    print("╚" + "=" * 58 + "╝")
    
    greedy_fractional = GreedyKnapsack(items, weights, values, capacity)
    greedy_fractional_value = greedy_fractional.solve_fractional()
    
    # Comparative Analysis
    print_comparative_analysis(items, weights, values, capacity,
                              dp_max_value, dp_total_weight, dp_selected,
                              greedy_01_max_value, greedy_01_total_weight, greedy_01_selected,
                              greedy_fractional_value)
    
    # Print recommendations
    print_recommendations()
    
    print("\n" + "=" * 60)
    print("PROGRAM EXECUTION COMPLETED SUCCESSFULLY")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
