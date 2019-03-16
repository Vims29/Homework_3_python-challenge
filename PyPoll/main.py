# import the data csv file
import os
import csv

candidates = []
votes = []
#Percent = []

totalcount = 0

# Open csv file
with open("election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 
    # First line is header which is ignored
    csv_header = next(csvreader)
 
    # Calculate and format the percentage for candidates
    def percentage (part, whole):
        result = 100 * float(part)/float(whole)
        result = "%.3f%%" % result
        return result

    for i in csvreader:

        totalcount += 1
        # If candidate does not exist then add it to the candidate list and 
        # increment the vote count else just increment the vote count
        if i[2] not in candidates:
            candidates.append(i[2])
            position = candidates.index(i[2])
            votes.append(1)

        else:
            position = candidates.index(i[2])
            votes[position] += 1
       
# Combined the two statements below into a single statement
# winner = max(num_votes)
# index = num_votes.index(winner) 
winner = candidates[votes.index(max(votes))]

# Display Results
print(f" Election Results" + "\n")
print(f'---------------------------' + '\n')
print(f' Total Votes: {totalcount}'+'\n')
print(f'-------------------------------'+'\n')
for i in range(len(candidates)):
    print(f" {candidates[i]}: {percentage(votes[i],totalcount)} ({str(votes[i])})")
print(f'-------------------------------'+'\n')
print(" Winner: "   +  winner +"\n")
print('--------------------------------')

# Create the text file
output = open("Bimi_Election.txt", "w")
line1 = "Election Results"
line2 = "----------------------"
line3 = str(f"Total Votes: {str(totalcount)}" + "\n")
output.write('{}\n{}\n{}\n'.format(line1, line2, line3))
for i in range(len(candidates)):
    line = str(f'{candidates[i]}: {percentage(votes[i],totalcount)} ({str(votes[i])})')
    output.write('{}\n'.format(line))
line1 = "----------------------" 
line2 = " Winner: " + winner
line3 = "----------------------" 
output.write('{}\n\n{}\n\n{}'.format(line1, line2, line3))





    
   