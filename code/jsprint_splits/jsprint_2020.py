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
  file.write(line[0] + ",")
  for i in range(num1, num2):
    file.write(line[i] + ",")
  file.write("\n")

# -------------- MAIN --------------

apps = csv_to_list("../../jsprints/2020/jsprint2020.csv")
ss = open("../../application_programs/jsprints/2020/jsprint2020_cleaned.csv", "w")
ss.write("Team/Venture Name,First Name,Last Name,Email,NYU Affiliation,NYU Net ID (ex. jcc23),NYU School/College,Expected Graduation Year,Pronoun(s),Diversity,If you identify with an under-represented population in STEM please describe\n")

for line in apps:
  print_range(ss, line, 1, 11)
  if line[1] != line[11] and line[2] != line[12]:
    print_range(ss, line, 11, 21)
  if line[21] != "" and line[22] != "":
    print_range(ss, line, 21, 31)
  if line[31] != "" and line[32] != "":
    print_range(ss, line, 31, 41)

ss.close()