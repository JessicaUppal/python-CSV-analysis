import os
import csv

# Assign variables and their values
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Path to collect data from the Resources folder
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Read the CSV file
with open(csvpath, newline='') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    row = next(csvreader)


# Calculate Total Number Of Months & Net Amount Of Profit/Losses
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Loop through the data
    for row in csvreader:
        
        # Calculate Total Number Of Months 
        total_months += 1
        # Calculate Net Amount Of "Profit/Losses" Over The Entire Period
        net_amount += int(row[1])

        # Calculate change between the months
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

    