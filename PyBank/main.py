# ----------Set-up----------

# Import relavent modules

import os
import csv

# Set csv path and pull data to work with

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

# ----------Analysis----------

# Total months looked at

total_months = len(month_list)

# Net total amount of "Profit/Losses"

total_net_amount = 0

for i in profit_losses_list:
    total_net_amount += i

# Changes in "Profit/Losses"

delta_profits_losses_list = []
average_delta = 0
sum_of_deltas = 0

count = 1
while count < len(profit_losses_list):
    delta = profit_losses_list[count] - profit_losses_list[count - 1]
    delta_profits_losses_list.append(delta)
    count += 1

for i in delta_profits_losses_list:
    sum_of_deltas += i

average_delta = sum_of_deltas / len(delta_profits_losses_list)

# Greatest increase and decrease in profits

max_delta = max(delta_profits_losses_list)
max_delta_index = delta_profits_losses_list.index(max_delta)
max_delta_date = month_list[max_delta_index + 1]

min_delta = min(delta_profits_losses_list)
min_delta_index = delta_profits_losses_list.index(min_delta)
min_delta_date = month_list[min_delta_index + 1]

# ----------Output----------

# Put results in a list

results_list = ["Financial Analysis", "----------------------------",
f"Total months: {total_months}", f"Total: ${total_net_amount}",
f"Average Change: ${round(average_delta, 2)}", 
f"Greatest Increase in Profits: {max_delta_date} (${max_delta})",
f"Greatest Decrease in Profits: {min_delta_date} (${min_delta})"]

# Print results to terminal

for i in results_list:
    print(i)

# Export results as a text file to analysis

results_file = os.path.join("analysis", "results.txt")

with open(results_file, "w") as txtfile:
    for i in results_list:
        txtfile.write(i)
        txtfile.write("\n")
