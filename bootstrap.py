# bootstrapping

# Create an empty list
differences = []

# Define a sample size - using .shape[]
# full dataset - 3575 rows
size = df.shape[0] 


# resample with replacement 10,000 times

for i in range(10000):
	
	# define the sample size
	sample=df.sample(size, replace=True)
	
	# define the dataframe
	control_df=sample.query('group=="control"')
	experiment_df=sample.query('group=="experiment"')

	# compute CTR based on control_df and experiment_df
	control_ctr=control_df.query('action=="view and click"').index.nunique()/control_df.index.nunique()
	experiment_ctr=experiment_df.query('action=="view and click"').index.nunique()/experiment_df.index.nunique()

	# append the diff between experiment CTR and control CTR to the list differences
	differences.append(experiment_ctr-control_ctr)

