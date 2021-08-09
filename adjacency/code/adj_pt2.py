"""
Graham Harris
Summer Data Project
Adjacency Part 2: Created post-interim presentation. Further helps to clarify the difference between application and participant data. Hard-coded solution because data storage is inconsistent.
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

# Loop through all association files to link people to teams
def association():
  team_to_people = {}
  tpf = open("../data/team_to_people.csv", "w") # associates teams to people and vice versa
  # Bootcamp Apps
  bc_2019 = csv_to_list("../../application_programs/bootcamps/applications_19_person_view.csv")
  bc_2020 = csv_to_list("../../application_programs/bootcamps/applications_20_person_view.csv")
  bc_2021 = csv_to_list("../../application_programs/bootcamps/applications_21_person_view.csv")
  # JSprint
  jsprint_2019 = csv_to_list("../../application_programs/jsprints/jsprint2019_cleaned.csv")
  jsprint_2020 = csv_to_list("../../application_programs/jsprints/jsprint2020_cleaned.csv")
  jsprint_2021 = csv_to_list("../../application_programs/jsprints/jsprint2021_cleaned.csv")

  # Summer Applicants
  summer_app_2019 = csv_to_list("../../application_programs/summer_accelerators/apps/all_applications_2019.csv")
  summer_app_2020 = csv_to_list("../../application_programs/summer_accelerators/apps/all_applications_2020.csv")
  summer_app_2021 = csv_to_list("../../application_programs/summer_accelerators/apps/all_applications_2021.csv")
  # Summer Sprint
  summer_sprint_2019 = csv_to_list("../../application_programs/summer_accelerators/sprint/summer_sprint_2019.csv")
  summer_sprint_2020 = csv_to_list("../../application_programs/summer_accelerators/sprint/summer_sprint_2020.csv")
  summer_sprint_2021 = csv_to_list("../../application_programs/summer_accelerators/sprint/summer_sprint_2021.csv")
  # SLP
  slp_2019 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_2019.csv")
  slp_2020 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_2020.csv")
  slp_2021 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_2021.csv")
  all_files = [bc_2019, bc_2020, bc_2021, jsprint_2019, jsprint_2020, jsprint_2021, summer_app_2019, summer_app_2020, summer_app_2021, summer_sprint_2019, summer_sprint_2020, summer_sprint_2021,slp_2019, slp_2020, slp_2021]

  # Loop through all association files to link people to teams
  tpf.write("Team,Individual\n")
  for f in all_files:
    for line in f:
      x = line[0].strip(" ")
      y = line[1].strip(" ")
      tpf.write(x.title() + "," + y.title() + "\n")

bc2019 = csv_to_list("../../application_programs/master_lists/18-19 Teams App.csv")
###### missing one
bc2021 = csv_to_list("../../application_programs/master_lists/20-21 Teams App.csv")

# Write files
added_adj = open("../data/added_adjacency.csv", 'w') # adjacency to add to lists

# PEOPLE
added_adj.write("PEOPLE\n\n")


# TEAMS
added_adj.write("\nTEAMS\n\n")
added_adj.write("2019\n")
for line in bc2019:
  if line[3] == "yes":
    added_adj.write(line[0].title() + ",Bootcamp Participant 2019," + str(1) + "\n")
# added_adj.write("\n2020\n")
# for line in bc2020:
#   if line[X] == "yes":
#     added_adj.write(line[0].title() + ",Bootcamp Participant 2020," + str(1) + "\n")
added_adj.write("\n2021\n")
for line in bc2021:
  if line[2] == "yes":
    added_adj.write(line[0].title() + ",Bootcamp Participant 2021," + str(1) + "\n")


# association() only needed to run once