

import pandas as pd
import numpy as np

# set_index is destructive process i.e it promotes a column to index and deletes col from data frame.

def rename_cols (medals_df) :
    for col in medals_df.columns :
        if col[0:2] == '01' :
            new_col_name = 'Gold'+col[4:]
            medals_df.rename(columns={col : new_col_name}, inplace=True)
        if col[0:2] == '02' :
            new_col_name = 'Silver'+col[4:]
            medals_df.rename(columns={col : new_col_name}, inplace=True)
        if col[0:2] == '03' :
            new_col_name = 'Bronze'+col[4:]
            medals_df.rename(columns={col : new_col_name}, inplace=True)

    print ( ' -- After renaming columns following is the list of cols -- ')
    print(medals_df.columns)



medals_df = pd.read_csv('countries_and_medals_orig.csv', encoding="ISO-8859-1", index_col=0 , header=0  )
# header = 0 : Use row-0 as labels for columns
# index_col = 0 : Use column 0 as index for rows.
rename_cols(medals_df)

print (' ------------  Printing original dataframe -------------- ')
print (medals_df.head())


# re-set index : copies index col as a normal column and enables default numbered index
print (' ------------  Resetting index to default -------------- ')
medals_df.reset_index(inplace=True)
print (medals_df.head())


print (' ------------  Setting index to country names -------------- ')
medals_df.set_index('Team (IOC code)', inplace=True)
print (medals_df.head())



# Multi-level indexing
# Give a list of cols to be set as indexing in set_index.

medals_df.reset_index(inplace=True)
#medals_df.set_index(['Gold', 'Silver'], inplace=True)
print (medals_df['Gold'].unique)













