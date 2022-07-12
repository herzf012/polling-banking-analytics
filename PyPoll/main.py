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



