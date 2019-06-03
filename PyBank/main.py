import csv

#Part 1: Get total number of months
total_num_months = 0 #Total number of months in the dataset
file = 'Resources/budget_data.csv'
with open(file,) as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        total_num_months +=1
print("total number of months: " + str(total_num_months))

#Part 2: Get total amount of "Profit/Losses".
#This requires that I split the array
included_cols = [2]  #ensure I get the second column from the csv file

for row in reader:
    content = list(row[i] for i in included_cols)
    print(content)
