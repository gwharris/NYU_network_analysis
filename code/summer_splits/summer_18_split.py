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
  print_range(file, line, 3, 11)
  print_range(file, line, 11, 19)
  if line[19] != "" and line[20] != "":
    print_range(file, line, 19, 27)
  if line[27] != "" and line[28] != "":
    print_range(file, line, 27, 35)

# -------------- MAIN --------------

apps = csv_to_list("../../summer_accelerators/SA_2018/Accelerators2018.csv")
slp = open("../../summer_accelerators/SA_2018/slp_2018.csv", "w")
sprint = open("../../summer_accelerators/SA_2018/summer_sprint_2018.csv", "w")
all_apps = open("../../summer_accelerators/SA_2018/all_applications_2018.csv", "w")
slp.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s)\n")
sprint.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s)\n")
all_apps.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s)\n")

for line in apps:
  if "Yes" in line[0]:
    format(sprint, line)
  if "Yes" in line[1]:
    format(slp, line)
  format(all_apps, line)
  
slp.close()
sprint.close()
all_apps.close()