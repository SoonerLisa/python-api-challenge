# python-api-challenge
Module 6 Challenge
Best if using Kernel: dev (Python 3.13.0) ~\anaconda3\envs\dev\python.exe
Programs needed for the execution of files include:
-Visual Studio Code
-Pandas/Python
-Pyproject
-Geoviews/Geoapify
-Cartopy
-hvplot
-OpenWeatherMap

In the "Background" Module 6 Assignment, started with this statement, "Data's true power is its ability to definitively answer questions." I did not accomplish this with the starter code, BCS instruction, class activities solved solutions or BCS Xpert.

Repository URL: https://github.com/SoonerLisa/python-api-challenge.git
Base URL (Geoapify):base_url = "https://api.geoapify.com"
2-Part Assignment (Deliverable 1 and 2)
Deliverable 1: WeatherPy (WeatherPy.ipynb)
  In this section Python used to script the visualization of weather conditions of over 500 cities of varying distances from the equator.
  Part 1 has 2 requirements.
  
Requirement 1: Create Plots to Showcase the Relationship Between Weather Variables and Latitude using OpenWeatherMap to retrieve weather data from cities listed in "cities.csv" starter code to create a series of scatter plots to showcase these relationships:
    -Latitude vs. Temperature
    -Latitude vs. Humidity
    -Latitude vs. Cloudiness
    -Latitude vs. Wind Speed
 
  Requirement 2: Compute Linear Regression for Each Relationship
    -Added the their linear regression and r^2 values in midst of their plots. Most showed a       correlation of plots along the linear regression line in the Northern Hemisphere, but          flatlined on the Southern Hemisphere along with their plots:
    
**    -Northern Hemisphere: Temperature vs. Latitude
    -Southern Hemisphere: Temperature vs. Latitude
    -Northern Hemisphere: Humidity vs. Latitude
    -Southern Hemisphere: Humidity vs. Latitude
    -Northern Hemisphere: Cloudiness vs. Latitude
    -Southern Hemisphere: Cloudiness vs. Latitude
    -Northern Hemisphere: Wind Speed vs. Latitude
    -Southern Hemisphere: Wind Speed vs. Latitude**

  Part 2
  Deliverable 2: VacationPy (VacationPy.ipynb)
  -Tools used: Jupyter notebooks, the geoViews Python Library, and Geoapify API.
  First plotting all cities in the city_data_df on a map with colorful,sizeable plots related to their humidity.
  Then narrowing the df to the following conditions:
    -A max temperature lower than 27 degress but higher than 21
    -Wind speed less than 4.5m/s
    -Zero cloudiness
  The code needed to import the required libraries and load the CSV file with the weather and cooridinates data for each
  city created in Part 1.

# Narrow down cities that fit criteria and drop any results with null values
#criteria_df = [#criteria_df(city_data_df)[
  #      "City",
   #     "Lon",
    #    "Lat",
     #   (Max Temp < 27),
      #  "Max Temp" > 21,
       # "Wind Speed" < 4.5,
        #"Cloudiness" == 0
 
 Last a new DF was created "hotel_df" to hold the filtered city_data_df to store the City, County, Latitude, Longitude, and Humidity   copied from the city_data_df. A new column, "Hotel Name" was added to present each city with the closest hotel within 10,000 meters   of its coordinates.
 The hotel search did not produce any findings. Only a long list of cities without hotels were the result.

Results for the first 10 rows:
**Starting hotel search
No hotel found for farsund, PE
No hotel found for new norfolk, PE
No hotel found for jamestown, EG
No hotel found for lanzhou, PE
No hotel found for ushuaia, EG
No hotel found for albany, PE
No hotel found for carnarvon, PE
No hotel found for sisimiut, PH
No hotel found for saint-pierre, PE
No hotel found for colorado, PE**

One of the possible reasons for this result given by Xpert in BCS, were that the cities in the dataframe did not exist in the Geoapify API call. This can be verified by searching Geoapify with the cities' coordinates from the given city_data_df.csv
within the instructed distance.
I finished the last task of the assignment since some cities in Geoapify showed a match to a df city, just not populating a hotel. When hovered over a city plot, a list of statistics pop up.

**Example of pop up:
Lon: -106.7679
Lat: 34.4163
City: nabire
Hotel Name: (blank)
Country: US**

No resources outside of the BCS network were used during this challenge.
