# Movie Analysis

# We will be doing an analysis with Pandas on movies to see if older movies are better than newer movies.

# imports
import csv
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

movies_pd = pd.read_csv("movies.csv")
movies_pd.head()

movies_pd.info()

movies_pdm = movies_pd[movies_pd['votes'] > 400]
print(movies_pdm['title'].count(), "movies have more than 400 votes.")

print("Average rating:", movies_pd['rating'].mean())
print('Average rating of major movies:', movies_pdm['rating'].mean())

movies_pdm = movies_pdm.sort_values('rating', ascending = False)
movies_pdm.head()

high_movies = []
high_movies.append(movies_pdm['title'].iloc[0])
high_movies.append(movies_pdm['title'].iloc[1])

print('Highest rated movies:', str(high_movies)  + ',', 'Rating:', movies_pdm['rating'].iloc[1])

movies_com = movies_pdm[movies_pdm['Comedy'] == 1]
movies_dram = movies_pdm[movies_pdm['Drama'] == 1]
movies_comdram = movies_pdm[(movies_pdm['Drama'] == 1) & (movies_pdm['Comedy'] == 1)]

comedies = movies_com.count()[1]
dramas = movies_dram.count()[1]
comdram = movies_comdram.count()[1]

print(comedies, "major movies are comedies.")
print(dramas, "major movies are dramas.")
print(comdram, "major movies are both, comedies and dramas.")

print(movies_com['rating'].describe())
print(movies_dram['rating'].describe())

movies_year = movies_pdm.groupby(['year']).year.count().reset_index(name = "number of movies")
print(movies_year)

plt.plot(movies_year['year'], movies_year['number of movies'])
plt.title('Number of Movies Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
# plt.show()
#

yr_avg = movies_pdm.groupby(['year']).rating.mean().reset_index(name="yearly avg rating")
print(yr_avg)
plt.plot(yr_avg['year'], yr_avg['yearly avg rating'])
plt.title('Average Rating per Year')
plt.xlabel('Year')
plt.ylabel('Average Rating')
# plt.show()
#

num_votes = movies_pdm.groupby(['year']).votes.sum().reset_index(name = 'votes')
print(num_votes)
plt.plot(num_votes['year'], num_votes['votes'])
plt.title('Number of Votes per Year')
plt.xlabel('Year')
plt.ylabel('Number of Votes')
# plt.show()
#

avg_votes = movies_pdm.groupby(['year']).votes.mean().reset_index(name = 'avg votes')
print(avg_votes)
plt.plot(avg_votes['year'], avg_votes['avg votes'])
plt.title('Average Number of Votes per Year')
plt.xlabel('Year')
plt.ylabel('Average Number of Votes')
# plt.show()
#