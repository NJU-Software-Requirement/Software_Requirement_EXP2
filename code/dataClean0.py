# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:22:05 2020

@author: ZQY
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
###处理严重性数据
'''
with open('./data.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)

    
dataframe_data=pd.DataFrame(json_data).T
dataframe_data.reset_index(drop=True,inplace=True)

dataframe_data['subimportance']=dataframe_data['importance'].map(lambda x:x[3:])
dataframe_data['importance']=dataframe_data['importance'].map(lambda x:x[0:3])

data_groupby_subimpt=dataframe_data.groupby(['importance','subimportance']).count()

'''
###处理评论数据
with open('./issues.json','r',encoding='utf-8')as fp:
    issues_json=json.load(fp)

issues_df=pd.DataFrame(issues_json)

def get_value(emojis_dict):
    x=0;
    for value in emojis_dict.values():
        x+=int(value);
    
    x-=2*int(emojis_dict.get('thumbs down',0))
    x-=2*int(emojis_dict.get('confused',0))
    return x,0


def get_pn(emojis_dict):
    x=0;
    for value in emojis_dict.values():
        x+=int(value);
    
    x-=int(emojis_dict.get('thumbs down',0))
    x-=int(emojis_dict.get('confused',0))
    return x
    
def get_nn(emojis_dict):
    x=0;
    x+=int(emojis_dict.get('thumbs down',0))
    x+=int(emojis_dict.get('confused',0))
    return x
def sigmod(x):
    return 1.0/(1.0+np.exp(-x))
max_comment=issues_df['comments'].max()
min_comment=issues_df['comments'].min()
issues_df['comments_val']=issues_df['comments'].apply(lambda x: sigmod(5*(x)/(max_comment)))
issues_df['positive_emojis_num']=issues_df['emojis'].apply(get_pn)
issues_df['negative_emojis_num']=issues_df['emojis'].apply(get_nn)
issues_df['emojis_val']=issues_df['positive_emojis_num']-issues_df['negative_emojis_num']
max_emojis=issues_df['emojis_val'].max()
min_emojis=issues_df['emojis_val'].min()
issues_df['emojis_val']=issues_df['emojis_val'].apply(lambda x:sigmod(5*(x)/(max_emojis)))


issues_df['total_val']=issues_df['emojis_val']+issues_df['comments_val']
###issues_df=issues_df[(issues_df['comments']!=0) | (issues_df['emojis']!={}) | ( issues_df['val']!=0)]
issues_df=issues_df[['ID','comments','comments_val','emojis','positive_emojis_num','negative_emojis_num','emojis_val','total_val']]
issues_df['total_val']=issues_df['total_val']/2
issues_df.sort_values(by='total_val',ascending=False,inplace=True)
issues_df.reset_index(drop=True,inplace=True)


issues_df.to_json('./val_sorted.json')
issues_df.to_csv('./val_sorted.csv')

plt.scatter(issues_df['total_val'],issues_df['comments_val'],s=1)
plt.xlabel('total val')
plt.ylabel('comments val')
plt.savefig('./total_coments.jpg')
plt.show()

plt.scatter(issues_df['total_val'],issues_df['emojis_val'],s=1)
plt.xlabel('total val')
plt.ylabel('emojis val')
plt.savefig('./total_emojis.jpg')
plt.show()

plt.scatter(issues_df['emojis_val'],issues_df['comments_val'],s=1)
plt.xlabel('emojis val')
plt.ylabel('comments val')
plt.savefig('./emojis_comments.jpg')
plt.show()


plt.scatter(issues_df['positive_emojis_num'],issues_df['negative_emojis_num'],s=1)
plt.xlabel('positive_emojis_num')
plt.ylabel('negative_emojis_num')
plt.savefig('./pn_emojis.jpg')
plt.show()
