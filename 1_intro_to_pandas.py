#################################################################################
# Objective :
#################################################################################
## Gentle intro to pandas
#   Creating series from a python list
#   Handling of missing data
#   Pandas is internally numpy
#   Creating series from python dict
#################################################################################



#################################################################################
# Series :
# Cross b.w list and dictionary
# Items are stored in order like a list
# but they are indexed (starting from 0)
# and each data column has its own label depicting what the data is.
#################################################################################


import pandas as pd
import numpy as np


#################################################################################
print ('------------ Creating pandas series from a list ------------------')
# create series py passing a list of values
#################################################################################

animals = ['Tiger', 'Bear', 'Moose']
animals_series = pd.Series(animals)
print (animals_series)


# Pandas automatically infers the data type (Ex : int 64 as below)
nums_series = pd.Series([1,2,3,4,5])
print (nums_series)
#################################################################################



#################################################################################
##  PANDAS IS INTERNALLLY NUMPY
#################################################################################
# Pandas internally stores the values using a numpy array
# Significant speedup while processing data as compared to standard python list
#################################################################################




#################################################################################
#       HANDLING MISSING DATA  #
#################################################################################
# Handling missing data is different in python and pandas (thus numpy too)
# Python has None indicating no value
# Pandas has None for non-number types and Nan for missing number values.
# NaN is not = None instead its a numeric value and is treated differently than None.


if (np.nan == None):
    print ('np.nan = None')
else:
    print ('np.nan is not = None')                  # Executed


# Instead np.nan is not even equal to itself
if (np.nan == np.nan):
    print ('np.nan = np.nan')
else:
    print ('np.nan is not = np.nan')                #  Executed


# TO check whether a number is = np.nan we can't use == as mentioned above
# So we need to use np.isnan function
if ( np.isnan(np.nan) ):
    print ('Finally found a way to check if a number is nan or not.')


print ('------------ Series with strings and None ------------------')
animals_series = pd.Series(['Lion', 'Cat', None])
print (animals_series)
# < Inserts None as a value in the column
## OUTPUT >
# 0    Lion
# 1     Cat
# 2    None
# dtype: object


print ('------------ Series with numbers and None ------------------')
nums_series= pd.Series([10, 20, None])
print (nums_series)
# Prints NaN instead of None.
## OUTPUT >
# 0    10.0
# 1    20.0
# 2     NaN
# dtype: float64

#################################################################################





#################################################################################
#   Creating Series from dictionary
#################################################################################

# Pandas discard the auto indexing (from 0)
# and use the keys of the dictionary as index values.

print ('------------ Creating series from dictionary ------------------')
sports_dict = {'Archery' : 'Bhutan',
               'Golf' : 'Scotland',
               'Sumo' : 'Japan',
               'Cricket' : 'India'}

sports_series = pd.Series(sports_dict)
print (sports_series)



# TO access the indexes of a Series we use series.index
print(sports_series.index)




print ('------------ Passing index separately to create a Pandas series ------------------')
# We can also pass the index list separately
countries = ['India', 'America', 'Canada' ]
animals = ['Tiger', 'Bear', 'Moose']

ca = pd.Series(animals, index = countries)
print (ca)


# What if there are unequal number of elements in the index or the values list.
# ERROR
#################################################################################






#################################################################################
# CONCLUSION
#################################################################################

#   Creating series from a python list
    # Auto indexing is done starting from 0

#   Handling of missing data
    # np.nan is used instead of none for missing numbers and np.nan is not equal to None (it is similar though)

#   Pandas is internally numpy

#   use <series_variable>.index to get all the  index values

#   Creating series from python dict
    # Keys of the dict are used to form the index of pandas series ( instead of auto indexing )

#################################################################################
































