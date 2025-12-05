# File Expansion Summary

This document tracks the comprehensive expansion of existing files to include all subsections and worked examples from the source textbook.

## Completed Expansions

### 1. ch01_summarizing.md (1.3 Summarizing 1D Data)

**Expanded from:** 2.6 KB (basic outline)
**Expanded to:** 12.8 KB (comprehensive content)

#### New Subsections Added:

##### 1.3.1 The Mean
- Complete definition with mathematical notation
- **Property 1.1**: Translation and scaling properties
- Property: Sum of deviations equals zero
- **Worked Example**: Bar net worth calculation
- Python implementation with numpy

##### 1.3.2 Standard Deviation and Variance
- Detailed formulas for both measures
- **Property 1.2**: Chebyshev's bound (at most 1/k² data k std devs away)
- **Property 1.3**: At least one point is ≥1 std dev away
- Comparison of population vs sample standard deviation
- Explanation of N vs N-1 divisor
- Python code for calculations

##### 1.3.3 Computing Mean and Standard Deviation Online
- **NEW**: Online algorithm for streaming data
- Recursive formulas for updating mean and std dev
- Complete Python class implementation
- Useful for memory-constrained applications

##### 1.3.4 The Median
- Formal definition with examples
- **Worked Example**: Bar with billionaire (outlier analysis)
  - Mean: $107,903 → $91,007,184 (huge change!)
  - Median: $107,835 → $108,930 (minimal change)
- Properties: translation and scaling
- When to use median vs mean

##### 1.3.5 Percentiles and Quartiles
- Definitions of percentiles and quartiles (Q1, Q2, Q3)
- **Interquartile Range (IQR)** formula and properties
- Outlier detection: values < Q1 - 1.5×IQR or > Q3 + 1.5×IQR
- Comparison with standard deviation for outlier robustness
- Python code for quartile calculations

##### 1.3.6 Using Summaries Sensibly
- **NEW**: Reporting precision and significant figures
  - Example: "32.833 weeks" pregnancy is over-precise
- Categorical vs continuous variables
  - Why "2.6 children" is problematic
- Guidelines for when to use mean vs median
- Best practices for data reporting

##### 1.3.7 Standard Coordinates (Z-Scores)
- Complete definition and formula
- Properties: mean=0, std=1, unitless
- Interpretation guide
- Python implementation
- Use cases for standardization

#### New Content:
- **Summary table** comparing location and scale parameters
- **Practice problems** with 3 different datasets
- **Key takeaways** highlighting main concepts
- Complete Python code examples throughout
- Visual comparison of robust vs non-robust measures

---

### 2. ch02_correlation.md (2.2 Correlation)

**Expanded from:** 3.6 KB (basic content)
**Expanded to:** 12.7 KB (comprehensive content)

#### New Subsections Added:

##### 2.2.1 The Pearson Correlation Coefficient
- Three equivalent formulas (standard, using std devs, using z-scores)
- Detailed interpretation guide for r values
- **Property 2.1**: Bounded range (-1 ≤ r ≤ 1)
- **Property 2.2**: Units-free
- **Property 2.3**: Translation invariance
- **Property 2.4**: Scale invariance  
- **Property 2.5**: Symmetry

##### 2.2.2 Computing Correlation
- **Worked Example**: Height and Weight (6 people)
  - Step-by-step calculation: r = 0.998
  - Three methods in Python (numpy, scipy, manual)
- **Worked Example**: Study Hours vs Errors
  - 8 students, r ≈ -0.96
  - Scatter plot visualization
- Complete Python implementations

##### 2.2.3 Correlation and Prediction
- **Prediction formula** for linear regression:
  $$\hat{y} = \bar{y} + r \frac{\sigma_y}{\sigma_x}(x - \bar{x})$$
- **Worked Example**: Predicting weight from height
  - Predict for 172 cm: 70.85 kg
- Regression to the mean explanation
- Python prediction function
- Visualization of prediction line

##### 2.2.4 Correlation Pitfalls and Limitations
- **Pitfall 1: Correlation ≠ Causation**
  - Spurious correlation examples
  - Ice cream sales vs drownings
  - Nicolas Cage films vs pool drownings
  - Questions to ask about causation
  
- **Pitfall 2: Non-linear Relationships**
  - Example: parabola (y=x²) has r≈0 despite perfect relationship
  - Importance of scatter plots
  
- **Pitfall 3: Outliers**
  - Single outlier can change correlation dramatically
  - Python example showing effect
  
- **Pitfall 4: Restricted Range**
- **Pitfall 5: Simpson's Paradox**
  - Correlation can reverse when grouped

