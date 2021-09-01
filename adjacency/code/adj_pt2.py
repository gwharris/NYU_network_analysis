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
  jsprint_2019 = csv_to_list("../../application_programs/jsprints/jsprint2019_apps.csv")
  jsprint_2020 = csv_to_list("../../application_programs/jsprints/jsprint2020_apps.csv")
  jsprint_2021 = csv_to_list("../../application_programs/jsprints/jsprint2021_apps.csv")
  # Summer Sprint
  summer_sprint_2019 = csv_to_list("../../application_programs/summer_accelerators/sprint/ssprint_applications_2019.csv")
  summer_sprint_2020 = csv_to_list("../../application_programs/summer_accelerators/sprint/ssprint_applications_2020.csv")
  summer_sprint_2021 = csv_to_list("../../application_programs/summer_accelerators/sprint/ssprint_applications_2021.csv")
  # SLP
  slp_2019 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_applications_2019.csv")
  slp_2020 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_applications_2020.csv")
  slp_2021 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_applications_2021.csv")
  all_files = [bc_2019, bc_2020, bc_2021, jsprint_2019, jsprint_2020, jsprint_2021, summer_sprint_2019, summer_sprint_2020, summer_sprint_2021,slp_2019, slp_2020, slp_2021]

  # Loop through all association files to link people to teams
  tpf.write("Team,Individual\n")
  # check = []

  for f in all_files:
    for line in f:
      line[0] = line[0].strip(" \"")
      line[1] = line[1].strip(" \"")
      item = line[0].title() + "," + line[1].title() + "\n"
      # if item not in check:
        # check.append(item)
        # tpf.write(item)
      if line[0] in team_to_people:
        team_to_people[line[0]].append(line[1])
      else:
        team_to_people[line[0]] = [line[1]]
  
  return team_to_people

# Participant files
participants2019 = csv_to_list("../../application_programs/master_lists/18-19 Teams App.csv")
participants2020 = csv_to_list("../../application_programs/master_lists/19-20 Teams App.csv")
participants2021 = csv_to_list("../../application_programs/master_lists/20-21 Teams App.csv")

# Write files
added_adj = open("../data/added_adjacency.csv", 'w') # adjacency to add to lists
bad = open("../data/unable_to_resolve.csv", "w")
bad.write("List of companies that did not register in the algorithm due to a number of reasons - name changes; misspellings; punctuation; etc.,Graham's Notes\n")

tp = association() # also prints association file
print(len(tp))

# TEAMS
bc2019 = []
bc2020 = []
bc2021 = []
sp2019 = []
sp2020 = []
sp2021 = []
sl2019 = []
sl2020 = []
sl2021 = []
added_adj.write("\tTEAMS\n")
added_adj.write("\n2018-2019\n")
for line in participants2019:
  if line[3] == "yes":
    added_adj.write(line[0].title() + ",Bootcamp Participant 2019," + str(1) + "\n")
    bc2019.append(line[0])
  if line[4] == "yes":
    added_adj.write(line[0].title() + ",Sprint Participant 2019," + str(1) + "\n")
    sp2019.append(line[0])
  if line[7] == "yes":
    added_adj.write(line[0].title() + ",SLP Participant 2019," + str(1) + "\n")
    sl2019.append(line[0])
added_adj.write("\n2019-2020\n")
for line in participants2020:
  if line[3] == "yes":
    added_adj.write(line[0].title() + ",Bootcamp Participant 2020," + str(1) + "\n")
    bc2020.append(line[0])
  if line[4] == "yes":
    added_adj.write(line[0].title() + ",Sprint Participant 2020," + str(1) + "\n")
    sp2020.append(line[0])
  if line[8] == "yes":
    added_adj.write(line[0].title() + ",SLP Participant 2020," + str(1) + "\n")
    sl2020.append(line[0])
added_adj.write("\n2020-2021\n")
for line in participants2021:
  if line[2] == "yes":
    added_adj.write(line[0].title() + ",Bootcamp Participant 2021," + str(1) + "\n")
    bc2021.append(line[0])
  if line[3] == "yes":
    added_adj.write(line[0].title() + ",Sprint Participant 2021," + str(1) + "\n")
    sp2021.append(line[0])
  if line[4] == "yes":
    added_adj.write(line[0].title() + ",SLP Participant 2021," + str(1) + "\n")
    sl2021.append(line[0])

# PEOPLE
added_adj.write("\n\n\tPEOPLE\n")

print("\n\n\n")
added_adj.write("\n2018-2019\n")
for team in bc2019:
  if team in tp:
    for person in tp[team]:
      added_adj.write(person.title() + ",Bootcamp Participant 2019," + str(1) + "\n")
  else:
    bad.write(team + ",could not be found 2019 bc\n")
for team in sp2019:
  if team in tp:
    for person in tp[team]:
      added_adj.write(person.title() + ",Sprint Participant 2019," + str(1) + "\n")
  else:
    bad.write(team + ",could not be found 2019 sp\n")
for team in sl2019:
  if team in tp:
    for person in tp[team]:
      added_adj.write(person.title() + ",SLP Participant 2019," + str(1) + "\n")
  else:
    bad.write(team + ",could not be found 2019 slp\n")
added_adj.write("\n2019-2020\n")
for team in bc2020:
  if team in tp:
    for person in tp[team]:
      added_adj.write(person.title() + ",Bootcamp Participant 2020," + str(1) + "\n")
  else:
    bad.write(team + ",could not be found 2020 bc\n")
for team in sp2020:
  if team in tp:
    for person in tp[team]:
      added_adj.write(person.title() + ",Sprint Participant 2020," + str(1) + "\n")
  else:
    bad.write(team + ",could not be found 2020 sp\n")
for team in sl2020:
  if team in tp:
    for person in tp[team]:
      added_adj.write(person.title() + ",SLP Participant 2020," + str(1) + "\n")
  else:
    bad.write(team + ",could not be found 2020 slp\n")
added_adj.write("\n2020-2021\n")
for team in bc2021:
  if team in tp:
    for person in tp[team]:
      added_adj.write(person.title() + ",Bootcamp Participant 2021," + str(1) + "\n")
  else:
    bad.write(team + ",could not be found 2021 bc\n")
for team in sp2021:
  if team in tp:
    for person in tp[team]:
      added_adj.write(person.title() + ",Sprint Participant 2021," + str(1) + "\n")
  else:
    bad.write(team + ",could not be found 2021 sp\n")
for team in sl2021:
  if team in tp:
    for person in tp[team]:
      added_adj.write(person.title() + ",SLP Participant 2021," + str(1) + "\n")
  else:
    bad.write(team + ",could not be found 2021 slp\n")
