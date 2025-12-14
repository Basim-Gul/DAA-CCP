"""
===============================================================================
Assignment 03: Knapsack Problem Application - Air Flight Cargo Optimization
===============================================================================

Comprehensive Implementation with Dynamic Programming and Greedy Algorithms
Including Visualizations and Detailed Analysis

@author: Basim Gul
@course: Design and Analysis of Algorithms (CSC-321) - BS(CS)-5
@instructor: Dr. Muhammad Tariq Siddique
@date: December 14, 2025

===============================================================================
"""

import time
import math
import sys

# Try to import matplotlib for visualizations
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.gridspec import GridSpec
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Note: matplotlib not available. Graphs will be skipped.")
    print("Install with: pip install matplotlib\n")


# ============================================================================
# DYNAMIC PROGRAMMING IMPLEMENTATION
# ============================================================================

class DynamicProgrammingKnapsack:
    """
    Solver for 0/1 Knapsack problem using Dynamic Programming approach.
    
    Time Complexity: O(n * W) where n is number of items and W is capacity
    Space Complexity: O(n * W) for the DP table
    """
    
    def __init__(self, items, weights, values, capacity):
        """Initialize the knapsack problem."""
        self.items = items
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.num_items = len(items)
        self.dp_table = [[0 for _ in range(capacity + 1)] 
                         for _ in range(self.num_items + 1)]
        self.selected_items = [False] * self.num_items
        self.execution_time = 0
        
    def solve(self):
        """Solve the 0/1 knapsack problem using Dynamic Programming."""
        start_time = time.time()
        
        print("\n" + "=" * 70)
        print(" " * 15 + "DYNAMIC PROGRAMMING APPROACH - 0/1 KNAPSACK")
        print("=" * 70 + "\n")
        
        # Build the DP table
        self._build_dp_table()
        
        # Display the complete DP table
        self._display_dp_table()
        
        # Backtrack to find selected items
        self._backtrack()
        
        end_time = time.time()
        self.execution_time = (end_time - start_time) * 1000
        
        # Display results
        self._display_results()
        
        return self.dp_table[self.num_items][self.capacity]
    
    def _build_dp_table(self):
        """Build the DP table using bottom-up approach."""
        print("Building DP Table:")
        print("State Transition: DP[i][w] = max(DP[i-1][w], DP[i-1][w-weight[i]] + value[i])")
        print()
        
        # Fill the DP table
        for i in range(1, self.num_items + 1):
            for w in range(1, self.capacity + 1):
                item_index = i - 1
                item_weight = self.weights[item_index]
                item_value = self.values[item_index]
                
                if item_weight > w:
                    self.dp_table[i][w] = self.dp_table[i-1][w]
                else:
                    exclude_item = self.dp_table[i-1][w]
                    include_item = self.dp_table[i-1][w - item_weight] + item_value
                    self.dp_table[i][w] = max(exclude_item, include_item)
    
    def _display_dp_table(self):
        """Display the complete DP table with formatting."""
        print("\nComplete DP Table (showing key weight columns):")
        print("=" * 100)
        
        # Show selected weight columns for better visibility
        key_weights = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        
        # Print header
        print(f"{'Item/Weight':<15} |", end="")
        for w in key_weights:
            if w <= self.capacity:
                print(f"{w:5} |", end="")
        print()
        
        # Print separator
        print("-" * 15 + "+" + "-" * (7 * len([w for w in key_weights if w <= self.capacity])))
        
        # Print rows
        for i in range(self.num_items + 1):
            if i == 0:
                row_label = "None"
            else:
                item_name = self.items[i-1]
                if len(item_name) > 14:
                    item_name = item_name[:11] + "..."
                row_label = item_name
            
            print(f"{row_label:<15} |", end="")
            
            for w in key_weights:
                if w <= self.capacity:
                    print(f"{self.dp_table[i][w]:5} |", end="")
            print()
        print()
    
    def _backtrack(self):
        """Backtrack through the DP table to find which items were selected."""
        print("\nBacktracking to find selected items:")
        print("=" * 50)
        
        i = self.num_items
        w = self.capacity
        
        while i > 0 and w > 0:
            if self.dp_table[i][w] != self.dp_table[i-1][w]:
                self.selected_items[i-1] = True
                print(f"  Step: DP[{i}][{w}] ≠ DP[{i-1}][{w}] → Item {i} ({self.items[i-1]}) SELECTED")
                w -= self.weights[i-1]
            else:
                print(f"  Step: DP[{i}][{w}] = DP[{i-1}][{w}] → Item {i} ({self.items[i-1]}) NOT selected")
            i -= 1
        print()
    
    def _display_results(self):
        """Display the final results."""
        print("\n" + "=" * 70)
        print(" " * 20 + "DYNAMIC PROGRAMMING RESULTS")
        print("=" * 70)
        
        print("\n📦 Selected Items:")
        print("-" * 70)
        total_weight = 0
        total_value = 0
        
        for i in range(self.num_items):
            if self.selected_items[i]:
                print(f"  ✓ {self.items[i]:<20} Weight: {self.weights[i]:>3}kg   Value: ${self.values[i]:>3}")
                total_weight += self.weights[i]
                total_value += self.values[i]
        
        print("\n📊 Summary Statistics:")
        print("-" * 70)
        print(f"  • Total Weight Used:      {total_weight} kg / {self.capacity} kg")
        print(f"  • Total Value Achieved:   ${total_value}")
        print(f"  • Capacity Utilization:   {(total_weight * 100.0) / self.capacity:.2f}%")
        print(f"  • Unused Capacity:        {self.capacity - total_weight} kg")
        print(f"  • Execution Time:         {self.execution_time:.4f} ms")
        
        print("\n⚙️  Complexity Analysis:")
        print("-" * 70)
        print(f"  • Time Complexity:  O(n × W) = O({self.num_items} × {self.capacity}) = O({self.num_items * self.capacity})")
        print(f"  • Space Complexity: O(n × W) = O({self.num_items} × {self.capacity}) = O({self.num_items * self.capacity})")
        print("=" * 70 + "\n")
    
    def get_selected_items(self):
        """Get the selected items."""
        return self.selected_items
    
    def get_total_weight(self):
        """Get total weight of selected items."""
        total_weight = 0
        for i in range(self.num_items):
            if self.selected_items[i]:
                total_weight += self.weights[i]
        return total_weight


