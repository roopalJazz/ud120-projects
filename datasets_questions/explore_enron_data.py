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
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "Data points:", len(enron_data)
print "Features:", len(enron_data[enron_data.keys()[0]])

c_poi=0;

for name,i in enron_data.iteritems():
	if i['poi']:
		c_poi+=1;       
print "POI in Dataset:", c_poi

print "Stock value of James Prentice:", enron_data["PRENTICE JAMES"]['total_stock_value']
print "Wesley Colwell to POI emails:", enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print "Stock options of Jeffrey Skilling:", enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

enron_keyPOIPayment = dict((k,enron_data[k]['total_payments']) for k in ("LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"))
max_earner = max(enron_keyPOIPayment, key=enron_keyPOIPayment.get)
print "Largest total payment earner and payment:", max_earner, enron_keyPOIPayment[max_earner]

salaries_available = 0
emails_available = 0
total_payments_unavailable = 0
total_payments_unavailable_poi = 0
for name in enron_data:
    if not np.isnan(float(enron_data[name]['salary'])):
        salaries_available += 1
    if enron_data[name]['email_address'] != "NaN":
        emails_available += 1
    if np.isnan(float(enron_data[name]['total_payments'])):
        total_payments_unavailable += 1
        if enron_data[name]['poi']:
            total_payments_unavailable_poi += 1
        
    
print "Salaries available:", salaries_available
print "Emails available:", emails_available
print "NaN for total payment and percentage:", total_payments_unavailable, float(total_payments_unavailable)/len(enron_data)*100
print "NaN for total payment of POI and percentage:", total_payments_unavailable_poi, float(total_payments_unavailable_poi)/c_poi*100

"""
Results

Data Points:146
Features: 21
POI in dataset: 18
Stock Value of James Prentice: 1095040
Wesley Colwell to POI emails:11
Stock Options of Jeffrey Skillings:19250000
Largest total payment earner and payment: LAY KENNETH L
Salaries Available: 95
Emails Available:111
NaN for total payment and percentage:: 21 14.3835616438
NaN for total payment of POI and percentage: 0 0.0

"""

