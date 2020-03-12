# -*- coding: utf-8 -*-
import pandas as pd
import codecs
import numpy as np
import gc
# file_name = '/Users/hw_liu/Desktop/data/HaiNanSpring/zone.csv'
file_name = '/Users/doran/Desktop/data/Holiday_Quantity/9072457.csv'
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# df = pd.read_csv(file_name,sep=',',engine = 'python',iterator=True)
df = pd.read_csv(file_name,sep=',')

df['zone'] = df['zone'].str.strip()

basket = df.pivot_table(columns = "zone",index="uid",values="quantity",
              aggfunc=np.sum).fillna(0)
# print(basket.head(20))

# 列名为商品名称，每一行为一个订单。
basket2 = (df.groupby(['uid', 'zone'])['quantity'].sum().unstack().reset_index().fillna(0).set_index('uid'))

# print(basket2.head())

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
basket_sets = basket.applymap(encode_units)
basket_sets2 = basket2.applymap(encode_units)

frequent_itemsets = apriori(basket_sets2, min_support=0.05, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

print(frequent_itemsets)
print(rules)