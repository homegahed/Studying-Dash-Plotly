# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:58:34 2022

@author: hmegahed
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



url = 'assets/dsc.csv'

df = pd.read_csv(url)

# change column names to lower case
df.columns = list(df.columns.str.replace("-","").str.lower())


numeric_cols = df.columns[2:5]


for i in numeric_cols:
    df[i] = df[i].str.replace(',', '')
    df[i] = df[i].str.replace('-', '0')
    df[i] = df[i].astype('float')

df['code'] = df['code'].astype('O')
df['year'] = df['year'].astype('O')

df  = df.query('imports > 0 & exports > 0 & reexports > 0')

items_list = list(df['item'].unique())
# print(len(a))

items_list.remove('04- Prepared Foodstuffs')
# print(items_list)

items_dict = {}
for i in items_list:
    items_dict[i[:2]] = i[4:] 

items_df = pd.DataFrame(items_dict, index=[0]).T

items_df['serial'] = np.arange(1, 22, 1)

items_shortname = ['Live animals', 'Vegetables', 'Oils','Food Baverage', 
                   'Minerals', 'Chemicals', 'Plastic Ruber', 'Leather', 'Wood', 
                   'Paper', 'Textiles', 'Footwear', 'Cement', 'Precious stones',
                   'base metals', 'Machinery', 'Vehicles', 'Optical Medical',
                   'Arms', 'Miscellaneous', 'Art work']

items_df['short'] = items_shortname
   
items_df = items_df.reset_index(drop=False)


items_df.columns = ['codes', 'items', 'serial', 'abrev']
# print(items_df.head())
# print(items_df)
merged_df = df.merge(items_df, left_on='code', right_on='serial')

merged_df = merged_df.drop(['code', 'item'], axis = 1)

dff = merged_df[['serial', 'codes', 'items', 'abrev', 'year', 'trade',
                  'imports', 'exports', 'reexports']]

dff['total'] = dff['imports'] + dff['exports'] + dff['reexports']

vars_trade = ['imports', 'exports', 'reexports', 'total']




items_sums = dff.groupby('abrev')[vars_trade].sum()
items_sums.to_csv('assets/trade_sum_items.csv', header=True)



items_means = dff.groupby('abrev')[vars_trade].mean()
items_means.to_csv('assets/trade_means_items.csv', header=True)



year_sums = dff.groupby('year')[vars_trade].sum()
year_sums.to_csv('assets/trade_sums_years.csv', header=True)



year_means = dff.groupby('year')[vars_trade].mean()
year_means.to_csv('assets/trade_means_years.csv', header=True)

# plt.figure(figsize=[20,15])
# plt.bar(items_means.index, items_means['trade']);
# plt.xticks(rotation=45)

# # print(items_df.columns)

# print(dff.columns)

dff.to_csv('assets/trade_clean.csv')
