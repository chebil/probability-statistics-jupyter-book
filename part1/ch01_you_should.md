# 1.6 You Should

This section summarizes the key concepts, definitions, terms, facts, and skills you should master from Chapter 1.

## 1.6.1 Remember These Definitions

### Dataset
A collection of descriptions of different instances of the same phenomenon. Can be categorical (finite set of values) or continuous (any value in a range).

### Mean
The average value of a dataset:
$$\text{mean}(\{x\}) = \frac{1}{N} \sum_{i=1}^{N} x_i$$

### Standard Deviation
Measures the typical deviation from the mean:
$$\text{std}(\{x\}) = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \text{mean}(\{x\}))^2}$$

### Variance
The square of the standard deviation:
$$\text{var}(\{x\}) = \frac{1}{N} \sum_{i=1}^{N} (x_i - \text{mean}(\{x\}))^2$$

### Median
The middle value when data is sorted. For even-length datasets, average the two middle values.

### Percentile
The $k$-th percentile is the value such that $k\%$ of the data is less than or equal to that value.

### Quartiles
- **First quartile (Q1)**: 25th percentile
- **Second quartile (Q2)**: 50th percentile (median)
- **Third quartile (Q3)**: 75th percentile

### Interquartile Range (IQR)
The difference between the third and first quartiles:
$$\text{IQR} = Q3 - Q1$$

### Standard Coordinates (Z-scores)
Normalized data with mean 0 and standard deviation 1:
$$\tilde{x}_i = \frac{x_i - \text{mean}(\{x\})}{\text{std}(\{x\})}$$

