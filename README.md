# CS3012 Project
1.  Interrogate the GitHub API to retrieve and display data regarding the logged in developer.
2.  Interrogate the GitHub API to build visualisation of data available that elucidates some aspect of the software engineering process, such as a social graph of developers and projects, or a visualisation of individual of team performance. Provide a visualisation of this using the d3js library. See https://d3js.org.

### Part one
This program allows you to login with your GitHub account and will print out your username and all of your repositories.
Using [userInterrogation.py](https://github.com/Arthur9817/CS3012-Project/blob/master/Src/userInterrogation.py).

### Part two
For this part of the project, I decided to retrieve the [10 most starred repositories](https://github.com/search?q=stars%3A>1&type=Repositories) on GitHub and plot them on a bar chart. I retrieved this data by using the '[requests](http://docs.python-requests.org/en/master/)' API in the [gitAp.py](https://github.com/Arthur9817/CS3012-Project/blob/master/Src/gitApi.py) program. With 'requests', I get the GitHub API of the 10 most starred repositories, take their names and star count and output the results into a CSV file. With these results I then create a bar chart by using the D3.js library in the [barChart](https://github.com/Arthur9817/CS3012-Project/blob/master/Src/barChart.js) file. This JavaScript file reads in the results and scales them accordingly to create the bar chart.

### Final result
![alt text](https://github.com/Arthur9817/CS3012-Project/blob/master/Images/Bar%20chart.png)
