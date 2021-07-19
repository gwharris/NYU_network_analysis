"""
Graham Harris
Summer Data Project
Splits the entries in the 2020 JSprint application into a person-centric view.
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

# -------------- MAIN --------------

apps = csv_to_list("../../jsprints/2019/jsprint2019.csv")
ss = open("../../jsprints/2019/jsprint2019_cleaned.csv", "w")
ss.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s),If you identify with an under-represented population in STEM please describe\n")
not_acc = open("../../jsprints/2019/jsprint2019_applied_not_accepted.csv", "w")
not_acc.write("Team/Venture Name,First Name,Last Name,Email,NYU Net ID (ex. jcc23),NYU Affiliation,NYU School/College,Expected Graduation Year,Pronoun(s),If you identify with an under-represented population in STEM please describe\n")

for line in apps:
  if line[0] == "Yes" and line[1] == "Yes":
    print_range(ss, line, 3, 12)
    print_range(ss, line, 12, 21)
    if line[21] != "" and line[22] != "":
      print_range(ss, line, 21, 30)
    if line[30] != "" and line[31] != "":
      print_range(ss, line, 30, 39)
  else:
    print_range(not_acc, line, 3, 12)
    print_range(not_acc, line, 12, 21)
    if line[21] != "" and line[22] != "":
      print_range(not_acc, line, 21, 30)
    if line[30] != "" and line[31] != "":
      print_range(not_acc, line, 30, 39)

ss.close()