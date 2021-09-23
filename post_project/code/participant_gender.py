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

fd = open("../data/gender/teams_split.txt", "w")

for arg in sys.argv:
  try:
    lines = csv_to_list("../data/gender/" + arg + ".csv")
    index = 9
    if "bc" in arg:
      index = 10
    
    female = []
    male = []
    all_teams = []
    f_identifier = ["she", "her", "hers", "female", "woman"]
    m_identifier = ["he", "him", "his", "male", "man"]
    for line in lines:
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

  except:
    print(arg + " error\n")