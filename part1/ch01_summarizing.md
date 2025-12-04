# 1.3 Summarizing 1D Data

After visualizing data, we need numerical summaries. This section covers fundamental descriptive statistics.

## The Mean

The **mean** (average) is calculated as:

$$\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i$$

```python
import numpy as np

data = np.array([100, 105, 98, 102, 110])
mean = np.mean(data)
print(f"Mean: {mean}")
```

### Properties
- Sensitive to outliers
- Sum of deviations from mean equals zero
- Linear: mean(ax + b) = a·mean(x) + b

## Standard Deviation

**Standard deviation** measures spread:

$$\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})^2}$$

```python
std = np.std(data)
print(f"Standard Deviation: {std}")
```

## Variance

**Variance** is the square of standard deviation: $\sigma^2$

```python
variance = np.var(data)
print(f"Variance: {variance}")
```

## The Median

The **median** is the middle value when sorted:
- Robust to outliers
- Better than mean for skewed data

```python
median = np.median(data)
print(f"Median: {median}")
```

## Percentiles and Quartiles

- **Q1** (25th percentile): First quartile
- **Q2** (50th percentile): Median  
- **Q3** (75th percentile): Third quartile

```python
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)
print(f"Q1: {q1}, Q2: {q2}, Q3: {q3}")
```

## Interquartile Range (IQR)

**IQR = Q3 - Q1**

Useful for outlier detection:
- Outliers: values < Q1 - 1.5×IQR or > Q3 + 1.5×IQR

```python
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(f"Outlier bounds: [{lower_bound}, {upper_bound}]")
```

## Box Plots

Box plots visualize the five-number summary:
- Minimum
- Q1 
- Median
- Q3
- Maximum

```python
import matplotlib.pyplot as plt

plt.boxplot(data)
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()
```

## Standard Coordinates (Z-Scores)

Standardize data:

$$z_i = \frac{x_i - \bar{x}}{\sigma}$$

Properties:
- Mean = 0
- Std Dev = 1

```python
z_scores = (data - mean) / std
print(f"Z-scores: {z_scores}")
print(f"Mean of z-scores: {np.mean(z_scores):.10f}")
print(f"Std of z-scores: {np.std(z_scores):.10f}")
```

## Key Takeaways

1. **Mean vs Median**: Use median for skewed data
2. **Standard Deviation**: Measures typical deviation from mean
3. **IQR**: Robust measure of spread
4. **Z-scores**: Standardize for comparison
5. **Box plots**: Quick visual summary

## Practice

Try calculating these statistics for:
1. Test scores: [85, 92, 78, 90, 88, 95, 100]
2. Income data (skewed)
3. Datasets with outliers

## Next Section

→ Continue to [Chapter 2: Looking at Relationships](../part1/chapter02.md)