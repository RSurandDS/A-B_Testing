# CTR CALCULATION

# CONTROL GROUP

# Get dataframe with all observations from control group
control_df = df.query['group=="control"']

# Compute CTR for control group 
# We divide the number of 'view and click' elements in 'control_df' 
# by the total number of elements in the 'control_df'
control_ctr=control_df.query('action=="view and click"').index.nunique()/control_df.index.nunique()

# display the CTR
control_ctr


# EXPERIMENT GROUP
# get dataframe with all observations from experiment group
experiment_df=df.query['group=="experiment"']

# Compute CTR for experiment group
experiment_ctr=experiment_df.query('action=="view and click"').index.nunique()/experiment_df.index.nunique()

# display the CTR
experiment_ctr


# --------------------------
# COMPUTE the difference in the CTR
diff = experiment_ctr-control_ctr