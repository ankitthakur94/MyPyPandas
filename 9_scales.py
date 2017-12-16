
import pandas as pd
import numpy as np

## Types of scales for data

    # 1) Ratio scale :
            # units are equally spaced.
            # mathematical operations are valid.
            # Ex : height and weight.

    # 2) Interval scale :
            # units are equally spaced.
            # * and / operations are not valid
            # there is no true zero.
                # i.e a zero value does not indicate absence of value.
            # Ex : measure of temprature  / direction in compass.
                # 0-degree direction does not mean missing value.

    # 3) Ordinal Scale :
            # Order of values is important.
            # values are not evenly spaced.
            # Ex :
                # Grading A+ / A / A- / B+ / B / B-

    # 4) Nominal Scale :
            # Categorical data.
            # No order
            # No meaning of applying mathematical operations.
            # Ex : Teams in a football tournament.


# Pandas has inbuilt support for data type conversions.

# Usage 1 :
    # Conversion of a column having grades from categorical data type to ordinal data type.
    # This can be useful when we want to query say students having grades > B (i.e A+/A/A-)
    # In nominal scale (categorical) we can't have comparison operations, for > B to work we will have to apply some string -> int conversion techniques.
    # To avoid that we will convert nominal to ordinal scale (which has order) and thus comparison operations can be applied.


print ( ' ---- Original data frame ---- ')
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0:'Grades'}, inplace=True)
print (df.head())
print ('data types : ', df.dtypes)


print ( ' ---- Converting to category data type ---- ')
print (df['Grades'].astype('category').head())



print ( ' ---- Adding ordering also (ie ordinal data type) ---- ')
df['Grades'] = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],     # Categories have to be mentioned in increasing order.
                             ordered=True)
print (df['Grades'].head())

# now since we have given a logial order, we can perform comparison operations and generate boolean masks to be used for broadcasting.
# min / max () operations can also be used on ordinal data.


# This will print a boolean mask.
print (  df['Grades'] > 'B' )





## Reducing continuous values into categorical data
    # can be used for good visualization.

# pandas can automatically convert this.

# pd.cut (<df['col] / seires , 4 , lables = ['lable1' , 'label2',  'label3',  'label4' ])
    # Creates 4 bins equally spaced (Ex : 0-10 , 10-20 , 20-30)
s1 = pd.Series ([2,12,232,45,56,87,34,32,56,34,45,57,97], dtype=int)
print (pd.cut(s1, 4 , labels= ['l1' , 'l2' , ';3', 'l4']))



# pandas also provides with a lot of other options for categorizing data (.i.e populating bins for the data)










