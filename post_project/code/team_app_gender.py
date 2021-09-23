"""
Graham Harris
Post Project Analysis
Calculate percentage of teams who have at least 1 female cofounder, etc.
"""

import sys

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

def print_format(arg, path, fd):
  index = 9
  if "bc" in arg:
    index = 10
    
  female = []
  male = []
  all_teams = []
  f_identifier = ["she", "her", "hers", "female", "woman"]
  m_identifier = ["he", "him", "his", "male", "man"]
  for line in path:
    flag = 0
    line[0] = line[0].strip("\"\'\\ ")
    for id in f_identifier:
      if id in line[index] and line[0] not in female:
        female.append(line[0])
        flag = 1
    for id in m_identifier:
      if id in line[index] and line[0] not in male and flag != 1:
        male.append(line[0])
    if line[0] not in all_teams:
      all_teams.append(line[0])

  fd.write(arg + ":\n")
  fd.write("Teams with at least 1 male-identifying individual: " + str(len(male)) + "\n")
  fd.write("Percent of teams 1 with male-identifying individual: " + str(len(male)/len(all_teams)* 100) + "\n")
  fd.write("Teams with at least 1 female-identifying individual: " + str(len(female)) + "\n")
  fd.write("Percent of teams 1 with female-identifying individual: " + str(len(female)/len(all_teams) * 100) + "\n")
  fd.write("Number of total teams: " + str(len(all_teams)) + "\n\n")

  print(arg + " success\n")

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

fd = open("../data/gender/app_teams_split.txt", "w")

print_format("bc 2019-2020", bc_2020, fd)
print_format("bc 2020-2021", bc_2021, fd)
print_format("jsprint 2018-2019", jsprint_2019, fd)
print_format("jsprint 2019-2020", jsprint_2020, fd)
print_format("jsprint 2020-2021", jsprint_2021, fd)
print_format("ssprint 2018-2019", summer_sprint_2019, fd)
print_format("ssprint 2019-2020", summer_sprint_2020, fd)
print_format("ssprint 2020-2021", summer_sprint_2021, fd)
print_format("slp 2018-2019", slp_2019, fd)
print_format("slp 2019-2020", slp_2020, fd)
print_format("slp 2020-2021", slp_2021, fd)

