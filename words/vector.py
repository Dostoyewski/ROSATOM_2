# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:27:41 2019

@author: Федор
"""
import pymorphy2
import pandas as pd

morph = pymorphy2.MorphAnalyzer()
p = morph.parse('деревья')[0]
print(p.normal_form)

data = pd.read_excel('words.xlsx')
words = data['words']
amount = data['amount']
fwords = pd.DataFrame()
i = 0

#for word in words:
#    p = morph.parse(word)[0]
##    print(p.normal_form)
#    fwords = fwords.append({'word': p.normal_form, 'amount': amount[i]}, ignore_index=True)
#    i += 1
#
#fwords.to_excel('fwords.xlsx')

data = pd.read_excel('prepared_data.xlsx')
for i in range(0, len(data['text'])):
    text = data['text'][i].split()
    ww = ''
    for word in text:
        ww = ww + morph.parse(word)[0].normal_form + ' '
    fwords = fwords.append({'word': ww}, ignore_index = True)
    
fwords.to_excel('data.xlsx')
    