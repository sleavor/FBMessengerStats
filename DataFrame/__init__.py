#Import libraries necessary for the package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import datetime

def get_year(date):
    '''Grabs year from a date timestamp ms'''
    
    return(datetime.datetime.fromtimestamp(date/1000).year)

def get_month(date):
    '''Grabs month from a date timestamp ms'''
    
    return(datetime.datetime.fromtimestamp(date/1000).month)
    
def get_day(date):
    '''Grabs day from a date timestamp ms '''
    
    return(datetime.datetime.fromtimestamp(date/1000).day)
    
def get_hour(date):
    '''Grabs hour from a date timestamp ms'''
    
    return(datetime.datetime.fromtimestamp(date/1000).hour)

def get_min(date):
    '''Grabs minute from a date timestamp ms'''
    
    return(datetime.datetime.fromtimestamp(date/1000).minute)

def make_df(files):
    ''' Makes list of Facebook Messenger data files into dataframe'''
    
    #Initializes empty list
    messages = []
    
    #Loops through files and grabs each message adding to list
    for file in files:
        read = json.load(open(file))
        for message in read['messages']:
            messages.append(message)
    
    #Create dataframe
    df = pd.DataFrame(messages)
    
    #Add words, number of words, number of reactions
    df['words'] = df['content'].str.split()
    df['num_words'] = df['words'].str.len()
    df['num_reacts'] = df['reactions'].str.len()
    df['num_reacts'] = df['num_reacts'].fillna(0)
    
    #Add day, month, year, and time of day columns
    df['day'] = df.timestamp_ms.apply(lambda date: get_day(date))
    df['month'] = df.timestamp_ms.apply(lambda date: get_month(date))
    df['year'] = df.timestamp_ms.apply(lambda date: get_year(date))
    df['hour'] = df.timestamp_ms.apply(lambda date: get_hour(date))
    df['min'] = df.timestamp_ms.apply(lambda date: get_min(date))

    #Return the dataframe of messages
    return df

def create_time_df(df, minLim, maxLim):
    '''Creates a dataframe where posts were only made in the specified hours'''
    
    return df[(df.hour >= minLim) & (df.hour <= maxLim)]

def create_image_df(df):
    '''Creates a dataframe with only image posts'''

    return df[~df.photos.isnull()]

def create_vid_df(df):
    '''Creates a dataframe with only video posts'''

    return df[~df.videos.isnull()]

def create_gif_df(df):
    '''Creates a dataframe with only gif posts'''

    return df[~df.gifs.isnull()]

def create_stickers_df(df):
    '''Creates a dataframe with only sticker posts'''

    return df[~df.sticker.isnull()]

def create_files_df(df):
    '''Creates a dataframe with only file posts'''

    return df[~df.files.isnull()]

def make_mem_df(df, member):
    '''Returns a dataframe for posts for a member'''

    return df[df.sender_name==member]

def make_word_df(df):
    '''Returns a dataframe that only has posts with at least one word in them'''

    #returns the df of all word messages
    return df[df.num_words > 0]

def make_text_df(df):
    '''Returns a dataframe with only text messages'''

    #returns the df of all text messages
    return df[(df.photos.isnull()) & (df.videos.isnull())]