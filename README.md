# sqlalchemy-challenge

Step 1 - Climate Analysis and Exploration
To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

Objectives:
-Use the provided hawaii.sqlite files to complete your climate analysis and data exploration.

-Use SQLAlchemy create_engine to connect to sqlite database.

-Use SQLAlchemy automap_base() to reflect tables into classes and save a reference to those classes called Station and Measurement.

-Link Python to the database by creating a SQLAlchemy session.

-Close out your session at the end of your notebook.

Precipitation Analysis
Finding the most recent date in the data set.

Using this date, retrieve the average precipitation per day for the previous 12 months. The query should be sorted by date ascending. Note you do not pass in the date as a variable to your query.

Load the query results into a Pandas DataFrame and set the index to the date column.

Plot the results using the DataFrame plot method. NOTE: Your plot will look different from the one below.

precipitation

Use Pandas to print the summary statistics for the precipitation data. HINT: This will be a single line of code.

Station Analysis
Design a query to calculate the total number of stations in the dataset.

Design a query that lists all stations with their corresponding observation count in descending order (observation count corresponds to the number of rows per station).

Which station id is the most active (i.e., has the greatest number of observations)?

Calculate the lowest, highest, and average temperature for that station id (i.e., the one with the greatest number of observations).

Hint: You will need to use functions in your queries.

Design a query to retrieve the last 12 months of temperature observation data (TOBS) for the most active station.

Plot the results as a histogram with bins=12.

station-histogram

Close out your session.

Step 2 - Climate App
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

Use Flask to create your routes.
Routes
/

Home page.

List all routes that are available.

/api/v1.0/precipitation

Using the query from part 1 (most recent 12 months of precipitation data), convert the query results to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary (note the specific format of your dictionary as required from above).
/api/v1.0/stations

Return a JSON list of stations from the dataset.
/api/v1.0/tobs

Query the dates and temperature observations of the most active station for the most recent 12 months of data.

Return a JSON list of temperature observations (TOBS) for that year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>

Create a query that returns the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date.

When given the start and the end date, calculate the minimum, average, and maximum obvserved temperature for dates between the start and end date inclusive.

Return a JSONified dictionary of these minimum, maximum, and average temperatures.

