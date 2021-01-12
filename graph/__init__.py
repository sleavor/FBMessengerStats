#Import libraries necessary for the package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import datetime

#Import internal package
from FBMessengerStats import stats

def make_total_graph(df, word):
    '''Creates a graph of who says a certain word in the most messages'''
    messages = stats.messages_by_word(df,word)
    title = 'Who says ' + word + ' the most'
    plt.bar(messages.index, messages)
    plt.title(title)
    plt.xticks(fontsize=8, rotation='vertical')
    plt.show()

def make_freq_graph(df, word):
    '''Creates a graph of the frequency of a word to show up in someone's
    message'''
    messages = stats.messages_by_word(df,word)
    merged = pd.merge(messages, df.sender_name.value_counts(), right_index = True, left_index = True)
    title = 'Who says ' + word + ' most frequently'
    plt.bar(merged.index, merged.sender_name_x/merged.sender_name_y)
    plt.title(title)
    plt.xticks(fontsize=8, rotation='vertical')
    plt.show()