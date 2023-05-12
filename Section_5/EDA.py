import pandas as pd 
import numpy as np 

#Look at distribution of data to see if it is normally distributed across all classes
non_dummy = pd.read_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/Data/non_dummy.csv')

#Value count for class, 
#looks like no target class imbalance of this dataset in terms of target,
#might need to control for class of car in training and test dataset
non_dummy_maint_value_count = non_dummy['maint'].value_counts()
"""
vhigh    432
low      432
med      432
high     432
"""
non_dummy_doors_value_count = non_dummy['doors'].value_counts()
"""
5more    432
4        432
3        432
2        432
"""
non_dummy_persons_value_count = non_dummy['persons'].value_counts()
"""
4       576
more    576
2       576
"""
non_dummy_lug_count = non_dummy['lug_boot'].value_counts()
"""
small    576
med      576
big      576
Name: lug_boot, dtype: int64
"""
non_dummy_persons_safety_count = non_dummy['safety'].value_counts()
"""
low     576
med     576
high    576
"""
non_dummy_class_value_count = non_dummy['class'].value_counts()
"""
unacc    1210
acc       384
good       69
vgood      65
"""
non_dummy_buying_value_count = non_dummy['buying'].value_counts()
"""
vhigh    432
low      432
med      432
high     432
"""

print("Done")