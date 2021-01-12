# Facebook Messenger Stats

A custom library by Shawn Leavor to get stats from your Facebook chat data using numpy, pandas, and matplotlib libraries.

To find out how to download your Facebook messenger history, follow [this guide](https://www.zapptales.com/en/download-facebook-messenger-chat-history-how-to/) and download as a .json file. For projects, you can download the data within a specified timeframe, like an entire month / year.

Once you have the file, place the data files you want to look at in a folder with your python code and open all the .json files. Facebook messenger stats can create a dataframe of all messages.

You can use the different functions in the library to get meaningful insights from your data.

The library is broken up into 3 sections: DataFrame, graph, and stats.

## DataFrame

DataFrame is used to create and manage different dataframes within the stats and graph categories. It is also used to initalize you messenger DataFrame. 

`FBChatStats.DataFrame.make_df(files)`

This function will create a dataframe from all of your files. Be sure to make all the files into one list. It will also handle changing the timestamp to the correct year format. Also finds the number of words and reactions in each post.

`FBChatStats.DataFrame.create_time_df(dataframe, hour 1, hour 2)`

Creates a dataframe for posts only during the specified hours. For example using `create_time_df(df, 0, 5)` will give you all the posts made between midnight and 5 AM.

## Stats

Stats is the most important part as it contains all the stats for your messenger chat. 

`FBChatStats.stats.find_busiest_day(dataframe)`

Provides the day where the most messages were sent.

`FBChatStats.stats.find_busiest_month(dataframe)`

Provides the month where the most messages were sent.

`FBChatStats.stats.total_words(dataframe)`

Finds the total number of words said by each member of the chat and returns it as a series.

`FBChatStats.stats.total_chat_words(dataframe)`

Returns the total number of words said within all messages.

`FBChatStats.stats.total_reacts(dataframe)`

Finds the total number of reactions received by each member of the messenger chat

`FBChatStats.stats.total_chat_reacts(dataframe)`

Finds the total number of reactions given/received in the entire chat.

`FBChatStats.stats.num_posts(dataframe)`

Returns the number of posts by each member of the messenger group as a series.

`FBChatStats.stats.total_posts(dataframe)`

Finds the total number of posts made within the chat.

`FBChatStats.stats.num_images(dataframe)`

Returns the number of images by each member of the messenger group as a series.

`FBChatStats.stats.total_images(dataframe)`

Finds the total number of images posted within the chat.

`FBChatStats.stats.num_vids(dataframe)`

Returns the number of videos by each member of the messenger group as a series.

`FBChatStats.stats.total_vids(dataframe)`

Finds the total number of videos posted within the chat.

`FBChatStats.stats.num_gifs(dataframe)`

Returns the number of gifs by each member of the messenger group as a series.

`FBChatStats.stats.total_gifs(dataframe)`

Finds the total number of gifs posted within the chat.

`FBChatStats.stats.num_stickers(dataframe)`

Returns the number of stickers by each member of the messenger group as a series.

`FBChatStats.stats.total_stickers(dataframe)`

Finds the total number of stickers posted within the chat.

`FBChatStats.stats.num_files(dataframe)`

Returns the number of files by each member of the messenger group as a series.

`FBChatStats.stats.avg_reacts(dataframe)`

Finds the average number of reactions a user receives on their messages.

`FBChatStats.stats.avg_img_reacts(dataframe)`

Finds the average number of reactions a user receives on their image messages.

`FBChatStats.stats.avg_txt_reacts(dataframe)`

Finds the average number of reactions a user receives on their text messages.

`FBChatStats.stats.avg_words(dataframe)`

Finds the average number of words a user says in their messages.

## Graphs

Graphs builds off of stats and uses the stats to create visual insights.

`FBChatStats.graph.make_total_graph(dataframe, word)`

Returns a bar graph of the total number of times a word is said by each user.

`FBChatStats.graph.make_freq_graph(dataframe, word)`

Returns a bar graph of the frequency of a word to show up in a message by each user.
