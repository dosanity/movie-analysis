# Movie Analysis with Python

## Overview of Project

### Purpose
There are many different movies throughout the years that were successful, but also many that failed. There are also old movies that people consider to be classics and are still watched today. In this project, we will be analyzing movies from 1900 to 2005 and organizing the information in a Pandas data frame. After that, we will use statistical analysis and visualize different charts to determine if older movies are better than newer ones.

## Python Analysis

### Analysis of Number of Movies per Year
In our first analysis, we used Python to organize and clean the data. We created a new data frame called `movies_pdm` which showcases the major movies. To determine if it is a major movie, we only kept movies with more than 400 votes. 
```
movies_pdm = movies_pd[movies_pd['votes'] > 400]
```
Furthermore, we utilized the `count()` and `groupby` functions to investigate the number of movies that were presented each year. We named this variable `movies_year`. 
```
movies_year = movies_pdm.groupby(['year']).year.count().reset_index(name = "number of movies")
```
From this data, we generated a line chart to visualize the number of movies per year. 

![Number-Of-Movies-per-Year](https://user-images.githubusercontent.com/29410712/179326829-53bc8a8b-d16d-4cbc-8386-b90b7a95ddde.png)

From this chart, we can see that as the years progressed, the number of movies have grown exponentially.

### Analysis of Average Rating per Year
In our second analysis, we used the same functions as the first analysis. Instead of the number of major movies, we looked at the yearly average rating of major movies. This variable is called `yr_avg`.
```
yr_avg = movies_pdm.groupby(['year']).rating.mean().reset_index(name="yearly avg rating")
```
From the cleaned data, we visualized a line chart for the average rating per year.

![Average-Rating-per-Year](https://user-images.githubusercontent.com/29410712/179327016-600e06bc-7552-4aa1-9e38-091ac0930bf8.png)

In this chart, we can see that the average rating decreases as the years progress.

### Analysis of Number of Votes per Year
In our third analysis, we used a similar function and created a new data frame called `num_votes`. This time we took the sum of all the votes for major movies each year.

```
num_votes = movies_pdm.groupby(['year']).votes.sum().reset_index(name = 'votes')
```
Using this data, we generated a line chart to visualize the number of votes per year.

![Number-of-Votes-per-Year](https://user-images.githubusercontent.com/29410712/179327136-a79cd596-a90d-444d-a8f3-2fc5d70aeff2.png)

Based on the chart, we can see that the number of votes increased as the years progressed.

### Analysis of Average Number of Votes per Year
Finally, in our last analysis, we created a new data frame called `avg_votes`. This is similar to the second analysis where we took the average.

```
avg_votes = movies_pdm.groupby(['year']).votes.mean().reset_index(name = 'avg votes')
```
From this data frame, we constructed a chart to visualize the average number of votes per year.

![Average-Number-of-Votes-per-Year](https://user-images.githubusercontent.com/29410712/179327355-f26c439a-9c98-4e33-868f-da0d2c89521e.png)

As we can see, the average number of votes increase per year since the year 1900.

## Results

Throughout our analysis, we looked at different data frames to determine if old movies are better than new movies. In conclusion, old movies are not necessarily better. There are just fewer votes thus resulting in less accurate results. There are also fewer movies created during the early 1900s and the only form of entertainment was those specific movies, people would find more entertaining. Also based on the charts, there are more movies and votes per year since 1900, but the ratings have decreased. We suggest that there are other factors that need to be considered in this analysis to determine the reasoning behind the charts.

