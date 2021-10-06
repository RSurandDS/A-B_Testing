# A/B Testing for an ad campaign

We will perform an A/B test to advise a company on whether they should go for the new ad or not.

Tools:

* Jupyter Notebook
* Libraries: Panda, Numpy, matplotlib



Steps:

* Load the dataset that we will work on.
* Find insights in our data and set up hypothesis testing
* Compute the difference in the click through rate
* Create sample distribution using bootstrapping
* Evaluate the null hypothesis and draw conclusions.


Hypothesis testing steps:

* Null hypothesis: the new ad did not generate more clicks than the old one (i.e new ad CTR is less than the old one)
* Alternative hypothesis: the new ad generates more click than the old one 
* Significance Level (alpha): probability of rejecting the null hypothesis when it's true
* P-Value calculation: probability of observing your statistic (or one more extreme in favor of the alternative) if the null hypothesis is true
