# Music Mood Detection Using Spotify Audio Features

**Authors**: James Meredith

## Overview

The purpose of this Data Science project was to develop an automated Machine Learning model for detections of a song's dominant mood based on it's audio features. Ultimately the use case for this project would be to pitch a new feature to Spotify where users can say "Hey Spotify, I'm feeling sad. Play me something sad" and then spotify would play them a song that's emotion is coded as sad. In terms of the project, ultimately I'm predicting that audio features of a song like it's key, rhythm, etc. will be highly correlated with it's dominant mood, and would be using the various audio features to run a logistic regression and compare it to decision trees. Audio features were derived from the Spotify API, and mood/emotion data was compiled using user-generated tags from Last.FM.

## Business Problem

Spotify currently offers a robust recommendation system whereby users receive recommendations for music they might like based on their past listening habits. However, Spotify does not currently offer a feature whereby users can request music based on their current mood. The purpose of this project is to develop a model that can predict the dominant mood of a song based on it's audio features, and then to use that model to develop a recommendation system for users to request music based on their current mood.

## Data

Song data was compiled using a dataset derived from the Spotify API. The database contained of over 90,000 recorded aviation accidents from 1921 to 2020. Emotion meta-data was compiled using user-generated tags from Last.FM. The data was then cleaned and merged into a single dataframe for analysis.

## Methods

Our analysis consisted of descriptive statistics, data visualization, and machine learning modeling. We used a logistic regression model to predict the dominant mood of a song based on it's audio features, and then compared the results to a decision tree model.

## Results

Baseline results of the model showed decision trees to be the superior model, with an accuracy score of 0.83. The logistic regression model had an accuracy score of 0.54. The decision tree model was also able to predict the dominant mood of a song with a 0.45 accuracy score. After tuning both models further, the decision tree model was able to achieve an accuracy score of 0.85, and the logistic regression model was able to achieve an accuracy score of 0.55. The decision tree model was also able to predict the dominant mood of a song with a 0.46 accuracy score.

### Confusion Matrix for Logistic Regression Model:
![Baseline Logistic Regression Confusion Matrix](images\baseline_logreg_cm.png)

### Confusion Matrix for Decision Tree Model:
![Baseline Decision Tree Confusion Matrix](images\baseline_dt_cm.png)

### Post-Tuning Confusion Matrix for Decision Tree Model:

### Post-Tuning Confusion Matrix for Logistic Regression Model:

## Conclusions

Based on the analysis, the author recommends the use of audio feature data to predict the dominant mood of a song. The author also recommends the use of a decision tree model to predict the dominant mood of a song based on it's audio features. The author does not recommend the use of a logistic regression model to predict the dominant mood of a song based on it's audio features.

## For More Information

Please review our full analysis in [our Jupyter Notebook](./full-analysis.ipynb) or [our presentation](./presentation.pdf).

For any additional questions, please contact James Meredith at <jam637.jlm@gmail.com>.

## Repository Structure

```
├── __init__.py
├── README.md
├── full-analysis.ipynb
├── presentation.pdf
├── code
│   ├── __init__.py
│   ├── visualizations.py
│   ├── data_preparation.py
│   └── eda_notebook.ipynb
├── data
└── images
```