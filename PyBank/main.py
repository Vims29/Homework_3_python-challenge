# import data/csv
import os
import csv
budget_Data = os.path .join("..", "Resources", "budget_data.csv")

#open csv
with open(budget_Data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=" ")
    print(f"Header:: {csv_header}")
    
# Lists  to store data
total_months = []
total_profit =[]

