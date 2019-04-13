# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:23:26 2019

@author: Федор
"""

import pandas as pd
import pymorphy2
from wordcloud import WordCloud
import matplotlib as mpl
import matplotlib.pyplot as plt

morph = pymorphy2.MorphAnalyzer()

def main():
    data = pd.read_excel('fwords3.xlsx')
    word = data['words']
    amount = data['amount']
    words = []
    amounts = []
    
    for i in range(0, len(word)):
        if('NOUN' in morph.parse(word[i])[0].tag):
            words.append(word[i].upper())
            amounts.append(amount[i])
    
    dic = {words[i]: amounts[i] for i in range(0, len(words))}
    print(dic)
    wc = WordCloud(width=4000, height=2500, background_color="white", relative_scaling=1.0,
               collocations=False, min_font_size=10).generate_from_frequencies(dic)
    plt.axis('off')
    plt.figure(figsize=(9, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    plt.savefig('rosatom_words.jpeg')
    
    
if __name__ == '__main__':
    main()