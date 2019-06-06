import csv
included_cols = [0,1]  #ensure I get the second column from the csv file

#Part 1: Get total number of months
total_num_months = 0 #Total number of months in the dataset
total_profit = 0 #net total of Profit/Loss
total_diff = 0 #total of changes
change = 0
prev = 0
current = 0
increase_date = ""
greatest_increase = 0
decrease_date = ""
greatest_decrease = 0
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
        total_profit = total_profit + int(content[1])
        
        #part 3
        prev = current
        current = int(content[1])
        if prev == 0:
            #do nothing
            change = 0
        else:  
            change = current - prev
        total_diff = total_diff + change
        #print(change)

        #part 4
        date = content[0]
        increase = int(content[1])
        decrease = int(content[1])        
        if greatest_increase == 0:
            increase_date = date
            greatest_increase = increase
        elif not(greatest_increase > increase):
            increase_date = date
            greatest_increase = increase
        
        if greatest_decrease == 0:
            decrease_date = date
            greatest_decrease = decrease
        elif not(greatest_decrease < decrease):
            decrease_date = date
            greatest_decrease = decrease
        #increase = content[1]
        #decrease = content[1]
        



average_change = total_diff/85
print("Total Months: " + str(total_num_months))
#print("Net Total Profit/Loss: " + str(total_profit))
print(f'Total: ${total_profit}')
#print("Total differences are: " + str(total_diff))
#print("Average change: " + str(total_diff/85))
#print(f'Average Change: ${:.2f}'.format(average_change))

print('Average Change: ${:.2f}'.format(average_change))

print(f'Greatest Increase in Profits: {increase_date} (${greatest_increase})')
#print(greatest_increase)
#print(increase_date)
print(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})')