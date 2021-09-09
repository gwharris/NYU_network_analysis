"""
Graham Harris
Summer Data Project
Splits the entries in the 2019 Summer Accelerator application into a person-centric view.
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

apps = csv_to_list("../../application_programs/summer_accelerators/SA_2019/Accelerators2019.csv")
slp = open("../../application_programs/summer_accelerators/SA_2019/slp_applications_2019.csv", "w")
sprint = open("../../application_programs/summer_accelerators/SA_2019/ssprint_applications_2019.csv", "w")
slp.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s),If you identify with an under-represented population in STEM  please describe\n")
sprint.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s),If you identify with an under-represented population in STEM  please describe\n")

for line in apps:
  if "Sprint" in line[44]:
    format(sprint, line)
  elif "SLP" in line[44]:
    format(slp, line)
  elif "Both" in line[44]:
    format(slp, line)
    format(sprint, line)
  else:
    print("wrong column")
  
slp.close()
sprint.close()