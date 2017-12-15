##########################################################
## Objective  :
##########################################################
# Adding new col to data frames
# Merging data frames.
    # types of merge
    # ways to merge
# handling conflicting data
# merging on multiple cols
##########################################################

import pandas as pd
import numpy as np

##########################################################
## Ways to query :
##########################################################
# iloc / loc -> row based queries
# [] -> col based query
# Boolean mask -> powerful way which uses broadcasting to query.
##########################################################



s1 = pd.Series ({'Name' : 'Ankit' ,
                 'Item' : 'Milk',
                 'Cost' : 100})

s2 = pd.Series ({'Name' : 'Karan' ,
                 'Item' : 'Chocolate',
                 'Cost' : 10})

s3 = pd.Series ({'Name' : 'Madhur' ,
                 'Item' : 'Eggs',
                 'Cost' : 50})


print ('--------- Creating a df from pandas.Series ---------- ')
df_from_series = pd.DataFrame([s1, s2, s3], index = ['Store1', 'Store2', 'Store1'])
print(df_from_series)

###############################################################
## Adding new col to an existing data frame.
###############################################################

#### 1.) Add a new col as a list with num elements in list = num rows. Each element in the list is added to a row in df.
    # pandas will automatically unpack the list into row elements.
df_from_series['Date'] = ['1-December', '1-May', 'April' ]
print ( ' ---------------- Adding dates as a separate column  ------------------')
print(df_from_series)


#### 2.) Adding a scalar value
df_from_series ['IsDelivered?'] = 'True'
print ( ' ---------------- Adding IsDelivered as a separate col using scalar value ------------------')
print(df_from_series)


#### 3.) Adding a new col as a list with num elements < num of rows

## 3.1) To add a list as a new col, the len of the list must be = num of rows. If not then we will have to write None at the missing values.
df_from_series['Feedback'] = ['Good', None, 'Bad']
print ( ' ---------------- Adding Feedback ------------------')
print(df_from_series)

## 3.2) If we want to add values for only specific rows, we can use pandas series ( <row_label> : <value> )
        # So if row-labels are default (0 , 1 ..  so on ) we can mention the rows for which we want to add data  and rest of the rows will have None.
        # So a pandas series (having index values = subset of row index of df) can be added as a new col to a df. Values for the given indexes in series will be added.
        # Rest will be None.

df_from_series.reset_index(inplace=True)
new_series = pd.Series({0 : '1-Jan', 2 : 'November'})                       # Modify the date column. Will be added for rows 0 and 1.
df_from_series['Date'] = new_series
print ( ' ---------------- Modifying dates via pandas series.------------------')
print(df_from_series)



##########################################################
# Joining data frames.
##########################################################

# Ways to join 2 data frames -> ( Imagine based 2 overlapping circle diagram in set theory )
    # Full outer join (Union)
    # Inner join (Intersection)
    # Left join -> All the elements in the left set. If a few elements happen to be common to left and right, get all the detials for those elements.
# Note that the column / index on which df's are merged are considered for union / intersection.
    # Ex : If 2 df's are being merged on index, and its an outer-full join, union of index values will be considered and apt. data will be taken.


# For an example : we have a staff and a student df. Some of the students are also staff.
print ( '------------ Merging data frames ---------------  ')
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])

staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())

# We want to merge the staff and students dataframes.
# For both of the above df's the index is same 'Name' . So we will merge on this index.
# i.e
# The new df will have 'Name' as its index.

##########################################################
### 1.) OUTER JOIN
##########################################################
union_df = pd.merge(staff_df, student_df, how = 'outer', left_index=True, right_index=True)
# Syntax :  Merge the left data frame (staff_df) and the right data frame (student_df) , It will be a union , use the  index of left ddataframe , use the index of right data frame.
print ( ' -------- Outer Join (Union) -------- ')
print (union_df)
# rows in final df : rows of left + right df
# cols in final df : cols of left + right df
# Missing entries = NaN
# Ex : Mike is just a student, so its Role entry will be Nan.
##########################################################



##########################################################
### 2.) INNER JON
##########################################################
intersection_df = pd.merge(staff_df, student_df, how = 'inner', left_index=True, right_index=True)
# Syntax : similar to above, just its an inner join.
print ( ' -------- Inner Join (Intersection) -------- ')
print (intersection_df)
# rows in final df : only the indexes common (intersection) to the 2 df's ( Here the names which are both student and staff)
# cols in final df : cols of left  + right df
#   all the cols will be printed.
##########################################################



