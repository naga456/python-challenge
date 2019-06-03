import csv
included_cols = [1]  #ensure I get the second column from the csv file

#Part 1: Get total number of months
total_num_months = 0 #Total number of months in the dataset
total_profit = 0 #net total of Profit/Loss
file = 'Resources/budget_data.csv'
with open(file,) as f:
    reader = csv.reader(f)
    next(reader,None) #skip the headers
    for row in reader:
        #print(row)
        total_num_months +=1
        content = list(row[i] for i in included_cols)
        #print(content)
        #print(float(content[0]))
        total_profit = total_profit + int(content[0])
print("total number of months: " + str(total_num_months))
print("Net Total Profit/Loss: " + str(total_profit))

#Part 2: Get total amount of "Profit/Losses".
#This requires that I split the array
