# Import data csv file
import os
import csv

# Assigning variables
totalMonths = 0
total_PL = 0
value = 0
change = 0
dates = []
profits = []

# Open and read the raw data file
with open("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # First line is header which is ignored
    csv_header = next(csvreader)

    # Read line after header and initialize variables
    firstRow = next(csvreader) 
    total_PL += int(firstRow[1])
    value = int(firstRow[1])
    totalMonths = 1

    for row in csvreader:
        totalMonths = totalMonths + 1
        dates.append(row[0])

        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        total_PL = total_PL + int(row[1])

        max_increase = max(profits)
        max_index = profits.index(max_increase)
        max_date = dates[max_index]

    # Greatest decrease (lowest increase) in profits 
    max_decrease = min(profits)
    worst_index = profits.index(max_decrease)
    worst_date = dates[worst_index]

    # Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

# Display results
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: ${str(total_PL)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {max_date} (${str(max_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(max_decrease)})")

# Output to .txt file
output = open("Bimi_budget.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(totalMonths)}")
line4 = str(f"Total: ${str(total_PL)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {max_date} (${str(max_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(max_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
