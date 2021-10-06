# Find insight in our data

# Dataframe is composed of:
	# Two columns: Group / Action
	# Group: Experiment / Control
	# Action: View / View and Click

# we use .value_counts() method

# For the group column 
df['group'].value_counts()

# For the action column
df['action'].value_counts()



