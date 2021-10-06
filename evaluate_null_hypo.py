# Plot sampling distribution

# transform the list 'differences' into numpy array
differences=np.array(differences)

# plot a histogram 
plt.hist(differences)


# simulate the distribution under the null hypothesis
null_hypothesis=np.random.normal(0,differences.std(),differences.size)

# plot the null distribution
plt.hist(null_hypothesis)
plt.axvline(diff,c='red')

# compute the P-Value
(null_hypothesis>diff).mean()
