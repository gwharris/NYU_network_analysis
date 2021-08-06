"""
Graham Harris
Summer Data Project
Created post-interim presentation - further helps to clarify the difference between application and participant data. Hard-coded solution because data storage is inconsistent.
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

bc2019 = csv_to_list("../../application_programs/master_lists/18-19 Teams App.csv")
###### missing one
bc2021 = csv_to_list("../../application_programs/master_lists/20-21 Teams App.csv")

teams_2019 = open("../data/2019_teams.csv", 'a')
teams_2021 = open("../data/2021_teams.csv", 'a')
for line in bc2019:
  if line[3] == "Yes":
    teams_2019.write(line[0] + ",Bootcamp Participant 2019," + str(1))
for line in bc2021:
  if line[2] == "Yes":
    teams_2021.write(line[0] + ",Bootcamp Participant 2021," + str(1))