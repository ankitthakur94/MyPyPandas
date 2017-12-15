#################################################################################
# Objective :
#################################################################################
## Gentle intro to pandas series.
#   Creating series from a python list
#   Handling of missing data
#   Pandas is internally numpy
#   Creating series from python dict
#################################################################################



#################################################################################
# Series :
# Cross b.w list and dictionary
# Items are stored in order like a list
# but they are indexed (default index starts from 0)

#  Structure of the pandas Series can be visualized as : ( Row labels are also known as index / index-labels / index-values )

            # <row1-label>          <Data>
            # <row2-label>          <Data>
            # <row3-label>          <Data>
            #   ..                    ..
            # <rown-label>          <Data>
                 # BY default row-label starts from 0 and increments by +1.
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
## OUTPUT >
# 0    Tiger
# 1     Bear
# 2    Moose
# dtype: object


# Pandas automatically infers the data type (Ex : int 64 as below)
nums_series = pd.Series([1,2,3,4])
print (nums_series)
## OUTPUT >
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
#################################################################################



#################################################################################
#  CREATING PANDAS SERIES FROM PYTHON DICTIONARY
#################################################################################

# In this case Pandas discards the auto creation of row-labels (from 0)
# and instead use the keys of the dictionary as row-labels and values as values.

print ('------------ Creating series from dictionary ------------------')
sports_dict = {'Archery' : 'Bhutan',
               'Golf' : 'Scotland',
               'Sumo' : 'Japan',
               'Cricket' : 'India'}

sports_series = pd.Series(sports_dict)
print (sports_series)
## OUTPUT >
# Archery      Bhutan
# Cricket       India
# Golf       Scotland
# Sumo          Japan
# dtype: object


# To access the list indexes of a Series we use series.index
print(sports_series.index)
# Index(['Archery', 'Cricket', 'Golf', 'Sumo'], dtype='object')



print ('------------ Passing index separately as a list to create a Pandas series ------------------')
# We can also pass the index list separately
countries = ['India', 'America', 'Canada' ]
animals = ['Tiger', 'Bear', 'Moose']

ca = pd.Series(animals, index = countries)
print (ca)


# What if there are unequal number of elements in the index and the values list.
# ERROR
#################################################################################


#################################################################################
##  PANDAS IS INTERNALLY NUMPY
#################################################################################
# Pandas internally stores the values using a numpy array
# Significant speedup while processing data as compared to standard python list
#################################################################################




#################################################################################
#       HANDLING MISSING DATA  #
#################################################################################
# Handling missing data is different in python and pandas (thus numpy too)
# Python has 'None' indicating no value
# In case of missing values -> pandas has None for non-number types and Nan for missing number values.
# NaN != None instead its a numeric value and is treated differently than None.


if (np.nan == None):
    print ('np.nan = None')                         # Not Executed
else:
    print ('np.nan is not = None')                  # Executed


# Instead np.nan is not even equal to itself
if (np.nan == np.nan):
    print ('np.nan = np.nan')                       # Not Executed
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
# CONCLUSION
#################################################################################

#   Creating  pandas series :
    # Auto indexing (Automatic creation of row-labels)  is done starting from 0 if index list is not explicitly specified.
     # 1)  From python list
        # Ex : ser = pd.Series ( [list] )
            # Creates a pandas series like a numpy 1-D array with each value in the list being appended to a row.

    # 2) From python dict
        # Ex : ser pd.series ( dict )
            # Auto-indexing is turned off.
            # Keys of dict are used as indexes (row-labels) and values as values of series.

    # 3) Separately specifying index as list.
        # Ex : ser = pd.Series ( list1 , index = list2 )
            # Here list1 will comprise the values and list2 will be used as index.
            # list1 and list2 must be of the same length.

#   Handling of missing data
    # np.nan is used instead of none for missing numbers and np.nan is not equal to None (it is similar though)

#   Pandas is internally numpy

#   use <series_variable>.index to get all the  index values. ( Here index  values refer to row-labels )
#################################################################################
