##########################################################
### 3.) LEFT JOIN
##########################################################
left_df = pd.merge(staff_df, student_df, how = 'left', left_index=True, right_index=True)
# Gets all the staff's cols / details  (i.e name and Role) but if a staff is also a student, get its student cols also ( Here : School )
print ( ' -------- Left Join on staff -------- ')
print (left_df)
# rows in final df : all the rows in the left data frame ( i.e staff_df )
# cols in final df : all the cols in left df + cols in right df if there are common indexes in left and right df's.
##########################################################


##########################################################
### 4.) RIGHT JOIN
##########################################################
# Works similar to left join.
# Gets all elements in the right set.
# If indexes are common in left and right data frames, gets cols of Left data frame as well.
# FOr the common indexes, all the cols are filled, for the indexes only in right set, the cols of left df are Nan.
##########################################################



##########################################################
### Joining on columns
##########################################################
# So far we have seen how to join data frames on indexes (2 df's should have the same index) (left_index = True and right_index= True )
# But we can join 2 df's on any 2 common cols also.

staff_df.reset_index(inplace=True)
student_df.reset_index(inplace=True)

left_df = pd.merge(staff_df, student_df,  how='left' , left_on='Name' , right_on='Name')
print (' ---- Joining on Name column ----- ')
print(left_df)
##########################################################



##########################################################
## Conflicting data.
##########################################################
# In the same example of 2 dfs' of students / staff , there are 2 common persons (James and Sally) i.e they are both students as well as staff.
# A column is common to both the data frames -> Location, but has different meaning for both of them
# In staff_df location will be the office address and in students_df -> location will be home adress.
# What if we merge the 2 df's on "Name" column
# Result -> will be a df now containing 2 Location columns -> Location_x and Location_y ,
    # Location_x -> Location values of left data frame.
    # Location_y -> Location values of right data frame.

# So pandas will preserve both the values in case of conflicting columns .

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
print ( ' Staff data -> ')
print (staff_df)
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
print (' Students data ->')
print(student_df)

left_df = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
print ( ' ----  Merged df with common cols but different  data ---  ')
print (left_df)

##########################################################



##########################################################
## Merging on multiple cols ->
##########################################################
# First name can be common for 2 people but they will be differentiated on last name. So we can merge on multiple columns.

staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])

pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])

# Here pandas will check if the Full name (First + Last) is same then only call it the same person.
##########################################################


##########################################################
## CONCLUSION
##########################################################

# Adding new column to a df

    # 1.) As a list (num_elements in list = num_rows in df)
        # df['new_column_string'] = <some_list>
            # List will be unpacked such that each element is added to a new row.
            # If num of elements in list is != num_rows, then pandas errors out.

    # 2.) A scalar value
        # df ['new_col'] = 5
            # all the rows will have value = 5 for this col.

    # 3.) Adding a pandas series, with values only for specific row indexes of df.
        # A pandas series with index_values = row_indexes of those rows for which you want to add data.
        # df ['new_col'] = <series>
            # where series = pd.Series ({ 0 : 'val1' , 1 : 'val2' } )       # Will add data for row num 1 and 3.


# Merging 2 data frames
    # general syntax :
        # new_df = pd.merge ( left_df, right_df , how='' ,  left_on = 'col_name'/ left_index = , right_on = 'col_name' / right_index= )

    # Merge can be called on
        # index of left_df and index of right df
        # index of left and col_name of right
            # anc vice versa.
            # just that on whatever merge is being called, the name should be the same.

    # For merging say union (outer join), the index / col_name which are being used to merge will be considered for union.
    # and this holds for all the merge types.

    # Merge can be of following types :
        # Outer join -> Union
        # Inner -> intersection
        # left -> All elements of left df.
        # right -> All elements of right df.


    # Conflicting data handling in merge
        # say if 2 cols are common in the 2 df's to be merged, but the data for the common cols is different.
        # after merging pandas will preseve values of both the cols by naming cols ans col_x and col_y in the final df.

    # Merging on multiple cols.
        # merge can be called on a list of cols in left_on=[] and right_on=[]

##########################################################