# ============================================================================
# GREEDY ALGORITHM IMPLEMENTATION
# ============================================================================

class Item:
    """Class to represent an item with its properties."""
    
    def __init__(self, name, weight, value, index):
        """Initialize an item."""
        self.name = name
        self.weight = weight
        self.value = value
        self.ratio = value / weight
        self.original_index = index
    
    def __lt__(self, other):
        """Compare items by ratio for sorting (descending order)."""
        return self.ratio > other.ratio


class GreedyKnapsack:
    """
    Solver for Knapsack problem using Greedy Algorithm approach.
    
    Time Complexity: O(n log n) for sorting + O(n) for selection
    Space Complexity: O(n) for storing item information
    """
    
    def __init__(self, item_names, weights, values, capacity):
        """Initialize the knapsack problem."""
        self.capacity = capacity
        n = len(item_names)
        self.items = [Item(item_names[i], weights[i], values[i], i) for i in range(n)]
        self.selected_items_01 = [False] * n
        self.fractional_amounts = [0.0] * n
        self.execution_time_01 = 0
        self.execution_time_fractional = 0
    
    def solve_01(self):
        """Solve using Greedy approach - 0/1 version."""
        start_time = time.time()
        
        print("\n" + "=" * 70)
        print(" " * 18 + "GREEDY ALGORITHM APPROACH - 0/1 VERSION")
        print("=" * 70 + "\n")
        
        self._display_ratios()
        self._sort_items()
        total_value = self._select_items_01()
        
        end_time = time.time()
        self.execution_time_01 = (end_time - start_time) * 1000
        
        self._display_results_01(total_value)
        
        return total_value
    
    def solve_fractional(self):
        """Solve using Greedy approach - Fractional version."""
        start_time = time.time()
        
        print("\n" + "=" * 70)
        print(" " * 15 + "GREEDY ALGORITHM APPROACH - FRACTIONAL VERSION")
        print("=" * 70 + "\n")
        
        self._display_ratios()
        self._sort_items()
        total_value = self._select_items_fractional()
        
        end_time = time.time()
        self.execution_time_fractional = (end_time - start_time) * 1000
        
        self._display_results_fractional(total_value)
        
        return total_value
    
    def _display_ratios(self):
        """Display value-to-weight ratios for all items."""
        print("Step 1: Calculate Value-to-Weight Ratios")
        print("=" * 70)
        print(f"{'Item':<25} {'Weight':>10} {'Value':>10} {'Ratio ($/kg)':>15}")
        print("-" * 70)
        
        for item in self.items:
            print(f"{item.name:<25} {item.weight:>8}kg ${item.value:>8} {item.ratio:>14.2f}")
        print()
    
    def _sort_items(self):
        """Sort items by value-to-weight ratio in descending order."""
        print("Step 2: Sort Items by Ratio (Descending Order)")
        print("=" * 70)
        
        self.items.sort()
        
        print("Sorted Order:")
        for i, item in enumerate(self.items, 1):
            print(f"  {i}. {item.name:<25} (Ratio: {item.ratio:.2f} $/kg)")
        print()
    
    def _select_items_01(self):
        """Select items greedily for 0/1 knapsack."""
        print("Step 3: Greedy Selection Process (0/1 - Items Cannot be Split)")
        print("=" * 70)
        
        remaining_capacity = self.capacity
        total_value = 0
        total_weight = 0
        
        print(f"Initial Capacity: {self.capacity} kg\n")
        
        for item in self.items:
            if item.weight <= remaining_capacity:
                self.selected_items_01[item.original_index] = True
                remaining_capacity -= item.weight
                total_value += item.value
                total_weight += item.weight
                
                print(f"  ✓ SELECTED: {item.name}")
                print(f"    • Weight: {item.weight}kg, Value: ${item.value}, Ratio: {item.ratio:.2f}")
                print(f"    • Running Total: Weight={total_weight}kg, Value=${total_value}")
                print(f"    • Remaining Capacity: {remaining_capacity}kg\n")
            else:
                print(f"  ✗ REJECTED: {item.name}")
                print(f"    • Weight: {item.weight}kg > Remaining: {remaining_capacity}kg\n")
        
        return total_value
    
    def _select_items_fractional(self):
        """Select items greedily for fractional knapsack."""
        print("Step 3: Greedy Selection Process (Fractional - Items Can be Split)")
        print("=" * 70)
        
        remaining_capacity = float(self.capacity)
        total_value = 0.0
        total_weight = 0.0
        
        print(f"Initial Capacity: {self.capacity} kg\n")
        
        for item in self.items:
            if item.weight <= remaining_capacity:
                self.fractional_amounts[item.original_index] = 1.0
                remaining_capacity -= item.weight
                total_value += item.value
                total_weight += item.weight
                
                print(f"  ✓ SELECTED (Full): {item.name}")
                print(f"    • Weight: {item.weight}kg (100%), Value: ${item.value}, Ratio: {item.ratio:.2f}")
                print(f"    • Running Total: Weight={total_weight:.2f}kg, Value=${total_value:.2f}")
                print(f"    • Remaining Capacity: {remaining_capacity:.2f}kg\n")
            elif remaining_capacity > 0:
                fraction = remaining_capacity / item.weight
                self.fractional_amounts[item.original_index] = fraction
                fractional_value = item.value * fraction
                
                total_value += fractional_value
                total_weight += remaining_capacity
                
                print(f"  ✓ SELECTED (Partial): {item.name}")
                print(f"    • Weight: {remaining_capacity:.2f}kg ({fraction * 100:.1f}%), Value: ${fractional_value:.2f}")
                print(f"    • Running Total: Weight={total_weight:.2f}kg, Value=${total_value:.2f}")
                print(f"    • Remaining Capacity: 0kg (FULL)\n")
                
                remaining_capacity = 0
                break
        
        return total_value
    
    def _display_results_01(self, total_value):
        """Display results for 0/1 version."""
        print("\n" + "=" * 70)
        print(" " * 18 + "GREEDY ALGORITHM RESULTS (0/1 VERSION)")
        print("=" * 70)
        
        print("\n📦 Selected Items:")
        print("-" * 70)
        total_weight = 0
        
        for item in self.items:
            if self.selected_items_01[item.original_index]:
                print(f"  ✓ {item.name:<20} Weight: {item.weight:>3}kg   Value: ${item.value:>3}")
                total_weight += item.weight
        
        print("\n📊 Summary Statistics:")
        print("-" * 70)
        print(f"  • Total Weight Used:      {total_weight} kg / {self.capacity} kg")
        print(f"  • Total Value Achieved:   ${total_value:.0f}")
        print(f"  • Capacity Utilization:   {(total_weight * 100.0) / self.capacity:.2f}%")
        print(f"  • Unused Capacity:        {self.capacity - total_weight} kg")
        print(f"  • Execution Time:         {self.execution_time_01:.4f} ms")
        
        print("\n⚙️  Complexity Analysis:")
        print("-" * 70)
        n = len(self.items)
        print(f"  • Time Complexity:  O(n log n) = O({n} log {n}) ≈ O({int(n * math.log2(n))})")
        print(f"  • Space Complexity: O(n) = O({n})")
        print("=" * 70 + "\n")
    
    def _display_results_fractional(self, total_value):
        """Display results for fractional version."""
        print("\n" + "=" * 70)
        print(" " * 15 + "GREEDY ALGORITHM RESULTS (FRACTIONAL VERSION)")
        print("=" * 70)
        
        print("\n📦 Selected Items:")
        print("-" * 70)
        total_weight = 0.0
        
        for item in self.items:
            fraction = self.fractional_amounts[item.original_index]
            if fraction > 0:
                if fraction == 1.0:
                    print(f"  ✓ {item.name:<20} Weight: {item.weight:>3}kg (Full)   Value: ${item.value:>3}")
                    total_weight += item.weight
                else:
                    partial_weight = item.weight * fraction
                    partial_value = item.value * fraction
                    print(f"  ✓ {item.name:<20} Weight: {partial_weight:>5.2f}kg ({fraction * 100:>5.1f}%)  Value: ${partial_value:>6.2f}")
                    total_weight += partial_weight
        
        print("\n📊 Summary Statistics:")
        print("-" * 70)
        print(f"  • Total Weight Used:      {total_weight:.2f} kg / {self.capacity} kg")
        print(f"  • Total Value Achieved:   ${total_value:.2f}")
        print(f"  • Capacity Utilization:   {(total_weight * 100.0) / self.capacity:.2f}%")
        print(f"  • Execution Time:         {self.execution_time_fractional:.4f} ms")
        
        print("\n⚙️  Complexity Analysis:")
        print("-" * 70)
        n = len(self.items)
        print(f"  • Time Complexity:  O(n log n) = O({n} log {n}) ≈ O({int(n * math.log2(n))})")
        print(f"  • Space Complexity: O(n) = O({n})")
        print("=" * 70 + "\n")
    
    def get_selected_items_01(self):
        """Get selected items for 0/1 version."""
        return self.selected_items_01


# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def create_visualizations(items, weights, values, capacity,
                         dp_value, dp_weight, dp_selected,
                         greedy_01_value, greedy_01_weight, greedy_01_selected,
                         greedy_frac_value, dp_time, greedy_01_time, greedy_frac_time):
    """Create comprehensive visualizations of the results."""
    
    if not MATPLOTLIB_AVAILABLE:
        print("\n⚠️  Matplotlib not available. Skipping visualizations.")
        return
    
    print("\n" + "=" * 70)
    print(" " * 20 + "GENERATING VISUALIZATIONS")
    print("=" * 70)
    print("\nCreating graphs and charts...")
    
    # Create figure with subplots
    fig = plt.figure(figsize=(20, 12))
    gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)
    
    # 1. Value Comparison Bar Chart
    ax1 = fig.add_subplot(gs[0, 0])
    algorithms = ['DP\n(0/1)', 'Greedy\n(0/1)', 'Greedy\n(Fractional)']
    values_list = [dp_value, greedy_01_value, greedy_frac_value]
    colors = ['#2ecc71', '#3498db', '#e74c3c']
    bars = ax1.bar(algorithms, values_list, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    ax1.set_ylabel('Total Value ($)', fontsize=12, fontweight='bold')
    ax1.set_title('Algorithm Value Comparison', fontsize=14, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:.0f}', ha='center', va='bottom', fontweight='bold')
    
    # 2. Weight Utilization Comparison
    ax2 = fig.add_subplot(gs[0, 1])
    weights_list = [dp_weight, greedy_01_weight, capacity]
    utilization = [(w/capacity)*100 for w in weights_list]
    bars = ax2.bar(algorithms, utilization, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    ax2.set_ylabel('Capacity Utilization (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Capacity Utilization Comparison', fontsize=14, fontweight='bold')
    ax2.set_ylim(0, 105)
    ax2.axhline(y=100, color='red', linestyle='--', linewidth=2, label='Full Capacity')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    ax2.legend()
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # 3. Execution Time Comparison
    ax3 = fig.add_subplot(gs[0, 2])
    times = [dp_time, greedy_01_time, greedy_frac_time]
    bars = ax3.bar(algorithms, times, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    ax3.set_ylabel('Execution Time (ms)', fontsize=12, fontweight='bold')
    ax3.set_title('Algorithm Speed Comparison', fontsize=14, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3, linestyle='--')
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}ms', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # 4. Item Selection Comparison (DP vs Greedy 0/1)
    ax4 = fig.add_subplot(gs[1, :2])
    y_pos = range(len(items))
    bar_height = 0.35
    
    dp_colors = ['green' if dp_selected[i] else 'lightgray' for i in range(len(items))]
    greedy_colors = ['blue' if greedy_01_selected[i] else 'lightgray' for i in range(len(items))]
    
    bars1 = ax4.barh([y - bar_height/2 for y in y_pos], 
                     [1 if dp_selected[i] else 0 for i in range(len(items))],
                     bar_height, label='DP', color=dp_colors, alpha=0.7, edgecolor='black')
    bars2 = ax4.barh([y + bar_height/2 for y in y_pos], 
                     [1 if greedy_01_selected[i] else 0 for i in range(len(items))],
                     bar_height, label='Greedy (0/1)', color=greedy_colors, alpha=0.7, edgecolor='black')
    
    ax4.set_yticks(y_pos)
    ax4.set_yticklabels(items)
    ax4.set_xlabel('Selected (1) / Not Selected (0)', fontsize=12, fontweight='bold')
    ax4.set_title('Item Selection Comparison: DP vs Greedy (0/1)', fontsize=14, fontweight='bold')
    ax4.legend()
    ax4.set_xlim(-0.1, 1.2)
    ax4.grid(axis='x', alpha=0.3, linestyle='--')
    
    # 5. Value-to-Weight Ratios
    ax5 = fig.add_subplot(gs[1, 2])
    ratios = [values[i]/weights[i] for i in range(len(items))]
    colors_ratio = ['green' if dp_selected[i] else 'red' for i in range(len(items))]
    bars = ax5.barh(items, ratios, color=colors_ratio, alpha=0.7, edgecolor='black')
    ax5.set_xlabel('Value/Weight Ratio ($/kg)', fontsize=12, fontweight='bold')
    ax5.set_title('Value-to-Weight Ratios\n(Green = Selected by DP)', fontsize=14, fontweight='bold')
    ax5.grid(axis='x', alpha=0.3, linestyle='--')
    for i, (bar, ratio) in enumerate(zip(bars, ratios)):
        width = bar.get_width()
        ax5.text(width, bar.get_y() + bar.get_height()/2.,
                f'{ratio:.2f}', ha='left', va='center', fontweight='bold', fontsize=9)
    
    # 6. Weight vs Value Scatter Plot
    ax6 = fig.add_subplot(gs[2, 0])
    for i in range(len(items)):
        if dp_selected[i]:
            marker, color, size = 'o', 'green', 200
            label = 'Selected (DP)' if i == [j for j in range(len(items)) if dp_selected[j]][0] else ''
        else:
            marker, color, size = 'x', 'red', 150
            label = 'Not Selected' if i == [j for j in range(len(items)) if not dp_selected[j]][0] else ''
        ax6.scatter(weights[i], values[i], marker=marker, s=size, 
                   color=color, alpha=0.7, edgecolors='black', linewidth=2, label=label)
    
    ax6.set_xlabel('Weight (kg)', fontsize=12, fontweight='bold')
    ax6.set_ylabel('Value ($)', fontsize=12, fontweight='bold')
    ax6.set_title('Item Distribution: Weight vs Value', fontsize=14, fontweight='bold')
    ax6.legend()
    ax6.grid(True, alpha=0.3, linestyle='--')
    
    # 7. Capacity Usage Pie Chart (DP)
    ax7 = fig.add_subplot(gs[2, 1])
    used_weight = dp_weight
    unused_weight = capacity - dp_weight
    ax7.pie([used_weight, unused_weight], 
            labels=['Used\nCapacity', 'Unused\nCapacity'],
            colors=['#2ecc71', '#ecf0f1'],
            autopct='%1.1f%%',
            startangle=90,
            explode=(0.05, 0),
            shadow=True,
            textprops={'fontsize': 11, 'fontweight': 'bold'})
    ax7.set_title('Capacity Utilization (DP)\nTotal: {}kg / {}kg'.format(used_weight, capacity), 
                  fontsize=14, fontweight='bold')
    
    # 8. Complexity Comparison
    ax8 = fig.add_subplot(gs[2, 2])
    n = len(items)
    dp_complexity = n * capacity
    greedy_complexity = int(n * math.log2(n)) if n > 0 else 0
    
    complexities = [dp_complexity, greedy_complexity]
    labels = [f'DP\nO(n×W)\n={dp_complexity}', f'Greedy\nO(n log n)\n≈{greedy_complexity}']
    colors_comp = ['#2ecc71', '#3498db']
    bars = ax8.bar(range(2), complexities, color=colors_comp, alpha=0.7, 
                   edgecolor='black', linewidth=2, tick_label=labels)
    ax8.set_ylabel('Operations Count', fontsize=12, fontweight='bold')
    ax8.set_title('Time Complexity Comparison\n(Theoretical)', fontsize=14, fontweight='bold')
    ax8.grid(axis='y', alpha=0.3, linestyle='--')
    for bar in bars:
        height = bar.get_height()
        ax8.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    # Add main title
    fig.suptitle('Assignment 03: Knapsack Problem - Comprehensive Analysis\n' +
                 'Airline Cargo Loading Optimization',
                 fontsize=18, fontweight='bold', y=0.98)
    
    # Save the figure
    output_path = '/home/runner/work/DAA-CCP/DAA-CCP/report/knapsack_analysis_graphs.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"\n✓ Visualizations saved to: {output_path}")
    
    # Show the plot
    # plt.show()  # Uncomment if running locally with display
    plt.close()
    
    print("✓ Visualization generation complete!")
    print("=" * 70 + "\n")


# ============================================================================
# COMPARATIVE ANALYSIS
# ============================================================================

def print_comparative_analysis(items, weights, values, capacity,
                              dp_value, dp_weight, dp_selected,
                              greedy_01_value, greedy_01_weight, greedy_01_selected,
                              greedy_frac_value, dp_time, greedy_01_time, greedy_frac_time):
    """Print comprehensive comparative analysis."""
    
    print("\n" + "=" * 70)
    print(" " * 20 + "COMPARATIVE ANALYSIS")
    print("=" * 70)
    
    print("\n" + "─" * 70)
    print(" " * 18 + "📊 ALGORITHM COMPARISON TABLE")
    print("─" * 70)
    
    print(f"\n{'Algorithm':<25} {'Value':>12} {'Weight':>12} {'Utilization':>15}")
    print("─" * 70)
    print(f"{'Dynamic Programming':<25} ${dp_value:>11} {dp_weight:>10}kg {(dp_weight/capacity)*100:>13.2f}%")
    print(f"{'Greedy (0/1)':<25} ${greedy_01_value:>11.0f} {greedy_01_weight:>10}kg {(greedy_01_weight/capacity)*100:>13.2f}%")
    print(f"{'Greedy (Fractional)':<25} ${greedy_frac_value:>11.2f} {capacity:>10}kg {100.0:>13.2f}%")
    
    print("\n" + "─" * 70)
    print(" " * 18 + "📦 ITEM SELECTION COMPARISON")
    print("─" * 70)
    
    print(f"\n{'Item':<25} {'Weight/Value':>15} {'DP':>10} {'Greedy 0/1':>15}")
    print("─" * 70)
    for i in range(len(items)):
        details = f"{weights[i]}kg / ${values[i]}"
        dp_status = "✓ YES" if dp_selected[i] else "✗ NO"
        greedy_status = "✓ YES" if greedy_01_selected[i] else "✗ NO"
        print(f"{items[i]:<25} {details:>15} {dp_status:>10} {greedy_status:>15}")
    
    print("\n" + "─" * 70)
    print(" " * 18 + "⚡ PERFORMANCE METRICS")
    print("─" * 70)
    
    n = len(items)
    print("\n⏱️  Execution Time:")
    print(f"  • Dynamic Programming:    {dp_time:.4f} ms")
    print(f"  • Greedy (0/1):           {greedy_01_time:.4f} ms")
    print(f"  • Greedy (Fractional):    {greedy_frac_time:.4f} ms")
    print(f"  • Speedup (Greedy/DP):    {dp_time/greedy_01_time:.2f}x faster")
    
    print("\n📈 Time Complexity:")
    print(f"  • Dynamic Programming:    O(n × W) = O({n} × {capacity}) = O({n * capacity})")
    print(f"  • Greedy Algorithm:       O(n log n) = O({n} log {n}) ≈ O({int(n * math.log2(n))})")
    
    print("\n💾 Space Complexity:")
    print(f"  • Dynamic Programming:    O(n × W) = O({n} × {capacity}) = O({n * capacity})")
    print(f"  • Greedy Algorithm:       O(n) = O({n})")
    
    print("\n🎯 Optimality Guarantees:")
    print("  • Dynamic Programming (0/1):    ✓ OPTIMAL (Guaranteed)")
    print("  • Greedy (0/1):                 ⚠ NOT GUARANTEED (May be suboptimal)")
    print("  • Greedy (Fractional):          ✓ OPTIMAL (Guaranteed)")
    
    print("\n" + "─" * 70)
    print(" " * 18 + "💡 KEY INSIGHTS")
    print("─" * 70)
    print()
    
    if dp_value == int(greedy_01_value):
        print("✓ Both DP and Greedy (0/1) achieved the SAME optimal value of ${}!".format(dp_value))
        print("  → This demonstrates that for this particular dataset, the greedy")
        print("    approach happened to find the optimal solution.")
        print("  → However, this is NOT guaranteed for all datasets.")
    elif dp_value > greedy_01_value:
        difference = dp_value - int(greedy_01_value)
        percentage = (difference * 100.0) / dp_value
        print(f"⚠ Dynamic Programming achieved ${difference} MORE value ({percentage:.2f}% better)")
        print("  → This demonstrates why DP guarantees optimal solutions while")
        print("    greedy approach may miss the optimal in 0/1 knapsack.")
    
    print(f"\n✓ Greedy (Fractional) achieved maximum possible value of ${greedy_frac_value:.2f}")
    print("  → By allowing fractional items, it utilized 100% of the capacity.")
    print("  → This represents the theoretical upper bound for this problem.")
    
    value_efficiency = (dp_value / greedy_frac_value) * 100
    print(f"\n📊 DP achieves {value_efficiency:.2f}% of the fractional knapsack optimal.")
    
    print("\n" + "=" * 70 + "\n")


# ============================================================================
# RECOMMENDATIONS
# ============================================================================

def print_recommendations():
    """Print practical recommendations for airline operations."""
    
    print("\n" + "=" * 70)
    print(" " * 12 + "🎓 RECOMMENDATIONS FOR AIRLINE CARGO MANAGEMENT")
    print("=" * 70)
    
    print("\n1️⃣  WHEN TO USE DYNAMIC PROGRAMMING:")
    print("─" * 70)
    print("  ✓ Items CANNOT be split (0/1 constraint is strict)")
    print("  ✓ Optimal solution is CRITICAL (maximum revenue required)")
    print("  ✓ Dataset is moderately sized (n ≤ 1000, W ≤ 10,000)")
    print("  ✓ Computational resources are available")
    print("  ✓ Solution can be computed offline (not time-critical)")
    print()
    
    print("2️⃣  WHEN TO USE GREEDY ALGORITHM:")
    print("─" * 70)
    print("  ✓ Items CAN be split (fractional knapsack - liquids, powders)")
    print("  ✓ Need FAST computation (real-time loading decisions)")
    print("  ✓ Large datasets (n > 10,000 items)")
    print("  ✓ Approximate solution is acceptable (0/1 case)")
    print("  ✓ Quick estimates needed for planning")
    print()
    
    print("3️⃣  PRACTICAL CONSIDERATIONS:")
    print("─" * 70)
    print("  • Consider item PRIORITY (medical supplies > commercial goods)")
    print("  • Factor in handling time and space requirements")
    print("  • Account for weight DISTRIBUTION for flight balance")
    print("  • Include safety margins in weight calculations (fuel, passengers)")
    print("  • Consider volume constraints (not just weight)")
    print("  • Factor in loading/unloading time windows")
    print()
    
    print("4️⃣  HYBRID APPROACH (RECOMMENDED):")
    print("─" * 70)
    print("  • Phase 1: Use GREEDY for initial quick estimate")
    print("  • Phase 2: Apply DP for final optimization if time permits")
    print("  • Phase 3: Combine with other constraints:")
    print("    - Volume limitations")
    print("    - Item fragility and handling requirements")
    print("    - Destination-based grouping")
    print("    - Priority tiers (emergency, standard, low-priority)")
    print()
    
    print("5️⃣  SCALABILITY CONSIDERATIONS:")
    print("─" * 70)
    print("  • For n=1000, W=10000:")
    print("    - DP: 10,000,000 operations (~acceptable)")
    print("    - Greedy: ~10,000 operations (very fast)")
    print("  • For n=10000, W=100000:")
    print("    - DP: 1,000,000,000 operations (may be slow)")
    print("    - Greedy: ~130,000 operations (still fast)")
    print("  → Consider greedy for very large scale operations")
    print()
    
    print("=" * 70 + "\n")


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def print_header():
    """Print program header."""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + " " * 10 + "ASSIGNMENT 03: KNAPSACK PROBLEM APPLICATION" + " " * 15 + "║")
    print("║" + " " * 15 + "Air Flight Cargo Loading Optimization" + " " * 16 + "║")
    print("║" + " " * 68 + "║")
    print("╠" + "=" * 68 + "╣")
    print("║  Student:    Basim Gul" + " " * 45 + "║")
    print("║  Course:     CSC-321 (DAA) - BS(CS)-5" + " " * 30 + "║")
    print("║  Instructor: Dr. Muhammad Tariq Siddique" + " " * 27 + "║")
    print("║  Date:       December 14, 2025" + " " * 37 + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝")
    print("\n")


def print_problem_definition(items, weights, values, capacity):
    """Print the problem definition."""
    print("=" * 70)
    print(" " * 15 + "📋 PROBLEM DEFINITION")
    print("=" * 70)
    
    print("\n🛫 SCENARIO: Airline Cargo Loading Optimization")
    print("─" * 70)
    print("An airline needs to optimize cargo loading for a flight with")
    print("limited weight capacity. Each item has a weight and revenue value.")
    print("The goal is to maximize total revenue while respecting weight limits.")
    print()
    
    print(f"📊 CONSTRAINTS:")
    print(f"  • Maximum Cargo Capacity: {capacity} kg")
    print(f"  • Number of Items Available: {len(items)}")
    print(f"  • Items cannot be split (0/1 Knapsack for DP)")
    print(f"  • Fractional loading allowed (for Greedy comparison)")
    print()
    
    print("📦 AVAILABLE CARGO ITEMS:")
    print("─" * 70)
    print(f"{'Item':<25} {'Weight':>12} {'Value':>12} {'Ratio ($/kg)':>15}")
    print("─" * 70)
    
    total_weight = sum(weights)
    total_value = sum(values)
    
    for i in range(len(items)):
        ratio = values[i] / weights[i]
        print(f"{items[i]:<25} {weights[i]:>10}kg ${values[i]:>10} {ratio:>14.2f}")
    
    print("─" * 70)
    print(f"{'TOTAL (if all selected)':<25} {total_weight:>10}kg ${total_value:>10}")
    print()
    
    if total_weight <= capacity:
        print(f"⚠️  NOTE: Total weight ({total_weight}kg) ≤ Capacity ({capacity}kg)")
        print("         All items can fit! Knapsack problem is trivial in this case.")
    else:
        print(f"✓ Valid Problem: Total weight ({total_weight}kg) > Capacity ({capacity}kg)")
        print("                 Optimization is required!")
    
    print("\n" + "=" * 70 + "\n")


def main():
    """Main function to run the comprehensive knapsack analysis."""
    
    # Print header
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
    
    # Print problem definition
    print_problem_definition(items, weights, values, capacity)
    
    # ========================================================================
    # SOLUTION 1: DYNAMIC PROGRAMMING
    # ========================================================================
    print("\n" + "╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "SOLUTION 1: DYNAMIC PROGRAMMING" + " " * 22 + "║")
    print("╚" + "=" * 68 + "╝")
    
    dp_solver = DynamicProgrammingKnapsack(items, weights, values, capacity)
    dp_max_value = dp_solver.solve()
    dp_total_weight = dp_solver.get_total_weight()
    dp_selected = dp_solver.get_selected_items()
    dp_time = dp_solver.execution_time
    
    # ========================================================================
    # SOLUTION 2: GREEDY ALGORITHM (0/1)
    # ========================================================================
    print("\n" + "╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "SOLUTION 2: GREEDY ALGORITHM (0/1)" + " " * 19 + "║")
    print("╚" + "=" * 68 + "╝")
    
    greedy_solver = GreedyKnapsack(items, weights, values, capacity)
    greedy_01_max_value = greedy_solver.solve_01()
    greedy_01_selected = greedy_solver.get_selected_items_01()
    greedy_01_total_weight = sum(weights[i] for i in range(len(items)) if greedy_01_selected[i])
    greedy_01_time = greedy_solver.execution_time_01
    
    # ========================================================================
    # SOLUTION 3: GREEDY ALGORITHM (FRACTIONAL)
    # ========================================================================
    print("\n" + "╔" + "=" * 68 + "╗")
    print("║" + " " * 12 + "SOLUTION 3: GREEDY ALGORITHM (FRACTIONAL)" + " " * 15 + "║")
    print("╚" + "=" * 68 + "╝")
    
    greedy_fractional = GreedyKnapsack(items, weights, values, capacity)
    greedy_frac_value = greedy_fractional.solve_fractional()
    greedy_frac_time = greedy_fractional.execution_time_fractional
    
    # ========================================================================
    # COMPARATIVE ANALYSIS
    # ========================================================================
    print_comparative_analysis(items, weights, values, capacity,
                              dp_max_value, dp_total_weight, dp_selected,
                              greedy_01_max_value, greedy_01_total_weight, greedy_01_selected,
                              greedy_frac_value, dp_time, greedy_01_time, greedy_frac_time)
    
    # ========================================================================
    # VISUALIZATIONS
    # ========================================================================
    create_visualizations(items, weights, values, capacity,
                         dp_max_value, dp_total_weight, dp_selected,
                         greedy_01_max_value, greedy_01_total_weight, greedy_01_selected,
                         greedy_frac_value, dp_time, greedy_01_time, greedy_frac_time)
    
    # ========================================================================
    # RECOMMENDATIONS
    # ========================================================================
    print_recommendations()
    
    # ========================================================================
    # CONCLUSION
    # ========================================================================
    print("=" * 70)
    print(" " * 15 + "✅ PROGRAM EXECUTION COMPLETED")
    print("=" * 70)
    print("\n📝 Summary:")
    print(f"  • Dynamic Programming found optimal value: ${dp_max_value}")
    print(f"  • Greedy (0/1) found value: ${greedy_01_max_value:.0f}")
    print(f"  • Greedy (Fractional) found value: ${greedy_frac_value:.2f}")
    print(f"  • All algorithms executed successfully!")
    
    if MATPLOTLIB_AVAILABLE:
        print(f"\n📊 Visualizations saved to: report/knapsack_analysis_graphs.png")
    
    print("\n" + "=" * 70 + "\n")
    print("Thank you for using the Knapsack Problem Solver!")
    print("For questions, contact: basim.gul@example.com")
    print("\n" + "=" * 70 + "\n")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
