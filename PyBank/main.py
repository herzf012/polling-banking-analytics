# Import relavent modules

import os
import csv

# Set csv path and pull data to work with.

budget_csv = os.path.join("Resources", "budget_data.csv")

budget_dict = {}
month_list = []
profit_losses_list = []


with open(budget_csv, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        month_list.append(row[0])
        profit_losses_list.append(int(row[1]))
        budget_dict[row[0]] = row[1]

print(profit_losses_list)

# Analysis
# Do analysis

