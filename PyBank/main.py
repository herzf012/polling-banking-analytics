# Import relavent modules

import os
import csv

# Set csv path and get it ready to be worked with

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        print(row[0])

