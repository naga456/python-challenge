import csv
included_cols = [1]  #ensure I get the second column from the csv file

#Part 1: Get total number of months
total_num_months = 0 #Total number of months in the dataset
total_profit = 0 #net total of Profit/Loss
total_diff = 0 #total of changes
change = 0
prev = 0
current = 0
file = 'Resources/budget_data.csv'
with open(file,) as f:
    reader = csv.reader(f)
    next(reader,None) #skip the headers
    for row in reader:
        #print(row)
        total_num_months +=1

        #Part 2: Get total amount of "Profit/Losses".
        #This requires that I split the array
        content = list(row[i] for i in included_cols)
        #print(content)
        #print(float(content[0]))
        total_profit = total_profit + int(content[0])
        
        #part 3
        prev = current
        current = int(content[0])
        if prev == 0:
            #do nothing
            change = 0
        else:  
            change = current - prev
        total_diff = total_diff + change
        #print(change)


print("total number of months: " + str(total_num_months))
print("Net Total Profit/Loss: " + str(total_profit))
print("Total differences are: " + str(total_diff))
print("Average change: " + str(total_diff/85))

