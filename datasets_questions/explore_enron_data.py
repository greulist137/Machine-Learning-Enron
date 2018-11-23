#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#Print how many rows we have in the data set
print('Number of rows: ')
print(len(enron_data))

#print how many features are there for each row
max_count = 0
print('Features: ')
for key,value in enron_data.items():
    temp_count = len(list(filter(bool, value)))
    if max_count < temp_count:
        max_count = temp_count

print(max_count)

#Print out how many people are labeled as a Person of Interest (POI)
for key,value in enron_data.items():   
    if max_count < temp_count:
        max_count = temp_count

print('Number of people labeled as a POI: ')

