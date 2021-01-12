#Import libraries necessary for the package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import datetime
from FBMessengerStats import DataFrame

def messages_by_day(df):
    '''Creates a series of the number of messages sent each day'''
    
    return df.groupby(['month','day','year']).size()

def find_busiest_day(df):
    '''Returns the date with the most messages sent and number on that day'''

    newdf = messages_by_day(df)
    maxDay = newdf[newdf == newdf.max()]
    return maxDay

def find_busiest_month(df):
    '''Finds which month has the most messages in it'''

    df = df.groupby(['month', 'year']).size()
    maxMonth = df[df == df.max()]
    return maxMonth

def messages_by_word(df, word):
    '''Returns series of the number of times a user has a message with the
    requested word in it'''

    word_df = df[df.content.str.contains(word) == True]
    return word_df.sender_name.value_counts()

def total_words(df):
    '''Takes dataframe of messages and finds the total number of words
    each member of the chat said'''

    return df.groupby(['sender_name']).num_words.sum()

def total_chat_words(df):
    '''Finds the total words said in the entire chat'''

    return df.num_words.sum()

def total_reacts(df):
    '''Takes dataframe of messages and finds the total number of 
    reactions a person received on their messages'''

    return df.groupby(['sender_name']).num_reacts.sum()

def total_chat_reacts(df):
    '''Takes dataframe and finds the total number of reactions throughout
    the entire chat'''

    return df.num_reacts.sum()

def num_posts(df):
    '''Takes a fbstats dataframe and finds the number of posts from each 
    member of the chat'''

    return df.sender_name.value_counts()

def total_posts(df):
    '''Find the total posts made in the chat'''

    return len(df)

def num_images(df):
    '''Takes a fbstats dataframe and finds the number of images posted
    by each member of the chat'''

    return df[~df.photos.isnull()].sender_name.value_counts()

def total_images(df):
    '''Find the total images posted in the chat'''

    return len(DataFrame.create_image_df(df))

def num_vids(df):
    '''Takes a fbstats dataframe and finds the number of videos posted
    by each member of the chat'''

    return df[~df.videos.isnull()].sender_name.value_counts()

def total_vids(df):
    '''Find the total videos posted in the chat'''

    return len(DataFrame.create_image_df(df))

def num_gifs(df):
    '''Takes a fbstats dataframe and finds the number of gifs posted
    by each member of the chat'''

    return df[~df.gifs.isnull()].sender_name.value_counts()

def total_gifs(df):
    '''Find the total gifs posted in the chat'''

    return len(DataFrame.create_gif_df(df))

def num_stickers(df):
    '''Takes a fbstats dataframe and finds the number of stickers posted
    by each member of the chat'''

    return df[~df.sticker.isnull()].sender_name.value_counts()

def total_stickers(df):
    '''Find the total stickers posted in the chat'''
    
    return len(DataFrame.create_stickers_df(df))

def num_files(df):
    '''Takes a fbstats dataframe and finds the number of files posted
    by each member of the chat'''

    return df[~df.files.isnull()].sender_name.value_counts()

def total_files(df):
    '''Find the total number of files posted in the chat'''

    return len(DataFrame.create_files_df(df))

def avg_reacts(df):
    ''' Takes a fbstats dataframe and finds the avg number of reactions
    for each message posted by each member '''

    return df.groupby(['sender_name']).num_reacts.mean()

def avg_img_reacts(df):
    ''' Takes a fbstats dataframe and finds the avg number of reactions
    for each image message posted by each member '''

    df = DataFrame.create_image_df(df)

    return df.groupby(['sender_name']).num_reacts.mean()

def avg_txt_reacts(df):
    ''' Takes a fbstats dataframe and finds the avg number of reactions
    for each text message posted by each member '''

    df = DataFrame.make_text_df(df)

    return df.groupby(['sender_name']).num_reacts.mean()

def avg_words(df):
    ''' Takes a fbstats dataframe and finds the avg number of words
    for each message posted by each member '''

    return df.groupby(['sender_name']).num_words.mean()