# Project Kojak
Project from weeks 9, 10, 11 and half of 12 of the Meetis Bootcamp

This project was a final, open ended project.   




More information for this project can be found in the following files:   
* **Kojak_Proposal.pdf** is a file with the project proposal   
* **Kojak_Presentation.pdf** is a file of the presentation slides for this project   
* **Kojak_Summary.pdf** is a file with the summary of the project findings   

### Files  
* **Kojak_DataExploration_Chiller.ipynb** - Pull lift_lines (lnes of constant lift) from the model and actual chiller data and plot in various configurations.
* **Kojak_ExtractChillerData.ipynb** - Read csv files from Optimum Energy and create unique csv files for each chiller.  The original data files include all chillers from a single plant which included 2 to 12 chillers.   
* **Kojak_LinearRegression_SelectPlants.ipynb** - Linear Regression and pymc3 models.  The code is configured so you can select the combination of chillers for the model.
* **Kojak_OptimizePlant.ipynb** - Given performace curves for a set of chillers for a chilled water plant and a required number of tons and Delta T Lift, predict operating point for plant which gives the minimum operating kW.  Uses scipy optimize.minimize library.   
* **util.py** - file containing some utility functions used multiple times   

* subdirectory **data** includes the data files for the project

### Data sources
* Optimum Energy, 411 First Avenue S, Suite 500, Seatle, WA 98104