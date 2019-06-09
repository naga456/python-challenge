import csv
import os

csvfile = "Resources/election_data.csv"
total_votes = 0
dict = {}
candidate = ""

def display():
    print("Election Results")
    print('-'*27)
    print(f'Total Votes: {total_votes}')
    print('-'*27)
    for r in results:
        votes=r[1]
        name = r[0]
        percentage = round((votes/total_votes)*100,3)
        print(f'{name}: {percentage}% ({votes})')
    print('-'*27)
    print(f'Winner: {results[0][0]}')
    print('-'*27)

    outfile = 'output.txt'
    file=open(outfile,'w')
    file.write("Election Results" +'\n')
    file.write('-'*27 +'\n')
    file.write(f'Total Votes: {total_votes} \n')
    file.write('-'*27 +'\n')
    for r in results:
        votes=r[1]
        name = r[0]
        percentage = f'{(votes/total_votes)*100:3f}'
        file.write(f'{name}: {percentage}% ({votes}) \n')
    file.write('-'*27 +'\n')
    file.write(f'Winner: {results[0][0]} \n')
    file.write('-'*27 +'\n')
    file.close()



with open(csvfile,'r') as file:
    reader = csv.reader(file,delimiter=',')
    next(reader,None)
    for row in reader:
        candidate = row[2]
        if candidate in dict:
            dict[candidate] +=1
        else:
            dict[candidate] = 1

###Get total
for key in dict:
    total_votes = total_votes + dict[key]

###Sort dict
from operator import itemgetter
results = sorted(dict.items(), key=itemgetter(1), reverse=True)
print(results)

###Display to terminal
display()

###Write to file

#print(sorted(dict.values(), reverse=True))



