# Disaster Response Pipeline

## Project Details

This project is a web app to classifying messages. During a disaster this app will help people to classify messages correctly and take the correct actions. 

### 1. ETL Process

In a first step data is merged and cleaned. Finally a clean dataset is stored.

### 2. Training Model

In a second step a model is trained on the data to classify future messages.

### 3. Run the Web App

Finally, the model is deployed to that messages can be classified online.


## Data Pipelines: Python Scripts

The archive has the following structure:

app
| - template
| |- master.html # main page of web app
| |- go.html # classification result page of web app
|- run.py # Flask file that runs app
data
|- disaster_categories.csv # data to process
|- disaster_messages.csv # data to process
|- process_data.py
|- DisasterResponse.db # database to save clean data to
models
|- train_classifier.py
|- classifier.pkl # saved model
README.md

The following commands need to be run in the corresponding folders to set up the database and train the model.

The ETL pipeline cleans the data and stores it in a database:

`python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db`

The ML pipeline trains the classifier and saves the model

`python train_classifier.py ../data/DisasterResponse.db classifier.pkl`

To run the Flask App

`python run.py`

Furthermore to get the correct url of the app:
`env|grep WORK`

The url then looks like this:
`https://SPACEID-3001.SPACEDOMAIN`

## Review

The reviewer recommended hosting the project in the cloud:
* https://www.heroku.com/
* 
Useful References:
* [Successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
* [5 types of git workflows](https://buddy.works/blog/5-types-of-git-workflows)
* [Python Docstrings](https://www.geeksforgeeks.org/python-docstrings/)
* [Docstring vs Comments](https://stackoverflow.com/questions/19074745/docstrings-vs-comments)
* [How to write a good readme for your github project?](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
* [Anatomy of a Readme File](https://classroom.udacity.com/courses/ud777/lessons/5338568539/concepts/53317786160923)
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [10 Useful Python Data Visualization Libraries for Any Discipline](https://blog.modeanalytics.com/python-data-visualization-libraries/)
* [5 Quick and Easy Data Visualizations in Python with Code](https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f)
* [The Best Python Data Visualization Libraries](https://www.fusioncharts.com/blog/best-python-data-visualization-libraries/)
