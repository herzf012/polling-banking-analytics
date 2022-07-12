# ----------Set-up----------

# Import relavent modules

import os
import csv

# Set csv path and pull data to work with

election_csv = os.path.join("Resources", "election_data.csv")

ballot_id_dict = {}
ballot_id_list = []
county_list = []
candidate_list = []

with open(election_csv, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        ballot_id_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])
        ballot_id_dict[row[0]] = [row[1], row[2]]

# ----------Analysis----------

# Calculate total number of votes

total_votes = len(ballot_id_list)

# Create list of unique candidates

candidate_list_unique = []

old_candidate = ""
for new_candidate in candidate_list:
    if (new_candidate != old_candidate) & (new_candidate not in candidate_list_unique):
        candidate_list_unique.append(new_candidate)
        old_candidate = new_candidate

# Calculate amount of votes each candidate won

candidate_total_votes_dict = {}

for i in candidate_list_unique:
    candidate_total_votes_dict[i] = 0

voted_for = ""
for id in ballot_id_list:
    voted_for = ballot_id_dict[id][1]
    candidate_total_votes_dict[voted_for] += 1

# Calculate percentage of votes each candidate won

candidate_percentage_votes_dict = candidate_total_votes_dict

for i in candidate_list_unique:
    candidate_percentage_votes_dict[i] = candidate_total_votes_dict[i] / total_votes

# Determine winner of election

winner = ""
max_votes = 0

for i in candidate_list_unique:
    if candidate_total_votes_dict[i] > max_votes:
        winner = i
        max_votes = candidate_total_votes_dict[i]

print(winner)







