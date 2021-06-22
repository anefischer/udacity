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

