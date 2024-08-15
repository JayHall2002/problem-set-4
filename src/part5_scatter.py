'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
import seaborn as sns
import matplotlib.pyplot as plt

def scatterplot_felony_vs_nonfelony(merged_df):
    """
    Creates a scatter plot where the x-axis is the prediction for felony 
    and the y-axis is the prediction for nonfelony, hued by whether 
    the current charge is a felony.
    
    Args:
        merged_df (pd.DataFrame): Dataframe containing the merged data.
    """
    sns.lmplot(data=merged_df, 
               x='prediction_felony', 
               y='prediction_nonfelony', 
               hue='has_felony_charge_x', 
               fit_reg=False)
    plt.title('Felony vs. Non-Felony Predictions')
    plt.xlabel('Prediction for Felony')
    plt.ylabel('Prediction for Non-Felony')
    plt.savefig('./data/part5_plots/scatterplot_felony_vs_nonfelony.png', bbox_inches='tight')
    plt.clf()

    # Print statement to answer the question
    print("Observation: The group of dots on the right side of the plot likely represents individuals with high felony predictions. This could indicate a strong likelihood of committing a felony, distinguishing them from those with lower predictions.")


# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def scatterplot_felony_rearrest_vs_actual(merged_df):
    """
    Creates a scatter plot where the x-axis is the prediction for felony 
    rearrest and the y-axis is whether someone was actually rearrested.
    
    Args:
        merged_df (pd.DataFrame): Dataframe containing the merged data.
    """
    sns.lmplot(data=merged_df, 
               x='prediction_felony', 
               y='has_felony_charge_y', 
               fit_reg=False)
    plt.title('Felony Rearrest Prediction vs. Actual Rearrest')
    plt.xlabel('Prediction for Felony Rearrest')
    plt.ylabel('Actual Felony Rearrest')
    plt.savefig('./data/part5_plots/scatterplot_felony_rearrest_vs_actual.png', bbox_inches='tight')
    plt.clf()

    # Print statement to answer the question
    print("Model Calibration: If the model is well-calibrated, we would expect the points to form a diagonal line from the bottom left to the top right. Any significant deviation from this pattern could indicate that the model's predictions are not well-calibrated.")
