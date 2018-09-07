# -*- coding: utf-8 -*-
"""
Spyder Editor

Created by Cynicmouth
07/01/2018
"""

import re
import os
import pandas as pd
#grabbing meta_file names as a list
path = 'E:\Dropbox\python\Github\Python_codes\python_regex'
meta_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.meta')]


def search(item, text):
    '''search pattern of item with in a text, return search results'''
    if isinstance(item, str) == False:
        raise ValueError("You must input a string!")
    
    regex_pattern = '<'+item + '>(.*)</' +item +'>'
    item_search = re.search(regex_pattern, text, re.IGNORECASE)
    
    if item_search:
        item = item_search.group(1)
        
    return item


# this should be automated with a dictionary => pending changes
id_list, loc_list, time_list = [], [], []

i=0

for file in meta_files:    
    # open each file and find needed info
    with open (file, 'r') as f:
        text = f.read()
        id = search('id',text)
        loc = search('loc',text)
        time = search('time', text)
    # end of finding info and close file
    # now append file info to a list
    id_list.append(id)
    loc_list.append(loc)
    time_list.append(time)
    
    i = i+1
    # end of lists
    # putting in a counter
    if ((i/len(meta_files))*100) % 2 == 0:
        print('Overvall Process...', ((i/len(meta_files))*100),'%')
    
    
#merging everything into a dataframe
meta_info = pd.DataFrame(
        {'id':id_list,
         'loc':loc_list,
         'time':time_list
         }
        )

#export it to csv file
meta_info.to_csv('meta_info.csv', sep = ',', encoding = 'utf-8')