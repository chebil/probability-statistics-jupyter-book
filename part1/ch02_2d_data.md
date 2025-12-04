# 2.1 Plotting 2D Data

## Scatter Plots

**Scatter plots** show relationships between two numerical variables.

```python
import numpy as np
import matplotlib.pyplot as plt

# Example: Height vs Weight
heights = np.array([165, 170, 175, 180, 185, 190])
weights = np.array([60, 65, 70, 75, 82, 88])

plt.figure(figsize=(8, 6))
plt.scatter(heights, weights, s=100, alpha=0.7)
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height vs Weight')
plt.grid(True, alpha=0.3)
plt.show()
```

### Interpreting Scatter Plots

**Positive Relationship**: Points trend upward
- As X increases, Y increases

**Negative Relationship**: Points trend downward  
- As X increases, Y decreases

**No Relationship**: Points scattered randomly

**Non-linear**: Curved pattern

## Categorical Data

For categorical variables, use bar charts or grouped visualizations.

```python
import pandas as pd

# Example: Goals by gender
data = pd.DataFrame({
    'Gender': ['Male', 'Male', 'Female', 'Female'],
    'Goal': ['Sports', 'Grades', 'Sports', 'Grades'],
    'Count': [60, 100, 57, 107]
})

data.pivot(index='Goal', columns='Gender', values='Count').plot(kind='bar')
plt.ylabel('Count')
plt.title('Student Goals by Gender')
plt.show()
```

## Series Plots

For time series or ordered data:

```python
# Temperature over time
days = np.arange(1, 8)
temps = np.array([72, 75, 78, 76, 74, 77, 80])

plt.plot(days, temps, marker='o', linewidth=2)
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.title('Weekly Temperature')
plt.grid(True, alpha=0.3)
plt.show()
```

## Multiple Groups

```python
# Compare multiple groups
male_heights = np.array([170, 175, 180, 185, 190])
male_weights = np.array([65, 70, 75, 80, 85])

female_heights = np.array([160, 165, 170, 175, 180])
female_weights = np.array([55, 60, 65, 70, 75])

plt.scatter(male_heights, male_weights, label='Male', alpha=0.7)
plt.scatter(female_heights, female_weights, label='Female', alpha=0.7)
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.title('Height vs Weight by Gender')
plt.show()
```

## Key Takeaways

1. Scatter plots reveal relationships
2. Look for patterns: linear, curved, clustered
3. Check for outliers
4. Use colors/markers for groups
5. Always label axes clearly

## Next

→ Continue to [2.2 Correlation](ch02_correlation.md)