#Compare 2 csv's /xlsx files using pandas - python

import pandas as pd
import ssl

try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


#df1 = pd.read_csv('https://bit.ly/movieusers',sep='|')
df1 = pd.read_csv('https://bit.ly/movieusers',sep='|', header=None)
#https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user

print(df1.head())
df2 = pd.read_csv('https://bit.ly/movieusers',sep='|', header=None)
#df2 = pd.read_csv('https://bit.ly/uforeports')
#https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv
print(df2.head())


# using pandas merge method and apply outer join

df_join = df1.merge(right = df2, left_on = df1.columns.to_list(), right_on = df2.columns.to_list(), how = 'outer')

print(df_join.head())

df1.rename(columns = lambda x : x + '_file1', inplace = True )
df2.rename(columns = lambda x : x + '_file2', inplace = True )

df_join = df1.merge(right = df2, left_on = df1.columns.to_list(), right_on = df2.columns.to_list(), how = 'outer')

records_present_in_df1_not_in_df2 = df_joinloc[df_join[df2.columns.to_list()].isnull().all(axis =  1), df1.columns.to_list()]

records_present_in_df2_not_in_df1 = df_joinloc[df_join[df1.columns.to_list()].isnull().all(axis =  1), df2.columns.to_list()]

# quite similar to SQL JOIN



