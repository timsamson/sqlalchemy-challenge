# sqlalchemy-challenge
<h1>Climate Analysis and Exploration</h1>

<h2>Introduction</h2>
This activity explores climate data as it relates to a data set form Hawaii. The activity analyses precipitation and temperature trends over a period as well as selected dates for a planned vacation of the users choosing. Additionally, the activity implores the user to create a FLASK api for the data set using many of the same SQL queries designed in the SQL Alchemy portions.


<h2>Technologies</h2>

<ul><li>Python 3.6</li>
<li>Jupyter Notebook</li>
<li>Pandas</li>
<li>Python</li>
<li>FLASK API</li></ul>

<h2>Dependencies</h2>
<ul>
<li>Sqlalchemy</li>
<li>Matplotlib</li>
<li>PyPlot</li>
<li>Scipy</li>
<li>Datetime</li></ul>

<h2>General Notes</h2>

Repo contains:

<ul><li>Resources- All Resource Files</li>
<li>Images- Charting Files</li>
<li>Climate.ipynb- Jupyter Notebook</li>
<li>App.py</li>
</ul>

<h2>Running the FLASK api</h2>

Please note in order to run the FLASK api for the dataset, the user will need to ensure all dependencies are installed in the local environment. Additionally the user should navigate to the folder containing "App.py" and launch terminal. to run use code python app.py . available routes will display on the webpage once the user copes the URL from the terminal into an appropriate web browser.
  
<h2>Observations and Graphs</h2>

!["Data for Last 365 Days of Dataset"](https://github.com/timsamson/sqlalchemy-challenge/blob/main/Images/Describe%20Data%20for%20Preious%20year%20prior%20to%20end%20of%20data.png)

<h3>Precipitation Levels</h3>

!["Daily Precip Levels"](https://github.com/timsamson/sqlalchemy-challenge/blob/main/Images/Daily_Precip_Level.png)

<h3>Most Active Station Temperature Histogram</h3>

The most active station for the dataset is 'USC00519281'

!["Stattion Temp Histogram"](https://github.com/timsamson/sqlalchemy-challenge/blob/main/Images/USC00519281_Histogram_Temp_Observations.png)

<h3>T-test June vs. Decemeber</h3>

!["T-test](https://github.com/timsamson/sqlalchemy-challenge/blob/main/Images/T-test.png)

The plot indicates that there is a meaningful temperature difference between the months of June and Decmeber.
Since the p-value is less than 0.05, (3.90) we can reject the null hypothesis thus conclude=ing that the difference in means is statistically significant.

<h3>Average Temperature During Trip Duration</h3>

Tmin = 65.0 | Tavg = 72.8108108108108 | Tmax = 79.0

!["Trip Average Temp"](https://github.com/timsamson/sqlalchemy-challenge/blob/main/Images/Trip_avg_temp.png)

<h3>Daily Normals During Trip Duration</h3>

!["Trip Daily Normals Data"](https://github.com/timsamson/sqlalchemy-challenge/blob/main/Images/Normals_Trip_Duration_Dataframe.png)

!["Trip Daily Normals"](https://github.com/timsamson/sqlalchemy-challenge/blob/main/Images/Daily_normals.png)
