"""
Graham Harris
Summer Data Project
Transforms data into a adjacency lists for easy network visualization. Does NOT run with command line arguments.
"""

import timeit

# -------------- METHODS --------------

# Converts CSV to a 2D/nested Python list structure.
def csv_to_list(path):
  fd = open(path, "r")
  fd.readline() # get rid of title line
  rc = []
  for line in fd:
    line = line.lower() # make sure all casing is the same
    line = line.split(",")
    rc.append(line)
  fd.close()
  return rc

# Creates nested list of people/orgs from affinity
def create_adjacency(path):
  fd = open(path, "r")
  rc = []
  for line in fd:
    line = line.lower() # all casing the same
    line = line.strip("\n")
    # {Name: List of Events, 2018-2019, 2019-2020, 2020-2021}
    item = {line: [
      ["Coaching",                    0, 0, 0],
      ["Startup School",              0, 0, 0],
      ["Female Founders",             0, 0, 0],
      ["HTSAS",                       0, 0, 0],
      ["Bootcamp Applications",       0, 0, 0],
      ["January Sprint Applications", 0, 0, 0],
      ["Summer Sprint Applications",  0, 0, 0],
      ["SLP Applications",            0, 0, 0]
      ]}
    rc.append(item)
  fd.close()
  return rc

# Eliminates anyone who didn't come to anything
def filter_zeros(all_list):
  rc = []
  for dict in all_list:
    counter = 0
    # Count number of events attended
    nested_list = dict.values()
    for list in nested_list:
      for inner in list:
        for i in range(1, len(inner)):
          counter += inner[i]
    if counter != 0:
      rc.append(dict)
  return rc

# Computes the proper weight of the adjacency by counting number of instances
def add_adjacency(item, name, dataset, csv_index, count_index):
  counter = 1
  for file in dataset: # For year in set of years
    for line in file: # Scan all lines
      if line[csv_index] == name: # If the name matches
        item[name][count_index][counter] += 1
    counter += 1
  return item

# Computes a 0/1 adjacency by counting number of instances
def binary_adjacency(item, name, dataset, line_index, count_index):
  counter = 1
  for file in dataset: # For year in set of years
    for line in file: # Scan all lines
      if line[line_index] == name: # If the name matches
        item[name][count_index][counter] = 1
    counter += 1
  return item

# Prints adjacency lists to CSVs in readable format
def print_adj(all_item, adj_macro, adj_list, adj_simple):
  for item in all_item:
    person = item.values()
    name = sorted(item)[0]
    for event in person:
      for event_year in event:
        count = 0
        for i in range(1, len(event_year)):
          if event_year[i] == 0:
            continue
          count += event_year[i]
          adj_macro.write(name.title() + "," + event_year[0] + " " + str(2018 + i) + "," + str(event_year[i]) + "\n")
          adj_list[i-1].write(name.title() + "," + event_year[0] + " " + str(2018 + i) + "," + str(event_year[i]) + "\n")
        if count == 0:
          continue
        adj_simple.write(name.title() + "," + event_year[0] + "," + str(count) + "\n")

# -------------- OPEN FILES --------------

# Files to print to
teams_adj = open("../data/adjacent_teams.csv", "w")
people_adj = open("../data/adjacent_people.csv", "w")
simplified_teams_adj = open("../data/simplified_adjacent_teams.csv", "w")
simplified_people_adj = open("../data/simplified_adjacent_people.csv", "w")
teams_2019 = open("../data/2019_teams.csv", "w")
teams_2020 = open("../data/2020_teams.csv", "w")
teams_2021 = open("../data/2021_teams.csv", "w")
people_2019 = open("../data/2019_people.csv", "w")
people_2020 = open("../data/2020_people.csv", "w")
people_2021 = open("../data/2021_people.csv", "w")
adj = [teams_adj, people_adj, simplified_people_adj, simplified_teams_adj, teams_2021, teams_2020, teams_2019, people_2021, people_2020, people_2019]
for a in adj:
  a.write("Source,Target,Weight\n")
teams_list = [teams_2019, teams_2020, teams_2021]
people_list = [people_2019, people_2020, people_2021]

# Affinity nested lists
all_people = create_adjacency("../../affinity/all_people.csv")
all_orgs = create_adjacency("../../affinity/all_organizations.csv")

# Coaching
coaching_2019 = csv_to_list("../../coaching/csv/2018_2019_coaching.csv")
coaching_2020 = csv_to_list("../../coaching/csv/2019_2020_coaching.csv")
coaching_2021 = csv_to_list("../../coaching/csv/2020_2021_coaching.csv")
coaching = [coaching_2019, coaching_2020, coaching_2021]

