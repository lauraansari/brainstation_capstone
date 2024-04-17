This is my capstone project submission for BrainStation's Data Science programe.

Problem statement: It is estimated that 99% of the world's population live in places with bad air quality. Poor air quality has adverse health affects on human, which means lower life quality and expectancy, and higher healthcare costs. Links between the effects of human activities and their consequences (for example, urbanization, traffic, and climate change) have been long established, however, public awereness on the impact of these factors are relatively low and the available information is often confusing. Establishing a model that's capable to capture the impact of external factors and provide accurate forecasts could improve awereness and engagement with the topic, which in turn could help facilitate a change for the better. To maximize potential reach, a location with a high public interest in the topic is chosen: 45% of residents in Los Angeles think that air quality is a 'big problem'. Moreover, the region has been ranked as the 4th most polluted city in the US, therefore improvement measures would be highly beneficial.

Proposed solution: In this project, I use forecasting and machine learning to predict air quality in Los Angeles over the next 10 years. I utilize autoregressive moving-average models, such as ARIMA and SARIMA and machine learning using linear regression to create accurate models that provide reliable future values. To improve the model accuracy, external factors (i.e. factors that may have an impact on AQI values) are taken into consideration and added.
I intend to use advanced data visualisation to convey the insights and present multiple what-if scenarios based on different external factors, such as weather-related factors.

Expected impact: An estimated 5% increase in public engagement and awereness could boost inidividual willingness to intervene and improve the situation. Increased awereness could also help vulnerable groups to plan ahead and make informed lifestyle decisions (e.g. adjusting outdoor activities) based on the time of the year/month, which could decrease their exposure to dangerous levels of air quality by an estimated 2%.


**Project status update (last updated 27 March):**
- Carried out research-driven advanced EDA
- Built and optimized ARIMA model, and built SARIMA model
- Hyperparameter optimization for SARIMA model
- Sprint 2 presentation added to the repository

**Next steps:**
- Forecasting using linear regression
- Adding external factors to improve model accuracy
- Extend EDA with external factors

The notebooks in this repository are:

- 01a - Data Loading and Cleaning
- 01b - Data Loading and Cleaning: New variables (not added yet)
- 02 - Data Exploration
- 03 - ARMA models and pre-processing
- 04 - Linear regression model
- 04 - Findings (not added yet)

The following files are required to run the notebooks:

- data folder: this contains all the data files in .csv format
- requirements.txt: this contains the list of required packages for the environment
- functions.py: this contains the custom functions used in the notebook (added, but not operational yet)