### Normal Data
Data whose histogram, when plotted in standard coordinates with sufficient samples, approximates the standard normal curve:
$$y(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$

## 1.6.2 Remember These Terms

### Visualization Terms
- **Bar chart**: Visual representation of categorical data with bar heights proportional to counts
- **Histogram**: Visual representation of continuous data using intervals (bins)
- **Box plot**: Visual summary showing median, quartiles, and outliers
- **Conditional histogram**: Histogram of a subset of data based on some condition

### Distribution Properties
- **Unimodal**: Histogram with one peak
- **Bimodal**: Histogram with two peaks
- **Multimodal**: Histogram with multiple peaks
- **Skewed**: Asymmetric distribution
  - **Right-skewed** (positively skewed): Long right tail, mean > median
  - **Left-skewed** (negatively skewed): Long left tail, mean < median
- **Symmetric**: Distribution where left and right sides mirror each other

### Summary Statistics Terms
- **Location parameter**: Indicates where data lies on the number line (mean, median)
- **Scale parameter**: Indicates spread of data (standard deviation, IQR)
- **Outlier**: Data point unusually far from other observations
- **Five-number summary**: Minimum, Q1, Median, Q3, Maximum

## 1.6.3 Remember These Facts

### Properties of the Mean
1. Scaling data scales the mean: $\text{mean}(\{kx_i\}) = k \cdot \text{mean}(\{x_i\})$
2. Translating data translates the mean: $\text{mean}(\{x_i + c\}) = \text{mean}(\{x_i\}) + c$
3. Sum of deviations from mean is zero: $\sum_{i=1}^{N} (x_i - \text{mean}(\{x\})) = 0$
4. Mean minimizes sum of squared distances: $\text{argmin}_\mu \sum_i (x_i - \mu)^2 = \text{mean}(\{x\})$

### Properties of Standard Deviation
1. Translation doesn't change standard deviation: $\text{std}(\{x_i + c\}) = \text{std}(\{x_i\})$
2. Scaling data scales standard deviation: $\text{std}(\{kx_i\}) = |k| \cdot \text{std}(\{x_i\})$
3. At most $\frac{1}{k^2}$ of data lies $k$ or more standard deviations from the mean (Chebyshev's inequality)
4. At least one data point must be at least one standard deviation from the mean: $(\text{std}(\{x\}))^2 \leq \max_i (x_i - \text{mean}(\{x\}))^2$

### Properties of Variance
1. Translation doesn't change variance: $\text{var}(\{x + c\}) = \text{var}(\{x\})$
2. Scaling affects variance by square: $\text{var}(\{kx\}) = k^2 \cdot \text{var}(\{x\})$

### Properties of the Median
1. Translation translates the median: $\text{median}(\{x + c\}) = \text{median}(\{x\}) + c$
2. Scaling scales the median: $\text{median}(\{kx\}) = k \cdot \text{median}(\{x\})$
3. More robust to outliers than the mean

### Properties of Standard Coordinates
1. Mean of standardized data is 0
2. Standard deviation of standardized data is 1
3. Shape of distribution is preserved

### The 68-95-99.7 Rule (for Normal Data)
For normal data:
- About **68%** of data lies within 1 standard deviation of the mean
- About **95%** of data lies within 2 standard deviations of the mean
- About **99.7%** of data lies within 3 standard deviations of the mean

### Outlier Detection (IQR Method)
Data points are considered outliers if:
- $x < Q1 - 1.5 \times \text{IQR}$ (lower outliers)
- $x > Q3 + 1.5 \times \text{IQR}$ (upper outliers)

## 1.6.4 Be Able to

### Computational Skills

1. **Calculate descriptive statistics**:
   - Compute mean, median, mode
   - Calculate standard deviation and variance
   - Find quartiles and IQR
   - Identify outliers using the IQR method

2. **Create visualizations**:
   - Draw bar charts for categorical data
   - Create histograms with appropriate bin sizes
   - Make box plots
   - Construct conditional histograms

3. **Transform data**:
   - Convert data to standard coordinates
   - Scale and translate datasets
   - Normalize data for comparison

4. **Compare distributions**:
   - Use multiple visualization methods
   - Compare means and medians
   - Assess spread using standard deviation and IQR
   - Identify differences in shape and skewness

### Analytical Skills

1. **Interpret visualizations**:
   - Identify distribution shape (symmetric, skewed, multimodal)
   - Spot outliers visually
   - Compare multiple groups using box plots
   - Extract patterns from histograms

2. **Choose appropriate summaries**:
   - Decide when to use mean vs. median
   - Select standard deviation vs. IQR based on data properties
   - Determine appropriate visualization for data type

3. **Recognize data patterns**:
   - Identify whether data is approximately normal
   - Detect skewness and its direction
   - Recognize when outliers are present
   - Understand when standard assumptions apply

4. **Make data-driven conclusions**:
   - Use descriptive statistics to answer questions
   - Compare groups systematically
   - Identify what additional analysis is needed
   - Recognize limitations of descriptive methods

## Quick Reference Formulas

```python
import numpy as np

# Mean
mean = np.mean(data)

# Standard deviation
std = np.std(data)

# Variance
var = np.var(data)

# Median
median = np.median(data)

# Quartiles
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  # same as median
q3 = np.percentile(data, 75)

# IQR
iqr = q3 - q1

# Outlier bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Standard coordinates
z_scores = (data - mean) / std

# Identify outliers
outliers = data[(data < lower_bound) | (data > upper_bound)]
```

## Self-Check Questions

Test your understanding with these questions:

1. **When would you use median instead of mean?**
   - Answer: When data is skewed or has outliers

2. **What does it mean if standard deviation is 0?**
   - Answer: All data points are identical

3. **Can the median be outside the IQR?**
   - Answer: No, the median is always Q2, which is between Q1 and Q3

4. **If you multiply all data by 2, what happens to the standard deviation?**
   - Answer: It also multiplies by 2

5. **What percentage of normal data lies within 1.5 standard deviations of the mean?**
   - Answer: Approximately 86.6%

6. **Why is the IQR more robust than standard deviation?**
   - Answer: It's based on quartiles, which are less affected by extreme values

7. **What does a right-skewed histogram indicate?**
   - Answer: Most data is on the left with a long tail to the right; mean > median

8. **How do you detect outliers using the IQR method?**
   - Answer: Points below Q1 - 1.5×IQR or above Q3 + 1.5×IQR

## Common Mistakes to Avoid

1. ❌ **Using mean for heavily skewed data** → ✅ Use median instead
2. ❌ **Forgetting to check for outliers** → ✅ Always visualize and check
3. ❌ **Comparing histograms with different scales** → ✅ Use standard coordinates
4. ❌ **Using too many or too few histogram bins** → ✅ Experiment with bin sizes
5. ❌ **Ignoring the context of data** → ✅ Consider what the numbers represent
6. ❌ **Confusing variance with standard deviation** → ✅ Remember: variance = std²
7. ❌ **Assuming all data is normal** → ✅ Check the histogram shape first

## Practice Recommendations

To master this material:

1. **Work with real datasets**: Find datasets online and practice all techniques
2. **Create multiple visualizations**: For each dataset, make several different plots
3. **Compare your interpretations**: Check if statistical summaries match visual impressions
4. **Code from scratch**: Implement mean, median, std calculations without libraries
5. **Explain to others**: Teaching concepts helps solidify understanding

## What's Next?

In Chapter 2, we'll extend these ideas to **2D data** and learn about:
- Scatter plots
- Correlation
- Prediction using relationships between variables

The foundation you've built here with 1D data will make those concepts much easier to understand!

---

**Remember**: Descriptive statistics and visualization are always your first steps in data analysis. Never skip them—they reveal patterns, problems, and possibilities that no advanced technique can recover if you miss them at the start.