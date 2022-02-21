# Hacklytics2022

<img src="media/logo.png" width = 200px height = 200px/>


This project was awarded `Best Healthcare Hack Powered by Anthem` for [Hacklytics 2022](https://hacklytics.io/), Georgia Tech’s 36 hour datathon.

Check out the [devpost submission](https://devpost.com/software/tbd-pc9f4d?ref_content=my-projects-tab&ref_feature=my_projects)

## About

This is an app that allows anyone to view insights into their health risks based on their age, gender, and location. The app then provides a score which recommends them to get insurance.

## Inspiration
Selecting a health insurance plan that is right you is a big decision.  With the cost of health insurance, most Americans question if it is worth keeping their insurance. We wanted to use our analytical skills to inform users of the risks they may be exposed to depending on their location, age, gender, and race. By visualizing potential health liabilities specific to their demographic, we hope that users can make a more informed decision on the type of insurance they should consider purchasing. General information on the types of health insurance in summarized at the bottom of the webapp. We hope this will help users navigate to the right insurance package in today's complicated healthcare system. Data is everywhere, and it can tell us a lot about the risks that are present in today's world.  Our app analyzes that data to inform you about the healthcare risks you might face in your daily life. 

## What it does

Ensurance is a web app that allows anyone to view insights into general health risks based on their age, gender, location, and race. The app then summarizes more information for getting insurance. Additionally our app can provide sentiment analysis on the user's thoughts on health insurance. 

## How we built it
- Initially we started with a brainstorming session for gathering the potential datasets 
- We performed data cleaning and analysis in Python with Pandas, made visualizations with Plotly, and collaborated on a shared Python notebook using Deepnote. 
- To host the app, we used Streamlit, an amazing tool for building web apps. This was used on Visual Studio Code, where we were able to code concurrently with the use of Live Share. 
- We also utilized Google Cloud Product for sentiment analysis to gauge what the user feels towards health insurance.

## Challenges we ran into

One of the challenge with this app was collecting the data we needed. A lot of data we found online either required payment or were not available. With the limited amount of data available, we had to make some assumptions and generalize data to a bigger population. For example, the infectious disease dataset was for Californian residents, but we generalized it to the US.
Another issue was the waiting time when requesting APIs. Some requests had a long queue, which was too much waiting time. We wanted to included some recommendations for health insurance plans using Vericred API, however we were on the waiting list and the approval is not yet given. Since we only had one and a half days to complete the hackathon.

## What we're proud of

We are proud to have built the app in one and a half days. We spent Friday night brainstorming and searching for datasets, and the entire Saturday coding our ideas. We're also proud to have worked as a team, especially since half of us are in opposite timezones.

## What we learned

- We learned more about healthcare related data and about how different demographics affect health.
- We also learned more about using Plotly and building a data product for people to use.
- Coding-wise, we discovered great ways to collaborate and code concurrently (Deepnote and Live Share on VSCode). This was far more efficient than relying on GitHub and fixing merge conflicts.

## What's next for Ensurance

- To use our sentiment analysis tool to receive reviews on specific types of insurance packages. Should this app be used by a company, this would be a good way to identify the pros and cons of insurance that the company has to offer.
- To update the webapp with more visualizations should we have access to more detailed datasets in the future.
- To build a recommendation system for insurance plans by collecting the data from Vericred API (once we are approved for the account by Vericred)
- To develop a model that will predict healthcare risk score based on user's demographics 

## Tech Stack

- Python (Pandas, Plotly)
- Streamlit for building the web app
- Deepnote for visualizations [Notebook](https://deepnote.com/project/hacklytics-visualizations-Sn_4dKBpSAmWjBx19STlQg/%2Fnotebook.ipynb)
- Google Cloud Product for sentiment analysis

## Datasets used

- Datasets we used

1. COVID-19 data by the New York Times
   - <https://github.com/nytimes/covid-19-data>
2. COVID-19 and Influenza Reported Patient Impact and Hospital Capacity by State by HealthData.gov
   - <https://beta.healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/g62h-syeh>
3. Infectious Disease 2001-2014 - dataset by health by data.world
   - <https://data.world/health/infectious-disease-2001-2014>
4. Web-based Injury Statistics Query and Reporting System by Injury Center|CDC
   - <https://www.cdc.gov/injury/wisqars/index.html>
5. Delay or nonreceipt of needed medical care during the past 12 months due to cost by Centers for Disease Control and Prevention
   - <https://data.cdc.gov/NCHS/Delay-or-nonreceipt-of-needed-medical-care-prescri/dmzy-x2ad>)

## Team members

- Benedict Neo
- Pravallika Myneni
- Andrew Schaefer
- Aastha Naik