# Female Founders
ff_2019 = csv_to_list("../../eventbrite/female_founders_2019.csv")
ff_2020 = csv_to_list("../../eventbrite/female_founders_2020.csv")
ff_2021 = csv_to_list("../../eventbrite/female_founders_2021.csv")
ff = [ff_2019, ff_2020, ff_2021]

# Startup School
ss_2019 = csv_to_list("../../startup_school/Startup School 2019.csv")
ss_2020 = csv_to_list("../../startup_school/Startup School 2020.csv")
ss_2021 = csv_to_list("../../startup_school/Startup School 2021.csv")
ss = [ss_2019, ss_2020, ss_2021]

# HTSAS
htsas_2019 = csv_to_list("../../HTSAS/htsas_2019.csv")
htsas_2020 = csv_to_list("../../HTSAS/htsas_2020.csv")
htsas_2021 = csv_to_list("../../HTSAS/htsas_2021.csv")
htsas = [htsas_2019, htsas_2020, htsas_2021]

# Bootcamp Apps
bc_2019 = csv_to_list("../../application_programs/bootcamps/applications_19_person_view.csv")
bc_2020 = csv_to_list("../../application_programs/bootcamps/applications_20_person_view.csv")
bc_2021 = csv_to_list("../../application_programs/bootcamps/applications_21_person_view.csv")
bcs = [bc_2019, bc_2020, bc_2021]

# JSprint
jsprint_2019 = csv_to_list("../../application_programs/jsprints/jsprint2019_apps.csv")
jsprint_2020 = csv_to_list("../../application_programs/jsprints/jsprint2020_apps.csv")
jsprint_2021 = csv_to_list("../../application_programs/jsprints/jsprint2021_apps.csv")
jsprints = [jsprint_2019, jsprint_2020, jsprint_2021]

# Summer Sprint
summer_sprint_2019 = csv_to_list("../../application_programs/summer_accelerators/sprint/ssprint_applications_2019.csv")
summer_sprint_2020 = csv_to_list("../../application_programs/summer_accelerators/sprint/ssprint_applications_2020.csv")
summer_sprint_2021 = csv_to_list("../../application_programs/summer_accelerators/sprint/ssprint_applications_2021.csv")
summer_sprints = [summer_sprint_2019, summer_sprint_2020, summer_sprint_2021]

# SLP
slp_2019 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_applications_2019.csv")
slp_2020 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_applications_2020.csv")
slp_2021 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_applications_2021.csv")
slps = [slp_2019, slp_2020, slp_2021]

# -------------- MAIN --------------

start = timeit.default_timer() # Time program run

print("\nCalculating people adjacency...\n") # DEBUG
for item in all_people:
  name = sorted(item)[0]
  item = add_adjacency(item, name, coaching, 1, 0) # Loop through coaching years
  item = add_adjacency(item, name, ff, 0, 2) 
  item = add_adjacency(item, name, ss, 1, 1) 
  item = add_adjacency(item, name, htsas, 1, 3) 
  item = add_adjacency(item, name, bcs, 1, 4) 
  item = add_adjacency(item, name, jsprints, 1, 5) 
  item = add_adjacency(item, name, summer_sprints, 1, 6) 
  item = add_adjacency(item, name, slps, 1, 7) 

print("Calculating organization adjacency...\n") # DEBUG
for item in all_orgs:
  name = sorted(item)[0]
  item = binary_adjacency(item, name, bcs, 0, 4) 
  item = binary_adjacency(item, name, jsprints, 0, 5) 
  item = binary_adjacency(item, name, summer_sprints, 0, 6) 
  item = binary_adjacency(item, name, slps, 0, 7) 

print("Filtering zeros from people adjacency...\n")
all_people = filter_zeros(all_people)
print("Filtering zeros from organization adjacency...\n")
all_orgs = filter_zeros(all_orgs)

# Print format
print("Writing to people adjacency...\n")
print_adj(all_people, people_adj, people_list, simplified_people_adj)
print("Writing to organization adjacency...\n")
print_adj(all_orgs, teams_adj, teams_list, simplified_teams_adj)

# End timer
stop = timeit.default_timer() # Time program run
print('Time: ', stop - start, "seconds\n")

# Close files
simplified_people_adj.close()
simplified_teams_adj.close()
people_adj.close()
teams_adj.close()
for i in range(0,3):
  teams_list[i].close()
  people_list[i].close()