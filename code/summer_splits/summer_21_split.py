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
  if line[12] == "No":
    return
  print_range(file, line, 13, 22)
  if line[22] == "No":
    return
  print_range(file, line, 23, 32)
  if line[32] == "No":
    return
  print_range(file, line, 33, 40)

# -------------- MAIN --------------

apps = csv_to_list("../../application_programs/summer_accelerators/SA_2021/Accelerators2021.csv")
slp = open("../../application_programs/summer_accelerators/SA_2021/slp_applications_2021.csv", "w")
sprint = open("../../application_programs/summer_accelerators/SA_2021/ssprint_applications_2021.csv", "w")
slp.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s),If you identify with an under-represented population in STEM  please describe\n")
sprint.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s),If you identify with an under-represented population in STEM  please describe\n")

for line in apps:
  if "Sprint" in line[56]:
    format(sprint, line)
  elif "SLP" in line[56]:
    format(slp, line)
  elif "Both" in line[56]:
    format(slp, line)
    format(sprint, line)
  else:
    print("wrong column")
  print("x")
  
slp.close()
sprint.close()