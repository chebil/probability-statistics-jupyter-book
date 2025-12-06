# Chapter 9: Inferring Probability Models from Data

This chapter covers methods for **estimating parameters** of probability models from data. We explore both **frequentist** (Maximum Likelihood) and **Bayesian** approaches.

## Learning Objectives

After completing this chapter, you will be able to:

- Understand the likelihood function
- Compute maximum likelihood estimates (MLE)
- Apply Bayesian inference with prior and posterior distributions
- Use conjugate priors for analytical solutions
- Compute maximum a posteriori (MAP) estimates
- Compare frequentist and Bayesian approaches
- Apply these methods to common distributions

## Chapter Outline

1. **Maximum Likelihood Estimation** - The frequentist approach
2. **Bayesian Inference Basics** - Prior, likelihood, and posterior
3. **Conjugate Priors** - Analytical Bayesian inference
4. **Applications** - Real-world examples

## Why This Matters

Parameter estimation is fundamental to:
- **Machine Learning**: Training models on data
- **Statistics**: Fitting distributions to observations  
- **Science**: Estimating physical constants from experiments
- **Engineering**: System identification and calibration
- **Finance**: Risk modeling and option pricing

## Two Philosophies

### Frequentist (MLE)
> "Parameters are fixed but unknown. Data is random. Find the parameter value that makes the observed data most likely."

### Bayesian
> "Parameters are uncertain (random). Update beliefs about parameters using data via Bayes' theorem."

Let's explore both!