"""
Dynamic Programming Solution for 0/1 Knapsack Problem
Applied to Airline Cargo Loading Optimization

Time Complexity: O(n * W) where n is number of items and W is capacity
Space Complexity: O(n * W) for the DP table

@author Basim Gul
@course Design and Analysis of Algorithms (CSC-321)
"""

import time


class DynamicProgrammingKnapsack:
    """
    Solver for 0/1 Knapsack problem using Dynamic Programming approach.
    """
    
    def __init__(self, items, weights, values, capacity):
        """
        Initialize the knapsack problem.
        
        Args:
            items: List of item names
            weights: List of item weights
            values: List of item values
            capacity: Maximum weight capacity
        """
        self.items = items
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.num_items = len(items)
        self.dp_table = [[0 for _ in range(capacity + 1)] for _ in range(self.num_items + 1)]
        self.selected_items = [False] * self.num_items
        
    def solve(self):
        """
        Solve the 0/1 knapsack problem using Dynamic Programming.
        
        Algorithm:
        1. Build DP table bottom-up
        2. For each item and weight:
           - If item weight > current capacity: carry forward previous value
           - Else: max(exclude item, include item)
        3. Backtrack to find selected items
        
        Returns:
            Maximum value achievable
        """
        start_time = time.time()
        
        print("\n" + "=" * 60)
        print("DYNAMIC PROGRAMMING APPROACH - 0/1 KNAPSACK")
        print("=" * 60 + "\n")
        
        # Build the DP table
        self._build_dp_table()
        
        # Display the complete DP table
        self._display_dp_table()
        
        # Backtrack to find selected items
        self._backtrack()
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Display results
        self._display_results(execution_time)
        
        return self.dp_table[self.num_items][self.capacity]
    
    def _build_dp_table(self):
        """
        Build the DP table using bottom-up approach.
        DP[i][w] = max(DP[i-1][w], DP[i-1][w-weight[i]] + value[i])
        """
        print("Building DP Table:")
        print("State Transition: DP[i][w] = max(DP[i-1][w], DP[i-1][w-weight[i]] + value[i])")
        print()
        
        # Initialize first row (no items) - already done with [0] initialization
        # Initialize first column (no capacity) - already done with [0] initialization
        
        # Fill the DP table
        for i in range(1, self.num_items + 1):
            for w in range(1, self.capacity + 1):
                item_index = i - 1
                item_weight = self.weights[item_index]
                item_value = self.values[item_index]
                
                # If current item weight exceeds capacity, can't include it
                if item_weight > w:
                    self.dp_table[i][w] = self.dp_table[i-1][w]
                else:
                    # Choose maximum between:
                    # 1. Not including current item: DP[i-1][w]
                    # 2. Including current item: DP[i-1][w-weight] + value
                    exclude_item = self.dp_table[i-1][w]
                    include_item = self.dp_table[i-1][w - item_weight] + item_value
                    self.dp_table[i][w] = max(exclude_item, include_item)
    
    def _display_dp_table(self):
        """Display the complete DP table with formatting."""
        print("\nComplete DP Table:")
        print("=" * 18)
        
        # Print header
        print(f"{'Item/Weight':<12} |", end="")
        for w in range(self.capacity + 1):
            print(f"{w:4} |", end="")
        print()
        
        # Print separator
        print("-" * 12 + "+" + "-" * (6 * (self.capacity + 1)))
        
        # Print rows
        for i in range(self.num_items + 1):
            if i == 0:
                row_label = "None"
            else:
                item_name = self.items[i-1]
                if len(item_name) > 11:
                    item_name = item_name[:8] + "..."
                row_label = item_name
            
            print(f"{row_label:<12} |", end="")
            
            for w in range(self.capacity + 1):
                print(f"{self.dp_table[i][w]:4} |", end="")
            print()
        print()
    
    def _backtrack(self):
        """Backtrack through the DP table to find which items were selected."""
        print("Backtracking to find selected items:")
        print("=" * 37)
        
        i = self.num_items
        w = self.capacity
        
        while i > 0 and w > 0:
            # If value comes from including current item
            if self.dp_table[i][w] != self.dp_table[i-1][w]:
                self.selected_items[i-1] = True
                print(f"Step: DP[{i}][{w}] ≠ DP[{i-1}][{w}] → Item {i} ({self.items[i-1]}) SELECTED")
                w -= self.weights[i-1]
            else:
                print(f"Step: DP[{i}][{w}] = DP[{i-1}][{w}] → Item {i} ({self.items[i-1]}) NOT selected")
            i -= 1
        print()
    
    def _display_results(self, execution_time):
        """Display the final results."""
        print("\n" + "=" * 60)
        print("DYNAMIC PROGRAMMING RESULTS")
        print("=" * 60)
        
        print("\nSelected Items:")
        print("-" * 15)
        total_weight = 0
        total_value = 0
        
        for i in range(self.num_items):
            if self.selected_items[i]:
                print(f"✓ {self.items[i]} - Weight: {self.weights[i]}kg, Value: ${self.values[i]}")
                total_weight += self.weights[i]
                total_value += self.values[i]
        
        print("\nSummary:")
        print("-" * 8)
        print(f"Total Weight Used: {total_weight} kg / {self.capacity} kg")
        print(f"Total Value Achieved: ${total_value}")
        print(f"Capacity Utilization: {(total_weight * 100.0) / self.capacity:.2f}%")
        print(f"Execution Time: {execution_time:.4f} ms")
        
        print("\nComplexity Analysis:")
        print("-" * 19)
        print(f"Time Complexity: O(n × W) = O({self.num_items} × {self.capacity}) = O({self.num_items * self.capacity})")
        print(f"Space Complexity: O(n × W) = O({self.num_items} × {self.capacity}) = O({self.num_items * self.capacity})")
        print("=" * 60 + "\n")
    
    def get_selected_items(self):
        """
        Get the selected items.
        
        Returns:
            List of booleans indicating which items were selected
        """
        return self.selected_items
    
    def get_max_value(self):
        """
        Get the maximum value.
        
        Returns:
            Maximum value achievable
        """
        return self.dp_table[self.num_items][self.capacity]
    
    def get_total_weight(self):
        """
        Get total weight of selected items.
        
        Returns:
            Total weight used
        """
        total_weight = 0
        for i in range(self.num_items):
            if self.selected_items[i]:
                total_weight += self.weights[i]
        return total_weight
