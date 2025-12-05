# Chapter 4: Random Variables and Expectations

We have machinery to describe experiments with random outcomes, but we mostly care about **numbers** that are random. It is straightforward to link a number to the outcome of an experiment. The result is a **random variable**, a useful new idea.

Random variables turn up everywhere:
- The outcome of rolling a die
- The number of heads in 10 coin flips
- The amount of money you win or lose on a bet
- The time until a server responds
- The number of errors in transmitted data

Now if you take the same bet repeatedly, you could wonder how much money will change hands in total, per bet. This yields a new and useful idea: the **expected value** of a random variable.

## What You'll Learn

In this chapter, you will learn:

1. **Random Variables** (Section 4.1)
   - Discrete and continuous random variables
   - Probability mass and density functions
   - Joint and conditional probability for random variables

2. **Expectations and Expected Values** (Section 4.2)
   - Definition and computation of expected values
   - Mean, variance, and covariance
   - Properties of expectations
   - Connection to descriptive statistics

3. **The Weak Law of Large Numbers** (Section 4.3)
   - IID samples
   - Markov's inequality
   - Chebyshev's inequality
   - Statement and proof of the weak law

4. **Applications** (Section 4.4)
   - Should you accept a bet?
   - Decision trees and expectations
   - Utility theory
   - Practical decision-making with expectations

## Why This Matters

Expected values have strong properties. When you know some expected values, you can:
- Bound various probabilities
- Make optimal decisions under uncertainty
- Understand long-run behavior of random processes
- Justify simulation and sampling methods

Particularly important to **computer scientists and gamblers** is the **weak law of large numbers**. This law tells us that if you repeat an experiment many times, the average of the results will be close to the expected value with high probability.

For computer scientists, this means:
- **Simulation is valid**: Running many trials approximates expected behavior
- **Sampling works**: A large enough sample reveals population properties
- **Randomized algorithms are reliable**: Average-case performance is predictable

## Prerequisites

Before starting this chapter, you should understand:
- Basic probability concepts from Chapter 3
- Sets, events, and probability rules
- Conditional probability
- Independence

## Chapter Structure

```{tableofcontents}
```

## Key Insight

```{admonition} The Central Idea
:class: tip
**Random variables** let us work with numbers instead of abstract outcomes. **Expectations** tell us what value to expect "on average" over many trials. The **weak law of large numbers** guarantees that this average converges to the expected value as the number of trials increases.
```

Let's begin by understanding what random variables are and how they work!