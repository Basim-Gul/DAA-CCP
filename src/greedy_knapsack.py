"""
Greedy Algorithm Solution for Knapsack Problem
Applied to Airline Cargo Loading Optimization

Time Complexity: O(n log n) for sorting + O(n) for selection = O(n log n)
Space Complexity: O(n) for storing item information

@author Basim Gul
@course Design and Analysis of Algorithms (CSC-321)
"""

import time


class Item:
    """Class to represent an item with its properties."""
    
    def __init__(self, name, weight, value, index):
        """
        Initialize an item.
        
        Args:
            name: Item name
            weight: Item weight
            value: Item value
            index: Original index in the input list
        """
        self.name = name
        self.weight = weight
        self.value = value
        self.ratio = value / weight  # value-to-weight ratio
        self.original_index = index
    
    def __lt__(self, other):
        """Compare items by ratio for sorting (descending order)."""
        return self.ratio > other.ratio


class GreedyKnapsack:
    """
    Solver for Knapsack problem using Greedy Algorithm approach.
    """
    
    def __init__(self, item_names, weights, values, capacity):
        """
        Initialize the knapsack problem.
        
        Args:
            item_names: List of item names
            weights: List of item weights
            values: List of item values
            capacity: Maximum weight capacity
        """
        self.capacity = capacity
        n = len(item_names)
        self.items = [Item(item_names[i], weights[i], values[i], i) for i in range(n)]
        self.selected_items_01 = [False] * n  # For 0/1 version
        self.fractional_amounts = [0.0] * n  # For fractional version
    
    def solve_01(self):
        """
        Solve using Greedy approach - 0/1 version.
        
        Algorithm:
        1. Calculate value-to-weight ratio for each item
        2. Sort items by ratio in descending order
        3. Select items greedily until capacity is full
        
        Returns:
            Total value achieved
        """
        start_time = time.time()
        
        print("\n" + "=" * 60)
        print("GREEDY ALGORITHM APPROACH - 0/1 VERSION")
        print("=" * 60 + "\n")
        
        # Calculate and display ratios
        self._display_ratios()
        
        # Sort items by value-to-weight ratio
        self._sort_items()
        
        # Select items greedily
        total_value = self._select_items_01()
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Display results
        self._display_results_01(total_value, execution_time)
        
        return total_value
    
    def solve_fractional(self):
        """
        Solve using Greedy approach - Fractional version.
        
        Returns:
            Total value achieved
        """
        start_time = time.time()
        
        print("\n" + "=" * 60)
        print("GREEDY ALGORITHM APPROACH - FRACTIONAL VERSION")
        print("=" * 60 + "\n")
        
        # Calculate and display ratios
        self._display_ratios()
        
        # Sort items by value-to-weight ratio
        self._sort_items()
        
        # Select items greedily with fractional allowance
        total_value = self._select_items_fractional()
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Display results
        self._display_results_fractional(total_value, execution_time)
        
        return total_value
    
    def _display_ratios(self):
        """Display value-to-weight ratios for all items."""
        print("Step 1: Calculate Value-to-Weight Ratios")
        print("=" * 42)
        print(f"{'Item':<20} | {'Weight':<8} | {'Value':<8} | {'Ratio':<10}")
        print("-" * 61)
        
        for item in self.items:
            print(f"{item.name:<20} | {item.weight:>6}kg | ${item.value:>6} | {item.ratio:>10.2f}")
        print()
    
    def _sort_items(self):
        """Sort items by value-to-weight ratio in descending order."""
        print("Step 2: Sort Items by Ratio (Descending)")
        print("=" * 41)
        
        # Sort items using Python's built-in sort
        self.items.sort()
        
        print("Sorted Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} (Ratio: {item.ratio:.2f})")
        print()
    
    def _select_items_01(self):
        """Select items greedily for 0/1 knapsack."""
        print("Step 3: Greedy Selection (0/1 - No Fractions)")
        print("=" * 46)
        
        remaining_capacity = self.capacity
        total_value = 0
        total_weight = 0
        
        print(f"Initial Capacity: {self.capacity} kg\n")
        
        for item in self.items:
            if item.weight <= remaining_capacity:
                # Select entire item
                self.selected_items_01[item.original_index] = True
                remaining_capacity -= item.weight
                total_value += item.value
                total_weight += item.weight
                
                print(f"✓ SELECTED: {item.name}")
                print(f"  Weight: {item.weight}kg, Value: ${item.value}, Ratio: {item.ratio:.2f}")
                print(f"  Running Total - Weight: {total_weight}kg, Value: ${total_value}")
                print(f"  Remaining Capacity: {remaining_capacity}kg\n")
            else:
                print(f"✗ REJECTED: {item.name}")
                print(f"  Weight: {item.weight}kg > Remaining Capacity: {remaining_capacity}kg\n")
        
        return total_value
    
    def _select_items_fractional(self):
        """Select items greedily for fractional knapsack."""
        print("Step 3: Greedy Selection (Fractional - Allowed)")
        print("=" * 48)
        
        remaining_capacity = float(self.capacity)
        total_value = 0.0
        total_weight = 0.0
        
        print(f"Initial Capacity: {self.capacity} kg\n")
        
        for item in self.items:
            if item.weight <= remaining_capacity:
                # Select entire item
                self.fractional_amounts[item.original_index] = 1.0
                remaining_capacity -= item.weight
                total_value += item.value
                total_weight += item.weight
                
                print(f"✓ SELECTED (Full): {item.name}")
                print(f"  Weight: {item.weight}kg (100%), Value: ${item.value}, Ratio: {item.ratio:.2f}")
                print(f"  Running Total - Weight: {total_weight:.2f}kg, Value: ${total_value:.2f}")
                print(f"  Remaining Capacity: {remaining_capacity:.2f}kg\n")
            elif remaining_capacity > 0:
                # Select fraction of item
                fraction = remaining_capacity / item.weight
                self.fractional_amounts[item.original_index] = fraction
                fractional_value = item.value * fraction
                
                total_value += fractional_value
                total_weight += remaining_capacity
                
                print(f"✓ SELECTED (Partial): {item.name}")
                print(f"  Weight: {remaining_capacity:.2f}kg ({fraction * 100:.1f}%), Value: ${fractional_value:.2f}, Ratio: {item.ratio:.2f}")
                print(f"  Running Total - Weight: {total_weight:.2f}kg, Value: ${total_value:.2f}")
                
                remaining_capacity = 0
                print(f"  Remaining Capacity: 0kg (FULL)\n")
                break
        
        return total_value
    
    def _display_results_01(self, total_value, execution_time):
        """Display results for 0/1 version."""
        print("\n" + "=" * 60)
        print("GREEDY ALGORITHM RESULTS (0/1 VERSION)")
        print("=" * 60)
        
        print("\nSelected Items:")
        print("-" * 15)
        total_weight = 0
        
        for item in self.items:
            if self.selected_items_01[item.original_index]:
                print(f"✓ {item.name} - Weight: {item.weight}kg, Value: ${item.value}")
                total_weight += item.weight
        
        print("\nSummary:")
        print("-" * 8)
        print(f"Total Weight Used: {total_weight} kg / {self.capacity} kg")
        print(f"Total Value Achieved: ${total_value:.0f}")
        print(f"Capacity Utilization: {(total_weight * 100.0) / self.capacity:.2f}%")
        print(f"Execution Time: {execution_time:.4f} ms")
        
        print("\nComplexity Analysis:")
        print("-" * 19)
        n = len(self.items)
        print(f"Time Complexity: O(n log n) for sorting + O(n) for selection")
        print(f"               = O({n} log {n}) + O({n})")
        print(f"Space Complexity: O(n) = O({n})")
        print("=" * 60 + "\n")
    
    def _display_results_fractional(self, total_value, execution_time):
        """Display results for fractional version."""
        print("\n" + "=" * 60)
        print("GREEDY ALGORITHM RESULTS (FRACTIONAL VERSION)")
        print("=" * 60)
        
        print("\nSelected Items:")
        print("-" * 15)
        total_weight = 0.0
        
        for item in self.items:
            fraction = self.fractional_amounts[item.original_index]
            if fraction > 0:
                if fraction == 1.0:
                    print(f"✓ {item.name} - Weight: {item.weight}kg (Full), Value: ${item.value}")
                    total_weight += item.weight
                else:
                    partial_weight = item.weight * fraction
                    partial_value = item.value * fraction
                    print(f"✓ {item.name} - Weight: {partial_weight:.2f}kg ({fraction * 100:.1f}%), Value: ${partial_value:.2f}")
                    total_weight += partial_weight
        
        print("\nSummary:")
        print("-" * 8)
        print(f"Total Weight Used: {total_weight:.2f} kg / {self.capacity} kg")
        print(f"Total Value Achieved: ${total_value:.2f}")
        print(f"Capacity Utilization: {(total_weight * 100.0) / self.capacity:.2f}%")
        print(f"Execution Time: {execution_time:.4f} ms")
        
        print("\nComplexity Analysis:")
        print("-" * 19)
        n = len(self.items)
        print(f"Time Complexity: O(n log n) for sorting + O(n) for selection")
        print(f"               = O({n} log {n}) + O({n})")
        print(f"Space Complexity: O(n) = O({n})")
        print("=" * 60 + "\n")
    
    def get_selected_items_01(self):
        """Get selected items for 0/1 version."""
        return self.selected_items_01
