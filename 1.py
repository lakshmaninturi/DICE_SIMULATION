# dice_roll_simulation.py
# This script simulates rolling two six-sided dice 10,000 times,
# calculates the percentage of rolls for each possible sum (2 to 12),
# and visualizes the results using a bar chart.

import random
import numpy as np
import matplotlib.pyplot as plt
# Although the core simulation doesn't require scipy, it's a powerful library for
# more advanced statistical analysis. For a simple simulation like this,
# we can use numpy and matplotlib to handle the data and plotting.
# If we were to perform a more in-depth statistical test, like a chi-squared test
# to see if our results match the theoretical probabilities, we might use
# scipy.stats.chisquare.

def simulate_dice_rolls(num_rolls=10000):
    """
    Simulates rolling two dice a given number of times and
    returns the counts for each sum from 2 to 12.

    Args:
        num_rolls (int): The number of times to simulate the dice rolls.

    Returns:
        A dictionary with sums (2-12) as keys and their roll counts as values.
    """
    roll_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        # Simulate rolling two six-sided dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total_sum = die1 + die2
        roll_counts[total_sum] += 1
        
    return roll_counts

def calculate_percentages(roll_counts, total_rolls):
    """
    Calculates the percentage for each sum based on the counts.

    Args:
        roll_counts (dict): A dictionary of roll counts.
        total_rolls (int): The total number of rolls.

    Returns:
        A dictionary with sums (2-12) as keys and their percentages as values.
    """
    percentages = {}
    for total_sum, count in roll_counts.items():
        percentage = (count / total_rolls) * 100
        percentages[total_sum] = percentage
    return percentages

def visualize_results(percentages, num_rolls):
    """
    Creates and displays a bar chart of the dice roll percentages.

    Args:
        percentages (dict): A dictionary of percentages for each sum.
        num_rolls (int): The total number of rolls, used for the title.
    """
    # Sort the sums to ensure the graph is in order
    sums = sorted(percentages.keys())
    values = [percentages[s] for s in sums]
    
    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(sums, values, color='skyblue')
    
    # Add labels and title
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Percentage of Rolls')
    plt.title(f'Simulated Dice Roll Probabilities ({num_rolls} Rolls)')
    plt.xticks(sums)
    
    # Add text labels on top of each bar
    for i, v in enumerate(values):
        plt.text(sums[i], v + 0.5, f'{v:.2f}%', ha='center')
        
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    """
    Main function to run the dice roll simulation, calculate percentages, and
    display the results with a graph.
    """
    NUM_ROLLS = 10000
    
    print(f"Simulating {NUM_ROLLS} dice rolls...")
    
    # 1. Simulate the dice rolls
    roll_counts = simulate_dice_rolls(NUM_ROLLS)
    
    # 2. Calculate the percentages
    percentages = calculate_percentages(roll_counts, NUM_ROLLS)
    
    print("\n--- Simulation Results ---")
    for total_sum, percentage in sorted(percentages.items()):
        print(f"Roll {total_sum:2d}: {percentage:.2f}%")
        
    # 3. Visualize the results
    visualize_results(percentages, NUM_ROLLS)

if __name__ == "__main__":
    main()
