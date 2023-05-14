import pandas as pd 
import numpy as np 
from scipy.stats import chi2_contingency

#Look at distribution of data to see if it is normally distributed across all classes
non_dummy = pd.read_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/Data/non_dummy.csv',header=0)

non_dummy.drop(non_dummy.filter(regex="Unname"),axis=1, inplace=True)

#Value count for class, 
#looks like no target class imbalance of this dataset in terms of target,
#might need to control for class of car in training and test dataset

non_dummy_value_counts = non_dummy.apply(lambda x: x.value_counts()).T.stack()

#Explore Distribution Of other features within each class of cars
## Distribution of variables seem to be quite even across various classes so will also try stratified sampling for class variable to prepare training and testing data
unacc_class = non_dummy[non_dummy['class'] == 'unacc']
print(unacc_class['buying'].value_counts())
unacc_class_value_counts = unacc_class.apply(lambda x: x.value_counts()).T.stack()
acc_class = non_dummy[non_dummy['class'] == 'acc']
print(acc_class['buying'].value_counts())
acc_class_value_counts = acc_class.apply(lambda x: x.value_counts()).T.stack()
good_class = non_dummy[non_dummy['class'] == 'good']
print(good_class['buying'].value_counts())
good_class_value_counts = good_class.apply(lambda x: x.value_counts()).T.stack()
vgood_class = non_dummy[non_dummy['class'] == 'vgood']
print(vgood_class['buying'].value_counts())
vgood_class_value_counts = vgood_class.apply(lambda x: x.value_counts()).T.stack()
print("Done")


# Looking at association between variables 
# # Create an empty DataFrame to store the results
results_df = pd.DataFrame(columns=['Variable 1', 'Variable 2', 'Chi-square', 'P-value', 'Degrees of Freedom'])
column_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
# Loop through all pairs of variables
for i in range(len(column_names)):
    for j in range(i+1, len(column_names)):
        variable1 = column_names[i]
        variable2 = column_names[j]

        # Create a contingency table
        contingency_table = pd.crosstab(data[variable1], data[variable2])

        # Perform the chi-square test
        chi2, p, dof, expected = chi2_contingency(contingency_table)

        # Store the results in the DataFrame
        results_df = results_df.append({
            'Variable 1': variable1,
            'Variable 2': variable2,
            'Chi-square': chi2,
            'P-value': p,
            'Degrees of Freedom': dof
        }, ignore_index=True)

# Save the results to a CSV file
results_df.to_csv('association_results.csv', index=False)