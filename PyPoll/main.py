import os
import csv

# Assign variables and values
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Path to collect data from resources folder
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Read the CSV file
with open(csvpath, newline='') as csvfile:

    # Import the CSV reader and split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read header row 
    csv_header = next(csvfile)

