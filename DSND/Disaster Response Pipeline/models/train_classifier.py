import sys

import pandas as pd

from sqlalchemy import create_engine

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet') # download for lemmatization

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report, hamming_loss

import pickle

def load_data(database_filepath):
    """loads data from given database"""
    
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table("messages", con=engine)
    X = df['message']
    Y = df.iloc[:, 4:]

    # Get the label names
    category_names = list(Y.columns)

    return X, Y, category_names

def tokenize(text):
    """Tokenize and lemmatize each word in a given text"""
    
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    tokens_lemmatizer=[]
    for token in tokens:
        tokens_lemmatizer.append(lemmatizer.lemmatize(token).lower().strip())
        
    return tokens_lemmatizer


def build_model():
    """Create a machine learning pipeline"""
    
    pipeline = Pipeline([
            ('vec', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer()),
            ('clf', MultiOutputClassifier(RandomForestClassifier(n_estimators = 100, n_jobs = 6)))
        ])
    
    parameters = {'clf__estimator__max_features':['sqrt', 0.5],
                  'clf__estimator__n_estimators':[20, 50]}

    cv = GridSearchCV(estimator=pipeline, param_grid = parameters, cv = 5, n_jobs = 6)

    return pipeline

def evaluate_model(model, X_test, Y_test, category_names):
    """Generates report of model"""
    
    Y_pred = model.predict(X_test)
    for idx, column in enumerate(category_names):
        print(column)
        print(classification_report(Y_test[column], Y_pred[:,idx]))


def save_model(model, model_filepath):
    """Saves model"""
    
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()