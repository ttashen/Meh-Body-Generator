# Meh-Meh-Interesting

## Introduction
This project’s goal is to categorizing Meh’s deals and analyze each category’s sales
performance. Meh.com is a discount retail website that only provides one deal per day. The
deals range from useful tech items like Roomba vacuuming robots, to a box of junk that you
would never need, like Sharp Things In A Box. In addition to a detailed sales pitch, the website
reports a variety of information such as page hits and revenue that are featured in my analysis.

## Pipeline and Methodology

### Web Scraping: 
Collect the features of everyday’s deal, including product descriptions, sales
pitch, sales statistics, and user poll statistics.
Data cleaning and feature engineering: Create new features like price, conversion rate, and
dislikes vs. sales ratio; drop largely unpopulated features

### Natural language processing: 
To create additional features for clustering and analysis, I
implement natural language processing techniques to the description and sales pitch which
includes cleaning and extracting meaningful text content, as well as applying TFIDF-vectorizer
on meaningful words.

### Clustering: 
Apply Principle Components Analysis to reduce dimension on TFIDF-vectors; use
kmeans clustering algorithm to divide all deals into reasonable categories.
Anova testing: In order to test if there’s significant difference between categories, I used oneway
anova test; and then apply Tukey’s HSD Post-hoc comparison to further investigate which
categories outperforms others.

## Results
# The unreasonable outliers: 
While I was looking for a sales performance indicator, I first used the conversion rate, which is number of sales divided by number of page visits. But there is a surprising amount of cases early in the website’s history where this ratio is over 1, with a maximum that is over 53. The reason for this is unclear, but most likely the website’s visits counter was not very accurate when the website first launched. 

# Refferals:
The website keeps track of the traffic that were directed from other websites. But it looks like these refferals (ex. facebook) are not contributing to sales very much. 

![alt text](https://raw.githubusercontent.com/ttashen/Meh-Meh-Interesting/master/pics/facebook_referral.png)

# Exceptional Sales:
In the plot of the sales trend along time, there are a few spikes indicating exceptional sales. These are the days when meh broke their rules of one deal per day. Instead, the website updated a new deal every few hours. This strategy might be useful to increase sales. But more data will be needed to confirm the hypothesis.

![alt text](https://raw.githubusercontent.com/ttashen/Meh-Meh-Interesting/master/pics/time_series.png)

# Categories:
The clustering algorithm successfully placed the deals into categories, among which the best identified ones are Audio, tech/smart devices, kitchen, knives, camera/drones, power banks/lights.

# More sales from power banks/lights: 
Among the categories from clustering, only the power_banks/lights category has statistically significant better sales. So keep them coming!

![alt text](https://raw.githubusercontent.com/ttashen/Meh-Meh-Interesting/master/pics/boxplot.png)
