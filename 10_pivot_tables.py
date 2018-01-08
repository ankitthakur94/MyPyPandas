

# Transform view of the data-frame.
# specially used to plot a particular column against other
# Tutorial video --> https://www.youtube.com/watch?v=xPPs59pn6qU
#

import pandas as pd
import numpy as np


states_df = pd.read_csv('cities_and_temp3.csv', encoding="ISO-8859-1" )

print (states_df)
print (states_df.pivot(index='Date', columns='City'))

## Can pass aggragate functions in the pivot as well.
    # Explore more.









