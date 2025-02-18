'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
# Import Necessary Packages
import os
import seaborn as sns
import matplotlib.pyplot as plt


# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def barplot_fta(pred_universe):
    sns.countplot(data=pred_universe,
                x='fta')                
    plt.title('Bar Plot of FTA')
    plt.savefig('./data/part3_plots/barplot_fta.png')
    plt.clf()  # Clears figure for the next plot

# 2. Hue the previous barplot by sex
def barplot_fta_hue_sex(pred_universe):
    # Create the directory if it doesn't exist
    output_dir = 'data/part3_plots'
    os.makedirs(output_dir, exist_ok=True)
    sns.countplot(data=pred_universe,
                x='fta',
                hue='sex')
    plt.title('Hue by Sex of FTA')
    plt.savefig('./data/part3_plots/barplot_fta_hue_sex.png')
    plt.clf() 


# 3. Plot a histogram of age_at_arrest
def histogram_age_at_arrest(pred_universe):

    sns.histplot(data=pred_universe, 
                x='age_at_arrest')
    plt.title(' Histogram of Age at Arrest ')
    plt.xlabel(' Age at Arrest')
    plt.ylabel('Frequency')
    plt.savefig('./data/part3_plots/histogram_age_at_arrest.png', bbox_inches = 'tight')
    plt.clf()  
# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histogram_age_groups(pred_universe):

    bins = [18, 21, 30, 40, 100]
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)
    plt.title('Histogram of Age at Arrest with Custom Bins')
    plt.xlabel('Age at Arrest')
    plt.ylabel('Frequency')
    plt.savefig('./data/part3_plots/histogram_age_groups.png', bbox_inches='tight')
    plt.clf()  # Clear the figure for the next plot