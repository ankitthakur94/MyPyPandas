#####################################################################################
# Objective :
#####################################################################################
# Changing view will change the original df also.
# df.copy() to create a copy of the df.
# reading a csv_file
# renaming the column names / index names in a df.
#####################################################################################



#####################################################################################
#  Pandas toolkit gives us views of the data frame which helps us save runtime and memory.
# But changing a view can also change the original data frame, a thing we must be aware of.
#####################################################################################

import pandas as pd
import numpy as np


#####################################################################################
## Demonstration of original data frame being modified when its clip is modified.
#####################################################################################

s1 = pd.Series ({'Name' : 'Ankit' ,
                 'Item' : 'Milk',
                 'Cost' : 100})

s2 = pd.Series ({'Name' : 'Karan' ,
                 'Item' : 'Chocolate',
                 'Cost' : 10})

s3 = pd.Series ({'Name' : 'Madhur' ,
                 'Item' : 'Eggs',
                 'Cost' : 50})

df_from_series = pd.DataFrame([s1, s2, s3], index = ['Store1', 'Store2', 'Store1'])

print (' -- Original df -- ')
print(df_from_series)

Costs = df_from_series['Cost']                      # get a view of original df using []
Costs *= 0.8                                        # Changing a view will also change the original df

print (' -- Original df after modifying the view -- ')
print(df_from_series)
#####################################################################################




#####################################################################################
## TO AVOID THIS
# If you do not want to change the original df make a copy and do modifications on that copy
# df_copy = df.copy ()
#####################################################################################



#df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
#medals_df = df[1]
#medals_df.to_csv('countries_and_medals_orig.csv', header=False, index=False)



#####################################################################################
# READING a CSV FILE and setting column headers and df index
#####################################################################################
medals_df = pd.read_csv('countries_and_medals_orig.csv', encoding="ISO-8859-1", index_col=0 , header=0  )
# header = 0 : Use row-0 as labels for columns
# index_col = 0 : Use column 0 as index for rows.

print (medals_df.head())
#####################################################################################




#####################################################################################
# NO REPEATING COLUMN HEADERS in a DATAFRAME
#####################################################################################
# While reading the above csv file, we use 1st row was column labels.
# THe original csv file has repeating entries in 1st row
# (01 ! stands for Gold medal and comes 3 times) similar is the case with 02 ! and 03 !
# Pandas does not like repeating column headers and appends .1 , .2 for the consecutive repeating entry
# SO 3 times 01 ! ( 01 !  01 !  01 ! )  becomes -> ( 01 !  01 !.1  01 !.2)
#####################################################################################




#####################################################################################
# To get the columns list :
#####################################################################################
print (' -- All columns list -- ')
print (medals_df.columns)                   # Gives a list of all columns
#####################################################################################




#####################################################################################
# RENAMING COLUMNS
#####################################################################################
# use df.rename
    # df.rename (columns = {<mapper>})
            # to rename the column labels
    # df.rename (index = {<mapper>}
            # to rename the row labels i.e indexes

    # More on <mapper>
        # is a dict like object of the form { <old_column_name> : <new_column_name> , <old> : <new> .. and so on }
        # and the old_column name_str : is the existing column name and it will be replaced with
        # new_column_name_str : This is the new column name. What ever is in this variable will be set as is the new name for the column


# Lets rename 01 ! -> Gold  , 02 ! -> Silver , 03 ! -> Bronze
for col in medals_df.columns :
    print ( ' Got  col name : ', col)
    if col[0:2] == '01' :
        new_col_name = 'Gold'+col[4:]
        medals_df.rename(columns={col : new_col_name}, inplace=True)
    if col[0:2] == '02' :
        new_col_name = 'Silver'+col[4:]
        medals_df.rename(columns={col : new_col_name}, inplace=True)
    if col[0:2] == '03' :
        new_col_name = 'Bronze'+col[4:]
        medals_df.rename(columns={col : new_col_name}, inplace=True)

print ( ' -- After renaming columns -- ')
print(medals_df.head())
#####################################################################################



#####################################################################################
## Taking mean / max /  min  etc for every column in dataframe
# df.mean() -> Will give the mean of every column in the data frame.
#####################################################################################


#####################################################################################
# CONCLUSION
#####################################################################################
# Pandas does not allow repeating column names and appends .1 , .2 in consecutive repeating column names.
# df2 = df.copy ()
        # gives a copy of the df
# df.columns :
        # gives a list of all the column in the df
# df.rename (columns = {} <or> index = {} )
        # can be used to rename the column labels  or index labels (row-labels)
# df.mean ()
        # Gives mean for every column in data frame.
        # other operations such as max / min etc can also be applied.
#####################################################################################




