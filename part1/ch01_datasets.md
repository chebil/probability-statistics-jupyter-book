# 1.1 Datasets

## What is a Dataset?

A **dataset** is a collection of descriptions of different instances of the same phenomenon.

### Structure

- **N**: Number of data items (rows)
- **d**: Number of dimensions/features (columns)
- Each item is a **d-tuple**: an ordered list of d elements

### Notation

- Dataset: {x}
- Individual item: x_i (where i = 1, 2, ..., N)
- Component of item: x_i^(j) (j-th feature of i-th item)

## Types of Data

### Numerical Data

**Continuous**: Can take any value in a range
- Height, weight, temperature
- Time measurements
- Sensor readings

**Discrete**: Specific, countable values
- Number of children
- Dice rolls
- Count of events

### Categorical Data

**Nominal**: Categories without order
- Gender (male, female, other)
- Color (red, blue, green)
- Type of fruit

**Ordinal**: Categories with meaningful order
- Education level (high school, bachelor's, master's, PhD)
- Rating scales (poor, fair, good, excellent)
- Size (small, medium, large)

## Example Datasets

### Bar Net Worth Dataset (Synthetic)

```python
import numpy as np
import pandas as pd

# Net worth of 10 people in a bar (in USD)
net_worth = pd.DataFrame({
    'Index': range(1, 11),
    'Net_Worth': [100360, 109770, 96860, 97860, 108930, 
                  124330, 101300, 112710, 106740, 120170]
})

print(net_worth)
print(f"\nMean net worth: ${net_worth['Net_Worth'].mean():,.2f}")
```

### Student Popularity Dataset

From Chase and Danner (1992): Students in grades 4-6 were surveyed about what makes other students popular.

**Features**:
- Gender (Boy/Girl)
- Grade (4, 5, or 6)
- Age
- Goal (Grades/Popular/Sports)
- Race
- Urban/Rural
- And more...

## Data Representation

### Vectors vs. Tuples

- **Vectors**: Can add, subtract, scale → most numerical data
- **Tuples**: Cannot always add/subtract → mixed or categorical data

### Working with Data

```python
import numpy as np

# Example: Height and weight data
data = np.array([
    [170, 68],  # person 1: height (cm), weight (kg)
    [180, 75],  # person 2
    [165, 62],  # person 3
])

# Access first person's data
person_1 = data[0]
print(f"Person 1: Height={person_1[0]}cm, Weight={person_1[1]}kg")

# Access all heights
heights = data[:, 0]
print(f"All heights: {heights}")
```

## Key Takeaways

1. Datasets are structured collections of observations
2. Understanding data types guides analysis choices
3. Proper notation helps communicate clearly
4. Real-world datasets often mix different data types

## Next Steps

Now that we understand what datasets are, let's learn how to visualize them effectively.

→ Continue to [1.2 Plotting Data](ch01_plotting.md)