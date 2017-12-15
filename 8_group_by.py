#######################################################
# Objective :
#######################################################
# Learn how to use groupby('col_name')
# Split -> Apply -> Combine
# use of agg (['f1' , 'f2' ])
#######################################################



import pandas as pd
import numpy as np



states_df = pd.read_csv('cities_and_temp.csv', encoding="ISO-8859-1" , index_col=None)
print (states_df)

## INTENTION :
# In the states_df, city is a column name and multiple rows have the data for a single city.
# Group data per city and then run analytics per city
# use pandas group_by


print ( ' ---- Calling group by ----- ')
###################################################
## Calling group by
###################################################
g = states_df.groupby('city')
print (g)
# groupby ('column_name')  -> actually finds the uniquified values of the entries in that col and splits the orig df into that many df's , each having data for a particualr value.
# The above line creates a groupby object of pandas.
# 'g' is like a dict where keys are the uniquified city names and values are the data frame snippets of complete data frame for the given city.
    # <delhi> : <dataframe_for_delhi>
    # <mumbai> : <df_for_mumbai>
    # <chennai : <df_for_chennai>
        # Note that this is just a visualization purpose.


###################################################
# Now we can iterate on this dict-like structure
###################################################
for city, city_df in g:
    print (' --> Data for city : ', city)
    print (city_df)


print ( ' ----- Get the data frame for a particular group : mumbai ------ ')
###################################################
# get the data frame for a particular group
###################################################
    # Lets get the mumbai df.
mumbai_df = g.get_group('mumbai')
print (mumbai_df)


###################################################
# SPLIT -> APPLY -> COMBINE
###################################################
# Split : by group_by ('row_name')
# apply : apply a function like min / max / mean / count etc. which provides the max (say) for a particular column (or for every column as above) for every group.
# combine : to get a final df as a result.
###################################################

print ( ' --- Describe  function op -> --- ')
###################################################
# use .describe to print all the statistics for all the groups
###################################################
print (g.describe())
###################################################


###################################################
## Applying a combining function on a particular column for every group.
###################################################
print (' --- Max temp group wise --- ')
max_temp_df = states_df.groupby('city').temp.max()
print (max_temp_df)

print ( '  ---- Mean windspeed goup wise --- ')
mean_ws = states_df.groupby('city')['windspeed'].mean()
print (mean_ws)
###################################################


print ( ' ---- Applying multiple aggregation functions on temprature group wise ---- ')
###################################################
## Applying multiple combining functions on a particular column for every group
###################################################
agg_df_1 = states_df.groupby('city').temp.agg(['count', 'min', 'max' , 'mean'])
print(agg_df_1)
###################################################


print ( ' ----  Applying mean() to all columns group wise ----  ')
###################################################
## Applying a combining function to all the columns (again the result is printed for every group)
###################################################
## Applying combining functions to all columns (without giving any particular column)
all_col_df = states_df.groupby('city').mean()
print (all_col_df)
###################################################


print ( ' --- Applying mean() and max() functions to all the cols group wise --- ')
###################################################
## Applying multiple combining functions to all the cols
###################################################
print (states_df.groupby('city').agg(['mean', 'max']))
###################################################




## Conclusion

# groupby ()
