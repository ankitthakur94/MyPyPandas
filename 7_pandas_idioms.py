# Objective
####################################################
# Idiomatic solution.
    # make core efficient and more readable.
####################################################
import pandas as pd
import numpy as np


# 1.) Avoid chained indexing (i.e avoid '][')
    # i.e df[][] is to be avoided.
    # this can return a copy of the view
    # instead use iloc / loc and [] in combination.


# 2.) Chained functioning is not an issue.
     # since every function applied to a df will return a reference to the view.

    #### Method : 1 ( preferred , chained functions)
#(df.where(df['SUMLEV']==50)
#    .dropna()
#    .set_index(['STNAME','CTYNAME'])
#    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

    #### Method : 2 ( for beginners )
#df = df[df['SUMLEV']==50]
#df.set_index(['STNAME','CTYNAME'], inplace=True)
#df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})




states_df = pd.read_csv('states.csv', encoding="ISO-8859-1", index_col=0 )
print (states_df)



def get_min_max (row):
    print (row)
    row['min'] = np.min(row)
    row['max'] = np.max(row)
    return row


# Using apply function on df.
    # Takes in a function and applies it on every row / col one-by-one. The function should accept that row / col as argument.
    # axis = 1  -> applies function row-wise
    # axis = 0 -> applies function col-wise.
new_df = states_df.apply(get_min_max, axis=1)
print (new_df)


# 3.) Use lambda function instead of normal function for idiomatic python


####################################################
# CONCLUSION
####################################################

# Do no use chained indexing df[][]
# Use of chained functioning is encouraged.
# df.apply () function applies a function :
    # row - wise  if axis = 1
    # col - wise if axis = 0
####################################################















