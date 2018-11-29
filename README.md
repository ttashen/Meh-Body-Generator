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
The unreasonable outliers: While I was looking for a sales performance indicator, I first used
the conversion rate, which is number of sales divided by number of page visits. But there is a
surprising amount of cases early in the website’s history where this ratio is over 1, with a
maximum that is over 53. The reason for this is unclear, but most likely the website’s visits
counter was not very accurate when the website first launched.
The unlucky bags: From the plot of conversion rates along time, the large spike (Fig 1) caught
my eye. After further investigation, I discovered that the whole month of April in 2016, the
website only sold one product, the unlucky bags as April fool’s day joke. How ridiculous!
More sales from power banks/lights: Among the categories from clustering, only the power/
lights category has statistically significant better sales (Fig 2). So keep them coming!
