'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe
# ^ Completed this step within part1_etl.py


# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes


##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
import seaborn as sns
import matplotlib.pyplot as plt

def catplot_felony_rearrest(merged_df):
    """
    Create a categorical plot where the categories are charge type and 
    the y-axis is the prediction for felony rearrest.
    
    Args:
        merged_df (pd.DataFrame): Dataframe containing the merged data.
    """
    sns.catplot(data=merged_df, 
                x='has_felony_charge_x', 
                y='prediction_felony', 
                kind='bar')
    plt.title('Felony Rearrest Prediction by Charge Type')
    plt.xlabel('Charge Type')
    plt.ylabel('Prediction for Felony Rearrest')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest.png', bbox_inches='tight')
    plt.clf()

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# 
# In a print statement, answer the following question: What might explain the difference between the plots?
def catplot_nonfelony_rearrest(merged_df):
    """
    Create a categorical plot where the categories are charge type and 
    the y-axis is the prediction for non-felony rearrest.
    
    Args:
        merged_df (pd.DataFrame): Dataframe containing the merged data.
    """
    sns.catplot(data=merged_df, 
                x='has_felony_charge_x', 
                y='prediction_nonfelony', 
                kind='bar')
    plt.title('Non-Felony Rearrest Prediction by Charge Type')
    plt.xlabel('Charge Type')
    plt.ylabel('Prediction for Non-Felony Rearrest')
    plt.savefig('./data/part4_plots/catplot_nonfelony_rearrest.png', bbox_inches='tight')
    plt.clf()

    # Print statement to answer the question
    print("Difference Explanation: The difference between felony and non-felony predictions could be due to different factors influencing each prediction type, such as the severity of past offenses or the individual's criminal history.")


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?
def catplot_felony_rearrest_hue(merged_df):
    """
    Create a categorical plot where the categories are charge type and 
    the y-axis is the prediction for felony rearrest, hued by whether 
    the person actually got rearrested for a felony crime.
    
    Args:
        merged_df (pd.DataFrame): Dataframe containing the merged data.
    """
    
    sns.catplot(data=merged_df, 
                x='has_felony_charge_x', 
                y='prediction_felony', 
                hue='has_felony_charge_y', 
                kind='bar')
    plt.title('Felony Rearrest Prediction by Charge Type (Hued by Actual Rearrest)')
    plt.xlabel('Charge Type')
    plt.ylabel('Prediction for Felony Rearrest')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest_hue.png', bbox_inches='tight')
    plt.clf()

    # Print statement to answer the question
    print("Explanation: The higher predicted probability for arrestees with a current felony charge who were not rearrested for a felony may indicate that the model overestimates the risk for individuals with serious charges, or that other factors contribute to the likelihood of rearrest beyond the current charge type.")