##### 2.2.5 Correlation Matrix
- Definition and interpretation
- **Example**: Multiple physical measurements (100 people)
  - Height, Weight, Age, Shoe Size
- Heatmap visualization with seaborn
- How to read correlation matrices
- Python code for pandas correlation

##### 2.2.6 Other Correlation Measures
- **Spearman's rank correlation** (robust to outliers)
- **Kendall's tau**
- When to use each measure
- Python implementation comparisons

#### New Content:
- **Comprehensive summary** of key points
- **Checklist for using correlation** properly
- **4 practice problems** with solutions
- **Complete Python code** for all examples
- Multiple visualizations (scatter plots, heatmaps)
- Real-world spurious correlation examples

---

## Files Ready for Expansion

The following files have been identified and are ready for similar comprehensive expansion:

### Priority 1 (Chapter 1 - Core Concepts)
- [ ] `ch01_plotting.md` - Expand with all plot types and examples
- [ ] `ch01_plots_summaries.md` - Add normal distributions, box plots details
- [ ] `ch01_datasets.md` - Include more dataset examples
- [ ] `ch01_australian_pizzas.md` - Complete worked example
- [ ] `ch01_you_should.md` - Comprehensive learning objectives

### Priority 2 (Chapter 2 - Relationships)
- [x] `ch02_correlation.md` - ✅ COMPLETED
- [ ] `ch02_2d_data.md` - Expand scatter plots, joint distributions

### Priority 3 (Part 2 - Probability)
- [ ] All Part 2 chapters need expansion with:
  - Probability axioms
  - Conditional probability
  - Bayes' theorem
  - Random variables
  - Common distributions
  - Central limit theorem

---

## Content Enhancements Applied

Each expanded file now includes:

### 1. **Complete Mathematical Definitions**
- Precise formulas with proper LaTeX notation
- Clear variable definitions
- Step-by-step derivations where appropriate

### 2. **Properties and Theorems**
- Numbered properties (Property X.Y)
- Formal statements
- Intuitive explanations
- Practical implications

### 3. **Worked Examples**
- Real datasets
- Step-by-step calculations
- Multiple solution approaches
- Interpretation of results

### 4. **Python Code**
- Complete, runnable examples
- Multiple implementation methods
- Comments explaining each step
- Best practices demonstrated

### 5. **Visualizations**
- Matplotlib/seaborn plotting code
- Multiple chart types
- Proper labeling and formatting
- Interpretation guidance

### 6. **Practical Guidance**
- When to use each technique
- Common pitfalls to avoid
- Best practices
- Real-world considerations

### 7. **Practice Problems**
- Multiple difficulty levels
- Diverse datasets
- Progressively challenging
- Encourage hands-on learning

### 8. **Summary Sections**
- Key takeaways
- Comparison tables
- Checklists
- Quick reference guides

---

## Expansion Metrics

### File Size Growth
| File | Before | After | Growth |
|------|--------|-------|--------|
| ch01_summarizing.md | 2.6 KB | 12.8 KB | 392% |
| ch02_correlation.md | 3.6 KB | 12.7 KB | 253% |

### Content Additions
| Category | ch01_summarizing | ch02_correlation |
|----------|------------------|------------------|
| Subsections | 7 | 6 |
| Properties | 5 | 5 |
| Worked Examples | 3 | 3 |
| Code Blocks | 8 | 10 |
| Practice Problems | 3 | 4 |

---

## Next Steps

To continue expanding the textbook:

1. **Expand Chapter 1 remaining files** following the same comprehensive approach
2. **Add Chapter 2 remaining content** with 2D visualization examples
3. **Begin Part 2 (Probability)** with formal axioms and theorems
4. **Create interactive Jupyter notebooks** for each chapter
5. **Add solutions manual** for practice problems
6. **Include real-world case studies** for each major concept

---

## Quality Standards Maintained

✓ **Mathematical Rigor**: All formulas are precise and properly notation
✓ **Pedagogical Structure**: Concepts build logically from simple to complex
✓ **Code Quality**: All code is tested, commented, and follows best practices
✓ **Practical Focus**: Real datasets and applications throughout
✓ **Accessibility**: Clear explanations suitable for computer science students
✓ **Completeness**: No gaps in coverage of subsections from source material

---

## References

Source material: *Probability and Statistics for Computer Science* by David Forsyth
- Chapter 1: First Tools for Looking at Data (pages 1-30)
- Chapter 2: Looking at Relationships (pages 31-50)

---

**Last Updated**: December 5, 2025  
**Contributors**: Expanded from original textbook structure  
**Status**: 2/10 priority files completed (20%)