"""
Graham Harris
Summer Data Project
Splits the entries in the 2018 Summer Accelerator application into a person-centric view.
"""

# -------------- METHODS --------------

# Converts CSV to a 2D/nested Python list structure.
def csv_to_list(path):
  fd = open(path, "r")
  fd.readline() # get rid of title line
  rc = []
  for line in fd:
    line = line.split(",")
    rc.append(line)
  fd.close()
  return rc

def print_range(file, line, num1, num2):
  file.write(line[2] + ",")
  for i in range(num1, num2):
    file.write(line[i] + ",")
  file.write("\n")

def format(file, line):
  print_range(file, line, 3, 12)
  print_range(file, line, 12, 21)
  if line[21] != "" and line[22] != "":
    print_range(file, line, 21, 30)
  if line[30] != "" and line[31] != "":
    print_range(file, line, 30, 39)

# -------------- MAIN --------------

apps = csv_to_list("../../summer_accelerators/SA_2019/Accelerators2019.csv")
slp = open("../../summer_accelerators/SA_2019/slp_2019.csv", "w")
sprint = open("../../summer_accelerators/SA_2019/summer_sprint_2019.csv", "w")
all_apps = open("../../summer_accelerators/SA_2019/all_applications_2019.csv", "w")
slp.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s),If you identify with an under-represented population in STEM  please describe\n")
sprint.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s),If you identify with an under-represented population in STEM  please describe\n")
all_apps.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s),If you identify with an under-represented population in STEM  please describe\n")

for line in apps:
  if "Yes" in line[0]:
    format(sprint, line)
  if "Yes" in line[1]:
    format(slp, line)
  format(all_apps, line)
  
slp.close()
sprint.close()
all_apps.close()