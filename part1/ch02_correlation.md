# 2.2 Correlation

## What is Correlation?

**Correlation** quantifies the strength and direction of a linear relationship between two variables.

## Pearson Correlation Coefficient

The correlation coefficient $r$ ranges from -1 to +1:

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2} \sqrt{\sum (y_i - \bar{y})^2}}$$

Or equivalently, using standard coordinates:

$$r = \frac{1}{N} \sum z_x z_y$$

### Interpretation

- **r = +1**: Perfect positive correlation
- **r = -1**: Perfect negative correlation  
- **r = 0**: No linear correlation
- **|r| > 0.7**: Strong correlation
- **0.3 < |r| < 0.7**: Moderate correlation
- **|r| < 0.3**: Weak correlation

```python
import numpy as np
from scipy import stats

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 7, 8])

# Calculate correlation
r, p_value = stats.pearsonr(x, y)
print(f"Correlation: {r:.3f}")
print(f"P-value: {p_value:.4f}")
```

## Examples

### Strong Positive Correlation

```python
heights = np.array([160, 165, 170, 175, 180, 185])
weights = np.array([55, 62, 68, 75, 81, 88])

r = np.corrcoef(heights, weights)[0, 1]
print(f"Correlation: {r:.3f}")  # ~0.99
```

### Negative Correlation

```python
study_hours = np.array([8, 7, 6, 5, 4, 3, 2, 1])
errors = np.array([2, 3, 4, 5, 7, 9, 12, 15])

r = np.corrcoef(study_hours, errors)[0, 1]
print(f"Correlation: {r:.3f}")  # negative value
```

## Using Correlation for Prediction

Given correlation $r$, predict $y$ from $x$:

$$\hat{y} = \bar{y} + r \frac{\sigma_y}{\sigma_x}(x - \bar{x})$$

```python
def predict(x, x_data, y_data):
    r = np.corrcoef(x_data, y_data)[0, 1]
    
    x_mean = np.mean(x_data)
    y_mean = np.mean(y_data)
    x_std = np.std(x_data)
    y_std = np.std(y_data)
    
    y_pred = y_mean + r * (y_std / x_std) * (x - x_mean)
    return y_pred

# Predict weight for height=172cm
predicted_weight = predict(172, heights, weights)
print(f"Predicted weight: {predicted_weight:.1f} kg")
```

## Correlation Pitfalls

### 1. Correlation ≠ Causation

High correlation doesn't prove causation:
- Ice cream sales and drownings (both caused by summer)
- Number of Nicolas Cage films and swimming pool drownings

### 2. Non-linear Relationships

Correlation only measures *linear* relationships.

```python
# Parabolic relationship
x = np.linspace(-5, 5, 50)
y = x**2  # Perfect parabola

r = np.corrcoef(x, y)[0, 1]
print(f"Correlation: {r:.3f}")  # ~0, but clear relationship!
```

### 3. Outliers

Single outliers can dramatically affect correlation.

### 4. Simpson's Paradox

Correlation can reverse when data is grouped.

## Correlation Matrix

For multiple variables:

```python
import pandas as pd
import seaborn as sns

data = pd.DataFrame({
    'Height': [160, 165, 170, 175, 180],
    'Weight': [55, 62, 68, 75, 81],
    'Age': [20, 25, 30, 35, 40],
    'Shoe_Size': [7, 8, 9, 10, 11]
})

corr_matrix = data.corr()
print(corr_matrix)

# Visualize
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()
```

## Key Takeaways

1. Correlation measures linear relationship strength
2. Range: -1 to +1
3. Can use for prediction
4. **Correlation ≠ Causation**
5. Watch for non-linear patterns
6. Check scatter plots, don't just trust numbers

## Practice

1. Calculate correlation between:
   - Study hours and test scores
   - Temperature and heating bills
   - Age and reaction time

2. Create scatter plots and correlation matrices

3. Find examples of spurious correlations

## Next Part

→ Continue to [Part II: Probability](../part2/chapter03.md)