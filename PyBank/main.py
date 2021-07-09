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

# Calculate total number of months & net amount of Profit/Losses
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Loop through the data
    for row in csvreader:
        
        # Calculate total number of months 
        total_months += 1
        
        # Calculate net amount of "Profit/Losses" 
        net_amount += int(row[1])

        # Calculate change between the months
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

         # Calculate the average change 
        average_change = sum(monthly_change)/ len(monthly_change)
        highest = max(monthly_change)
        lowest = min(monthly_change)
        
        # Calculate greatest increase in profits
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate greatest decrease in profits
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
# Print analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Specify file to write to
analysis_output_file = os.path.join('.', 'analysis', 'budget_data_analysis.text')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(analysis_output_file, 'w',) as txtfile:

# Write the first row (column headers)
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
# Write all remaining rows 
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
