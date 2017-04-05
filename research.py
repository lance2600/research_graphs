#!/usr/bin/python3


'''I  need # of ALL # OF POST AND shares/ # / of like and / # of comments from EACH POST on DATE last week 3/25 - 3/31, at TIME : 9-10AM; 12-1PM; 9-10PM
excel sheet in there own column '''
import facebook
import requests
import random
import json
import csv
from datetime import datetime, timedelta
from collections import Counter
from time import sleep


access_token = 'EAACEdEose0cBALrXuZCbKeZCFPOcktFzYJgx372I8ZCaZC5o1wr5gfGh2bVYbO2JjBWZByCUoORvswOsjcCjfEi0RZAlXmiTzV79djn2ZAeAXBLeCA1ZCXfXeKJ9ZBGQTL9Bdo6o6mpBE9XoFBIaWGTJoEhEjKKWevgsPlNKBJJuBuLWWA16zxTYGFQQohun5gnkZD'
sources = ['foxnews', 'tmz', 'cnn']
times = {'morning':datetime(2017,3,25,14,0), 'afternoon':datetime(2017,3,25,17,0), 'evening':datetime(2017,3,25,1,0)}


graph = facebook.GraphAPI(access_token,version='2.8')

def initcsv(sources):
    for source in sources:
        with open("sample_data.csv", 'w') as files:
            files.write("Source, Date, Message ID, Comments, Likes, Shares")

def getdata(source, start_time, end_time):
    c = ","
    profile = graph.get_object(id=source)
    posts = graph.get_connections(profile['id'], 'posts', since=start_time, until=end_time)
    try:
        for post in posts['data']:
            data = graph.get_object(post['id'], fields='created_time,message,shares,likes,comments,id')
            likes = graph.get_connections(post['id'],connection_name="likes", summary='true')
            comments = graph.get_connections(post['id'], connection_name='comments', summary='true')
            output = [str(profile['name']),str(data['created_time']),str(data['id']),str(comments['summary']['total_count']),str(likes['summary']['total_count']),str(data['shares']['count'])]
            print(",".join(output))
            with open("sample_data.csv", 'a') as files:
                files.writelines("\n"+str(",".join(output)))










    except KeyError:
        pass



def process():
    for source in sources:
        for time in times:
            getdata(source, times[time], times[time] + timedelta(hours=1))
    for x in range(6):
        for time in times:
            times[time] += timedelta(days=1)
            for source in sources:
                getdata(source, times[time], times[time] + timedelta(hours=1))


initcsv(sources)
process()


