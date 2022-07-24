import csv
import re
import statistics
from functools import total_ordering
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


"""with open('/home/alsyke/Downloads/Movies dataset - title.basics (1).csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)"""
data = pd.read_csv('/home/alsyke/Downloads/Movies dataset - title.basics (1).csv')
columns = ['id','titleType','originalTitle','runtimeMinutes','genres','numVotes','startyear','rating']

answer = input(" Display the highest rating and movie name, lowest rating and movie name, and average runtime minutes(highestrated/lowestrated/runtimeminutes avg)")
if answer =="highestrated":

    # .....for Higest rated movie......
    Higest_ratedMovie=data.nlargest(1,'rating')[['startYear','originalTitle','rating',]]\
        .set_index('originalTitle')
    print(Higest_ratedMovie)
if answer =="lowestrated":
    # ....for lowest rated movie......

    lowest_ratedMovie=data.nsmallest(1,'rating')[['startYear','originalTitle','rating']]\
        .set_index('originalTitle')
    print(lowest_ratedMovie)

elif answer=="runtimeminutes avg":
    print(data['runtimeMinutes'].value_counts().mean())

#check the genres information
#print(data.groupby('genres').genres.count())
#print(data.genres.describe())
#fill the data
data.genres = data.genres.fillna('Drama,short')
print(data.genres)
#check the percentage of null value
#print(data.isnull().sum()/len(data)*100)


#print(data.sort_values(by="genres"))

#print(data.genres.str.split('|',expand=True).iloc[:0:2])
#print(data.groupby(['genres']).rating.mean().sort_values(ascending=False))

#check the genres in data
#print(data['genres'])
#check the genres datatype
#print(data['genres'].dtype)
answer = input("For a given genre display the number of movies and the mean rating(yes/no)")
if answer =="yes":
    list1 = []
    for value in data['genres']:
        list1.append(value.split(','))
        print(list1)

"""one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)
        print(one_d)

uni_list=[]
for item in one_d:
    if item not in uni_list:
        uni_list.append(item)
        print(len(uni_list))"""

one_d = []
for item in list1:
    for item1 in item:
        one_d.append(item1)
        print(one_d)

from collections import Counter

print(Counter(one_d))
pass


# genres and its ratings
genre_ratings = data.groupby('genres').rating.agg(['count', 'mean'])
print(genre_ratings[genre_ratings['count'] >= 10])
"""data.info()"""

answer=input(" Display top ten highest rated movies (yes/no)")
if answer=="yes":
    top10_len=data.nlargest(10,'rating')[['originalTitle','rating']]\
        .set_index('originalTitle')
    print(top10_len)


#print(data['genres'])

#for check the missing value in column
#print(data.isnull().sum(axis=0))

#for check the missing value in column
#print(data.isnull().sum(axis=1))
