###############################################################
# Objective :
# Explore basics of data frame.
###############################################################

import pandas as pd
import numpy as np

###############################################################
## Structure of DataFrame
###############################################################

# indices of df need not be unique, duplicate indexes are allowed.
# Columns in df always have a label

# <index>  <series_1> <series_2>

# Ex :
#        Animals         Owners
# 0       Dog             P1
# 1       Bear            P2
# 2       Cat             P3
# 3       Moose           P4

# Axis :
    # Axis 0 : Rows V
    # Axis 1 : Columns >

# .columns ()
    # Animals , Owners

# index : 0,1,2,3

# iloc and loc
    # df.iloc(2) -> Returns the row 3 data.
    # df['Owners'] -> Returns the Owners column
    # df.iloc(3)["Animals"] -> Moose
    # df.loc['string'] -> will returns the df snippet which have index = 'string'
###############################################################





###############################################################
# Creating data frame :
###############################################################
    # 1) Using group of series, where each series represents a column
        # Each index of a series will convert to a column of the data frame.
        # So values in each series will be each row of df.
        # Imagine series as flat (horizontal) with each new series being added as a new row in df.
        # If there is index mismatch in series, NaN is added to the series (rows in df) having no data for that index.
    # 2) Using group of dictionary, where each value column of a dict represents a column in df
###############################################################




###############################################################
# Ex : Creating df from 3 series
###############################################################
# We will have 3 columns : Name, Item, Cost

s1 = pd.Series ({'Name' : 'Ankit' ,
                 'Item' : 'Milk',
                 'Cost' : 100})
print(s1)
## OUTPUT >
# Cost      100
# Item     Milk
# Name    Ankit

s2 = pd.Series ({'Name' : 'Karan' ,
                 'Item' : 'Chocolate',
                 'Cost' : 10})

s3 = pd.Series ({'Name' : 'Madhur' ,
                 'Item' : 'Eggs',
                 'Cost' : 50})

print ('--------- Creating a df from pandas.Series ---------- ')
df_from_series = pd.DataFrame([s1, s2, s3], index = ['Store1', 'Store2', 'Store1'])
print(df_from_series)
## OUTPUT >
#        Cost       Item    Name
# Store1  100       Milk   Ankit
# Store2   10  Chocolate   Karan
# Store1   50       Eggs  Madhur
###############################################################





###############################################################
## Auto indexing
###############################################################
# IF no index was given then auto indexing (from 0) would have invoked.
#df_from_series = pd.DataFrame([s1, s2, s3] )
###############################################################



###############################################################
## Inconsistent indexes in series
###############################################################
# In the above example all the series (s1, s2, s3) have the same  index names ('Name', 'Item' , 'Cost')
# As discussed each index name of the series will be 1 column in data frame.
# What if series had different indexes.
    # Say s2 had another index as shown :

s2 = pd.Series ({'Name' : 'Karan' ,
                 'Item' : 'Chocolate',
                 'Cost' : 10,
                 'Qty' : 50})


print ('--------- Handling unequal indexes in series used to form the df ---------- ')
df_from_series = pd.DataFrame([s1, s2, s3], index = ['Store1', 'Store2', 'Store1'])
print(df_from_series)

# In case of series-index mismatch, each index of each series will be a new column name in df.
# For the series having values corresponding to that index, values will be added to the column in df
# For the series not having that index, NaN will be added for that series corresponding to the column in df

## OUTPUT >
#         Cost       Item    Name   Qty
# Store1   100       Milk   Ankit   NaN
# Store2    10  Chocolate   Karan  50.0
# Store1    50       Eggs  Madhur   NaN
###############################################################






###############################################################
# Using iloc and loc
###############################################################
# iloc and loc work similar as in pandas-Series.

# df.loc['index_label_string']
    # returns the df snippet where index of df  = 'index_string'
    # return type : DataFrame
    # Detailed explanation below

# df.iloc[integer / slice / list_of_integer]
    # returns the corresponding rows as df snippet
    # return DataFrame

# df['column_name']
    # returns the df index and column as a whole.
    # Return type : pandas-Series


print ('-- df.loc["Store1"] : -- ')
print(df_from_series.loc['Store1'])
print(type(df_from_series.loc['Store1']))

print ('-- df.iloc[0:2] : -- ')
print(df_from_series.iloc[0:2])
print(type(df_from_series.iloc[0:2]))

print ('-- df["Item"] : -- ')
print(df_from_series['Item'])
print(type(df_from_series['Item']))

# Alternate way to get the above data using loc ->
print (df_from_series.loc[:, 'Item'])

###############################################################




###############################################################
# df.loc in more details
###############################################################
# it works on labels and here labels refer to the index-labels (index-names) and column labels (column-names)
# So it can take 2 ranges separated by , ( df.loc [<range1> , <range2>] )
    # here range can be a single value or a list of values or a slice of values of the form : [start : stop : step]
    # Note that <range1> is mandatory and <range2> is optional and it is recommended to write both for clarity.
        # Can mention just ':' for row / column to be taken completely


    # <range1> : Should mention the range of index-labels
        # Exs of index-labels :
            # 1.) df.loc ['Store1']                              # Single index-label
                    # returns df snippet with Store1 as index label
            # 2.) df.loc [ ['Store1', 'Store2'] ]                # List of index-labels
                    # returns df snippet with Store 1 or Store 2 as index label

    # <range2> : Should mention the range of column-labels.
        # Ex of column-labels :
            # 1.) df.loc ['Store1', 'Cost']                     # Single row and single column label
                    # returns a pandas series with Store1 as index label and retunrs only cost column
            # 2.) df.loc ['Store1', ['Cost' , 'Name'] ]         # Single row and list of column label
                    # returns df snippet with Store1 as index label and returns Cost and Name colums
            # 3.) df.loc [ ['Store1', 'Store2'] , 'Name] ]      # List of  row and single coumn label
                    # returns pandas series.
            # 4.) df.loc [ ['Store1', 'Store2' ]  , ['Name', 'Cost' ] ] # List of  row and column label
                    # returns a pandas df


# Since loc / iloc / [] return a pandas data frame / series, the operations can be chained.
# but it comes at a cost
# It returns a copy of df, not a view of df and that too with no guarantee.
# So avoid chained indexing.
###############################################################





###############################################################
### COPY A DATAFRAME
# df_copy = df.copy()
###############################################################





###############################################################
## DROPPING DATA in Data frame
###############################################################
    # df.drop ( <index label / column label> )
    # Delete a particular row / column in data frame.
    # By default returns a copy and does not modify the original df.
# optional parameters :
    # inplace : defualt False
    # axis : default 0. i.e row . Can change it to 1 for column labels

print (' -- Dropping Qty column -- ')
df2 = df_from_series.drop('Qty', axis=1)
print (df2)
###############################################################






###############################################################
## ASSIGNING A NEW COLUMN to DF
###############################################################
    # Is as simple as assigning
df_from_series['New Column'] = None
df_from_series['New Column2'] = [10, 20, 30]

print (' -- Creating new columns -- ')
print (df_from_series)
## OUTPUT >
#         Cost       Item    Name   Qty New Column  New Column2
# Store1   100       Milk   Ankit   NaN       None           10
# Store2    10  Chocolate   Karan  50.0       None           20
# Store1    50       Eggs  Madhur   NaN       None           30
###############################################################






###############################################################
## MODIFYING ALL VALUES IN A PARTICULAR COLUMN IN A DF
###############################################################
df_from_series['Cost'] *= 0.8           # Will apply a 20% discount on all cost.
print (' -- Modifying the Cost column -- ')
print (df_from_series)
###############################################################


