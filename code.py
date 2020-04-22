# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset
df = pd.read_csv(path)

# convert state column in lower case
df['state'] = df['state'].apply(lambda x: x.lower())

# Calculate the total
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]

# sum of amount
sum_row = df[["Jan", "Feb", "Mar", "total"]].sum()

# append the row
df_final = df.append(sum_row, ignore_index=True)



# --------------
import requests

# intialize the url
url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response = requests.get(url)

# read the html file 
df1 = pd.read_html(response.content)[0]
df1 = df1.iloc[11:, :]
df1 = df1.rename(columns=df1.iloc[0, :]).iloc[1:, :]
df1['United States of America'] = df1['United States of America'].apply(lambda x: x.replace(" ", "")).astype(object)
print(df1.head())


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
value = list(df1['US'].values)

mapping={}
for val,country in enumerate(df1['United States of America']):
        if country not in mapping:    
            mapping[country]=value[val]
data = df_final['state'].apply(lambda x:mapping[x] if x in mapping else np.nan)
df_final.insert(6,'abbr',data)
print(df_final.head(20))

# Code ends here


# --------------
# Code stars here
df_final['abbr'].iloc[6]='MS'
df_final['abbr'].loc[df_final['state']=='tenessee']='TN'
print(df_final.head(10))
# Code ends here


# --------------
# Code starts here
df_sub = df_final.groupby(['abbr'])['Jan','Feb','Mar','total'].sum()
mapfun = lambda x: ("$"+str(x)) if (isinstance(x,float)) else x
formatted_df=df_sub.applymap(mapfun)
print(formatted_df.head())
# Code ends here


# --------------
# Code starts here
sum_row = pd.DataFrame(df_final[['Jan','Feb','Mar','total']].sum())
df_sub_sum = sum_row.transpose()
df_sub_sum = df_sub_sum.applymap(lambda x:"$"+str(x))
final_table = formatted_df.append(df_sub_sum)
print(final_table)
final_table = final_table.rename(index={0:'Total'})


# Code ends here


# --------------
# Code starts here
df_sub['total'] = df_sub['Jan'] + df_sub['Feb'] + df_sub['Mar']
df_sub['total'].plot(kind='pie')

# Code ends here


