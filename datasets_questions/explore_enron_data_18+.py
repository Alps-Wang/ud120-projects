import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### Reverse First name and Last Name to Last + First 
# name1 = "James Prentice"
# name1 =name1.upper()
# ## print name1

# name1_split = name1.split(' ')
# name1 = name1_split[1] +' '+ name1_split[0]

##print name1


### get all features 
# for key in enron_data["SKILLING JEFFREY K"].keys():
# 	print key

# salary
# to_messages
# deferral_payments
# total_payments
# exercised_stock_options
# bonus
# restricted_stock
# shared_receipt_with_poi
# restricted_stock_deferred
# total_stock_value
# expenses
# loan_advances
# from_messages
# other
# from_this_person_to_poi
# poi
# director_fees
# deferred_income
# long_term_incentive
# email_address
# from_poi_to_this_person



### define function to get feature value for given person
def getFeatureValue(name, feature):
	name = name.upper()
	name_split = name.split(' ')
	if len(name_split) == 3 :
		#if name_split[1] < 3:
		name = name_split[2] +' '+ name_split[0] +' '+ name_split[1]
		print name 
	elif len(name_split) == 2:
		name = name_split[1] +' '+ name_split[0]
		print name
	print enron_data[name][feature]


### Quiz 18
# getFeatureValue("James Prentice","total_stock_value")
### 1095040

### Quiz 19 
#getFeatureValue('Wesley Colwell','from_this_person_to_poi')
###11

## Quiz 20
#getFeatureValue('Jeffrey K Skilling','exercised_stock_options')

# name2 = 'Jeffrey K Skilling'
# name2 = name2.upper()
# name2_split= name2.split(' ')
# print len(name2_split)
# name2 = name2_split[2] +' '+ name2_split[0] +' '+ name2_split[1]
# print name2

# print enron_data[name2]['exercised_stock_options']


# for name in enron_data.keys():
# 	if enron_data[name]["poi"] == 1:
# 		print name


##for k, v in enron_data.iteritems(): if k in mykeys

# ## quiz 25
# keys_3 = ["SKILLING JEFFREY K","LAY KENNETH L","FASTOW ANDREW S"]

# for name in enron_data.keys():
# 	if name in keys_3:
# 		print enron_data[name]['total_payments'], name

# quiz 27 
# count_salary = 0
# count_email = 0
# for name in enron_data.keys():
# 	if enron_data[name]['salary'] <> 'NaN':
# 		count_salary +=1
# 	if enron_data[name]['email_address'] <> 'NaN':
# 		count_email += 1

# print count_salary, count_email



