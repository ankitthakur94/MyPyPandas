############################################################
#  Objective :
############################################################
# Learn about loc and iloc in pandas series
# Learn that prefer vectorization for speed-ups over normal python for loops.
############################################################


import pandas as pd
import numpy as np
import time


############################################################
# iloc vs loc
############################################################
#   iloc : Query via index value (numeric)
#   loc : Query via index label (name)
# These are not only used to get the data but also set the data
# Also if the index / label passed to iloc/loc is not present, it is added to the Series.
############################################################


############################################################
# Using iloc in different ways.
############################################################
sports_dict = {'Archery' : 'Bhutan',
               'Cricket' : 'India',
               'Golf' : 'Scotland',
               'Sumo' : 'Japan'}

sports_series = pd.Series(sports_dict)

## Passing a single integer to .iloc[] will give the value at that index only.
# But passing a list of indexes / slice works in the same way as for strings in python / numpy array
# Start index is included and end index is not

print ('------------ iloc : Single integer query --------')
print (sports_series.iloc[2] )
## OUTPUT >
# Scotland.

print ('------- iloc : Slice query --------')
print((sports_series.iloc[0:2]))                # Snippet of series with index = 0,1
## OUTPUT >
# Archery    Bhutan
# Cricket     India

print ('------ iloc : Slice query again----------')
print((sports_series.iloc[0:3:2]))              # Snippet of series with index = 0,2
## OUTPUT >
# Archery      Bhutan
# Golf       Scotland

print ('-------- iloc : index List query---------')
print((sports_series.iloc[[1,2,3]]))            # Snippet of series with index = 0,1,2
## OUTPUT >
# Cricket       India
# Golf       Scotland
# Sumo          Japan
############################################################


############################################################
## Using loc
# Querying via the simple index label returns the value at that index.
############################################################



print ('-------- loc : index label query ---------')
print (sports_series.loc['Cricket'] )
## OUTPUT =
# India


############################################################
# USING LAMBDA IN .LOC[]
############################################################
# We can pass a function which takes the series and returns True / False
# pandas internally checks if the function is True / False for all its values (not indexes)
# In out case it checks 1-by-1 if 'Bhutan' , 'India', 'Scotland', 'Japan' pass the check or not.
# since only Scotland will pass the below string check, it index label and this value is returned.
print ('--------- loc : Function query -----------')
print (sports_series.loc[lambda s : s == 'Scotland'])
## OUTPUT >
# Golf Scotland




############################################################
# Iterating over all items in a series
############################################################
# Way 1.) Typical for loop iteration like python.
#       Slow
# Way 2.) Leverage vectorization techniques gives by pandas (thus numpy)
#       Much faster and easier to read.


# Typical way to iterate over a series similar to python dict
s = pd.Series([1,2,3,4,5])
for index, item in s.iteritems():
    print ('Value at index {} is = {}'.format(index, item))



s = pd.Series(np.random.randint(1,10000,100000,dtype='int64'))


############################################################
# 1.) Sum all nums in a series
############################################################

# Way 1.) Typical python for loop
way_1_start_time = time.time()
sum = 0
for item in s:
    sum += item
way_1_time_taken = time.time() - way_1_start_time
print (' Sum using for loop took : ', way_1_time_taken)


# Way 2.) Vectorization using numpy
way_2_start_time = time.time()
sum = np.sum(s)
way_2_time_taken = time.time() - way_2_start_time
print (' Sum using vectorization in numpy took : ', way_2_time_taken)

# Result : vectorization is 20X faster than normal for loop.



############################################################
# 2.) Increment all items by 2.
############################################################

# Way 1.) Typical for loop
print (s.head())
way_1_start_time = time.time()

for index, item in s.iteritems():                               # Typical python for loop
    # s.set_value(index, item+2)                                # Can choose any method set_value or loc
    s.loc[index] = item+2

way_1_time_taken = time.time() - way_1_start_time
print ('Using for loop took : ', way_1_time_taken)



# Way 2.)  : vectorization
way_2_start_time = time.time()

s += 2                                                          # Vectorization

way_2_time_taken = time.time() - way_2_start_time
print (' Vectorization in numpy took : ', way_2_time_taken)


# Result : Vectorization is 4000X faster
# Typical mathematical operations are vectorized in numpy
############################################################




############################################################
## Repeating index labels
############################################################
## python dict does not support duplicate keys
# but
# pandas series has no issues in duplicate index labels
############################################################


orig_sports= pd.Series ({'Archery' : 'Bhutan',
               'Cricket' : 'India',
               'Golf' : 'Scotland',
               'Sumo' : 'Japan'} )

# THis will not work since dict can't contain duplicate keys
#cricket_sports = pd.Series ({'Cricket' : 'Pakistan',
 #                 'Cricket' : 'Australia'} )

cricket_sports = pd.Series(['Pakistan', 'Australia', 'England'], index = ['Cricket', 'Cricket', 'Cricket'])


all_sports = orig_sports.append(cricket_sports)     # append function does not modify the original series. instead returns a new one
print (all_sports )
## OUTPUT >
#Archery       Bhutan
#Cricket        India
#Golf        Scotland
#Sumo           Japan
#Cricket     Pakistan
#Cricket    Australia
#Cricket      England

print ('------------ Cricket loving countries -------------- ')
print (all_sports.loc['Cricket'] )
## OUTPUT >
# Cricket        India
# Cricket     Pakistan
# Cricket    Australia
# Cricket      England
############################################################



############################################################
# Conclusion
############################################################
#  Index and values for a series need not be homogeneous i.e mix of different data types is also possible.

############################################################
# 2.) iloc vs loc
############################################################
# iloc gets the data using numbered indexing
# loc gets the data by matching label  of the index.

# iloc / loc are used to get / set the data
#   If the index / label is not present, it is added.

#   only loc can accept a lambda function (  not iloc ) (To my knowledge)
#   loc['index_label'] : returns the series snippet for which index is = the given 'index_label'
#   loc[lambda s : s == 'string'] : checks for all values (not indexes) and returns the snippet of series
#       for which value = 'string'

############################################################
# THUMB RULE FOR QUERYING
############################################################
# So to query using number indexing (single index / list of index / slice of index) use iloc
# To get the clipped series for which index = 'some_string' use loc['some_string']
# To get the clipped series for which values = 'some_string' use loc[lambda s : s = 'some_string']
# In all the above 3 querying mechanism string can be substituted by number if the series contains numbers.

############################################################
# 3.) Iterating over a series
############################################################
# Typical way to iterate over a pandas series like a python dict by using iteritems
# for index, item in series_variable.iteritems() :

############################################################
# 4.) Set value at a particular index in series
############################################################
# To set value at a particular index use
# series.loc[index] = value
# or
# series.set_value(index, value)

############################################################
# 5.) Append to series to get a new one
############################################################
# Use series1.append(series2) to append 2 series and get a new one. Does not modify series1 or series2.
############################################################
