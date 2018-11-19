# Project Fletcher
Project from last half of week 6, weeks 7 and 8 of the Metis Bootcamp

This project focussed on Natural Language Processing (NLP) and unsupervised learning.   

My project was to look at trends in the news we read has changed in the last 4 years, focussing on how 
things have changed since Donald Trump became president.

My data came from the New York Times which has API access to its news articles.  I was able to pull 4 years of 
articles from January 2015 to November 2018 (present day).  The API generated json files and I used jq to extract
the headline, snippet (a short description of the article), the date and the news desk.  I used the news desk 
information to exclude some articles such as Classified and Sports from the dataset.  

More information for this project can be found in the following files:   
* **Fletcher_Proposal.pdf** is a file with the project proposal   
* **Fletcher_Presentation.pdf** is a file of the presentation slides for this project   
* **Fletcher_Summary.pdf** is a file with the summary of the project findings   

### Files
* **Fletcher_json_jq_output.ipynb** Use NY Times API pull articles and jq to extract the data used in this project
* **Fletcher_output_df.ipynb** Take output from previous and create DataFrame for project
* **Fletcher_NLP_Analysis.ipynb** NLP and K Means analysis
* **Fletchen_LDA_Analysis.ipynb** LDA and K Means analysis
* **Fletchen_LDA_Analysis_JustCompute.ipynb** LDA and K Means analysis stripped down to just the computations 
to reduce size of running file for AWS

* subdirectory **data** contains data files for project

### Data Sources
* New York Times API(<a href="https://developer.nytimes.com/">developer.nytimes.com)