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


### size of enron_data
#print len(enron_data)
### 146

### how many featuers for each person
#print len(enron_data["SKILLING JEFFREY K"])
### 21

###Finding POIs in the Enron Data
# def countPoi(dict1):
# 	n = 0
# 	for i in dict1:
# 		if enron_data[i]["poi"] == 1:
# 			n += 1
# 	return n



# pio = countPoi(enron_data)

# print pio
###18

### names in poi_names.txt
poi_names_list = []
with open("../final_project/poi_names.txt", "r") as f:
	for line in f:
		if '(y)' in line or '(n)' in line:
			line = line.strip('\n').upper()
			fn = line.split(' ')[1].replace(',',' ') + line.split(' ')[2]
			poi_names_list.append(fn)

### names in enron_data
enron_name= []
person_name = []
person_inList =[]
person_not_inList =[]

for name in enron_data.keys():
	if enron_data[name]["poi"] == 1:
		
		name_split = name.split(' ')
		for n in name_split:
			if len(n) > 2:
				person_name.append(n)

		name = ' '.join(person_name)
		del person_name[:]

		enron_name.append(name)


# ### Poi ####
# HANNON KEVIN P
# COLWELL WESLEY
# RIEKER PAULA H
# KOPPER MICHAEL J
# SHELBY REX
# DELAINEY DAVID W
# LAY KENNETH L
# BOWEN JR RAYMOND M
# BELDEN TIMOTHY N
# FASTOW ANDREW S
# CALGER CHRISTOPHER F
# RICE KENNETH D
# SKILLING JEFFREY K
# YEAGER F SCOTT
# HIRKO JOSEPH
# KOENIG MARK E
# CAUSEY RICHARD A
# GLISAN JR BEN F
# SKILLING JEFFREY K

### enron_name, which is in poi_names_list		
for n1 in enron_name:
	if n1 in poi_names_list:
			#count +=1
			person_inList.append(n1) 



### names in poi_names_list, which are not in enron_name
for n2 in poi_names_list:
	if n2 not in enron_name:
			#count +=1
			person_not_inList.append(n2)


print len(enron_name)
#print enron_name

print len(poi_names_list)
#print poi_names_list

print len(person_inList)
#print person_inList

print len(person_not_inList)
#print person_not_inList
