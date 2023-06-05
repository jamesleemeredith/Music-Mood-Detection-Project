# Music Mood Detection Using Spotify Audio Features

**Authors:** James Meredith
***

## Overview

The purpose of this Data Science project was to develop an automated Machine Learning model for the detection of a song's dominant mood based on it's audio features. The impetus behind conception of this project was to create a way for the Spotify recommendation system to implement mood-based contextual recommendation into the current recommendation system. The current recommendation system does a pretty good job of utilizing users past listening habits to recommend them songs they enjoy, but it lacks the context specificity to recommend songs appropriate to a user’s given mood. For example, I don’t want Spotify to include sad songs in my recommended playlist when I’m at the gym, or fast-paced techno music when I’m trying to fall asleep. So the goal of this project was to create an automated mood detection algorithm to be integrated into the current recommendation system, so users could simply say “Hey Spotify! Build me a playlist that matches my mood right now.” and Spotify does it. Song data was compiled from the Spotify API and emotion data used to train the model came from Last.FM user-generated tags. The data was then used to train a machine learning algorithm in order to build the detection model.  The logistic regression model had an accuracy score of 0.54. The decision tree model was also able to predict the dominant mood of a song with a 0.45 accuracy score. After tuning both models further, the decision tree model was able to achieve an accuracy score of 0.85, and the logistic regression model was able to achieve an accuracy score of 0.55. The decision tree model was also able to predict the dominant mood of a song with a 0.46 accuracy score. Based on the analysis, the author recommends the use of audio feature data to predict the dominant mood of a song. The author also recommends the use of a decision tree model to predict the dominant mood of a song based on it's audio features. The author does not recommend the use of a logistic regression model to predict the dominant mood of a song based on it's audio features.

## Business Problem

Spotify currently offers a robust recommendation system whereby users receive recommendations for music they might like based on their past listening habits. However, Spotify does not currently offer a feature whereby users can request music based on their current mood. The purpose of this project is to develop a model that can predict the dominant mood of a song based on it's audio features, and then to use that model to develop a recommendation system for users to request music based on their current mood. The target audience for this project is Spotify, and the goal is to develop a model that can be integrated into the current recommendation system to allow users to request music based on their current mood.

## Data

Song data was compiled using a dataset derived from the Spotify API. The database contained of over 1700 songs, and features mood data from Last.FM user-generated tags.

## Methods

Songs were tagged with one of 4 moods: happy, sad, angry, and calm. The data was then split into a training set and a test set, with the training set containing 80% of the data, and the test set containing 20% of the data. The training set was used to train the model, and the test set was used to test the model. The data was then used to train a machine learning algorithm in order to build the detection model. The detection model was created using an iterative approach that compared the accuracy and efficiency of several different machine learning models against a baseline dummy model. Pipelines were used to efficiently process the data for each model. The models were then tuned using GridSearchCV to find the optimal hyperparameters for each model. The models were then evaluated using accuracy scores and confusion matrices.

## Results

Results of the baseline dummy model showed an accuracy score of 0.25. A quick comparison of 9 potential alternative models was conducted, where it was revealed that decision trees, gradiant boosting, and random forest algorithms were the top 3 models by accuracy. Cross-validated accuracy scores and confusion matrices for each of the four models is displayed below:

### Cross-Validated Accuracy Scores for Baseline Dummy Model:
![Baseline Dummy Model Accuracy Scores](./images/dummy_model_cv_results.png)

### Confusion Matrix for Baseline Dummy Model:
![Baseline Dummy Model Confusion Matrix](./images/baseline_dummy_cm.png)

### Cross-Validated Accuracy Scores for Baseline Decision Tree Model:
![Baseline Decision Tree Accuracy Scores](./images/baseline_dt_cv_results.png)

### Confusion Matrix for Baseline Decision Tree Model:
![Baseline Decision Tree Confusion Matrix](./images/baseline_dt_cm.png)

### Cross-Validated Accuracy Scores for Baseline Gradient Boosting Model:
![Baseline Gradiant Booting Accuracy Scores](./images/baseline_gb_cv_results.png)

### Confusion Matrix for Baseline Gradient Boosting Model:
![Baseline Gradiant Booting Confusion Matrix](./images/baseline_dt_cm.png)

### Cross-Validated Accuracy Scores for Baseline Random Forest Model:
![Baseline Random Forest Accuracy Scores](./images/baseline_rf_cv_results.png)

### Confusion Matrix for Baseline Random Forest Model:
![Baseline Random Forest Confusion Matrix](./images/baseline_rf_cm.png)

Based on the results of the baseline models, the decision tree model was selected for further tuning. The decision tree model was tuned using GridSearchCV to find the optimal hyperparameters for the model. The tuned model was then evaluated using accuracy scores and a confusion matrix.

### Cross-Validated Accuracy Scores for Tuned Decision Tree Model:
![Tuned Decision Tree Accuracy Scores](./images/tuned_rf_cv_results.png)

### Confusion Matrix for Tuned Decision Tree Model:
![Tuned Decision Tree Confusion Matrix](./images/tuned_rf_cm.png)

## Conclusions

Based on the analysis, the author recommends the use of audio feature data to predict the dominant mood of a song. Due to the ease and accuracy of detecting the dominant mood of a song based on its audio features, the author recommends that Spotify integrate a mood detection model into their current recommendation system to allow users to request music based on their current mood. Limitations of the study include the use of user-generated tags to determine the dominant mood of a song, and the use of audio features that are proprietary to the Spotify API. Future work could include the use of a larger dataset, more audio features included in the analysis, the inclusion of more mood classes, sentiment analysis of song lyrics to strengthen model accuracy, and the use of a more robust model.

## For More Information

Please review the full analysis in [the Jupyter Notebook](./music_mood_detection_model.ipynb) or [the presentation](./presentation.pdf).

For any additional questions, please contact James Meredith at <jam637.jlm@gmail.com>.

## Repository Structure

```
├── data
├── images
├── .gitignore
├── README.md
└── music_mood_detection_model.ipynb
```