# Project McNulty
Project from weeks 4, 5 & half of 6 of the Meetis Bootcamp

This project focussed on supervised machine learning & data visualization.   

My projct was predicting flight delays at Seatac Airport in Seattle, WA.  Given a large dataset of 
filght arrivals from August 2016 to July 2018 (2 years) as well as weather information from this period I was able to 
predict with 65% accuracy and 64% recall if a flight arrival would delayed.  I took for a definition of delayed the 15 
minute mark commonly used in the industry.  

Some interesting information came out of this investigation regarding flight delays.
* The delays do not vary that much from day to day.  On average over this time, flights were delayed 19% of the time.
The variation throughout the year was not significant.
* The variation from airline to airline was not that significant.
* There are more flights in the summer than the winter with slightly more flights right before Christmas.
* Flight delys come mostly from National Air Service (out of control of airlines), Late Aircraft (plane did not arrive 
on-time from previous flight) and Carrier.  Weather and Security delays were not significant contributors.

More information for this project can be found in the following files:   
* **McNulty_Proposal.pdf** is a file with the project proposal   
* **McNulty_Presentation.pdf** is a file of the presentation slides for this project   
* **McNulty_Summary.pdf** is a file with the summary of the project findings   

## Files  
* **McNulty_DataRead.ipynb**   
* **McNulty_Visualize.ipynb**
* **McNulty_Analysis.ipynb** 
* subdirectory **data** includes the data files for the project

## Data sources
* Bureau of Transportation web site (<a href="http://transtats.bts.gov">transtats.bts.gov</a>) which has all the flight arrival and departures up to July 2018
* NOAA web site (www.ncdc.noaa.gov) which has historical weather data by location
